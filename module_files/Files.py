"""Módulo Files, maneja:
    Los archivos y la representación interna de los elementos.*
    Las listas principales y de reproducción.
    *Más en el módulo Format."""
import os
from module_files import Format


class Lists:
    """
    La clase Lists tiene las siguientes propiedades:
    self.format (str): El formato ("music", "videos" o "pictures")
    self.name (str): El nombre de archivo de la lista.
    self.path (str): La ubicación del archivo en el PC ("C:\\..\\..\\carpeta\\..\\ejemplo.txt")
        De ahora en adelante, al hablar de "el archivo" se refiere a este archivo.
    self.list (list): Donde se almacenará en internamente en python la lista, contiene elementos del tipo
        Music, Videos, Pictures (ver módulo Format)
    self.length (int): tamaño de list.
    """
    def __init__(self, _format, name="Main_list.txt"):
        """
        Crea una instancia de la clase Lists.

        :param _format: Es el nombre del formato, tiene que ser "music", "videos" o "pictures".
        :param name: "Es el nombre de la lista, por predeterminado es Main_list.txt, que es el nombre
        de las listas principales de cada formato.
        """
        self.format = _format
        self.name = name
        self.path = self.format + os.sep + self.name
        self.list = []
        self.length = 0

    def Open(self):
        """
        Abre el archivo y lo almacena en self.list.
        """
        fileHandler = open(self.path, "r")
        self.list = []
        constructor = None
        if self.format == "music":  # Escoger el constructor adecuado
            constructor = Format.Music
        elif self.format == "videos":
            constructor = Format.Videos
        elif self.format == "pictures":
            constructor = Format.Pictures

        for line in fileHandler:
            name, author, album, year, _type, path = line.strip().split("¬")
            entry = constructor(name, author, album, year, _type, path)
            self.list.append(entry)

        self.length = len(self.list)
        fileHandler.close()

    def Update(self):
        """
        Actualiza el tamaño de self.list.
        """
        self.length = len(self.list)

    def WriteList(self):
        """
        Sobrescribe la información de self.list en el archivo.
        """
        fileHandler = open(self.path, "w")
        for i in self.list:
            fileHandler.write(i.string + "\n")
        fileHandler.close()
        self.Update()

    def AddEntry(self, newEntry):
        """
        Recibe una entrada (ver módulo Format), la añade a self.list y actualiza el archivo.

        :param newEntry: Entrada que será agregada (ver módulo Format).
        """
        self.list.append(newEntry)
        self.WriteList()

    def DeleteEntry(self, entry):
        """
        Recibe una entrada y la elimina de la self.list y del archivo.

        :param entry: Entrada que será eliminada (ver módulo Format).
        """
        ans = []
        for i in self.list:
            equal = i.getName() == entry.getName() and i.getAuthor() == entry.getAuthor() \
                    and i.getYear() == entry.getYear() and i.getAlbum() == entry.getAlbum() \
                    and i.getType() == entry.getType()
            if not equal:
                ans.append(i)

        self.list = ans.copy()
        self.WriteList()

    def ModifyList(self, newEntry, oldEntry):
        """
        Sobrescribe la información de la nueva entrada en la vieja entrada.

        :param newEntry: Nueva entrada (ver módulo Format).
        :param oldEntry: Vieja entrada (ver módulo Format).
        """
        self.DeleteEntry(oldEntry)
        self.AddEntry(newEntry)

    def SortList(self, key):
        """
        función propia de las listas que ordena la lista (MainList o playlist)
        de acuerdo a un criterio (nombre, autor, etc...)
        RETURN: lista ordenada de objetos
        """
        self.__key = key
        if self.__key == "name":
            return sorted(self.list, key = lambda object : object.getName())
        elif self.__key == "author":
            return sorted(self.list, key = lambda object : object.getAuthor())
        elif self.__key == "album":
            return sorted(self.list, key = lambda object : object.getAlbum())
        elif self.__key == "year":
            return sorted(self.list, key = lambda object : object.getYear())
        elif self.__key == "type":
            return sorted(self.list, key = lambda object : object.getType())

    def Search(self, item):
        """
        función que recibe como parametro un item a buscar, busca en todas sus propiedades
        y retorna una lista de coincidencias (objetos ordenados por nombre)
        RETURN: lista de objetos ordenados por nombre
        """
        self.__item = item
        self.__itemsFound = set()
        for object in self.list:
            if self.__item in object.getName():
                self.__itemsFound.add(object)
            elif self.__item in object.getAuthor():
                self.__itemsFound.add(object)
            elif self.__item in object.getAlbum():
                self.__itemsFound.add(object)
            elif self.__item in object.getYear():
                self.__itemsFound.add(object)
            elif self.__item in object.getType():
                self.__itemsFound.add(object)
        self.__itemsFoundList = list(self.__itemsFound)
        return sorted(self.__itemsFoundList, key = lambda object : object.getName())


class MainList(Lists):
    """
    Hereda de Lists, sin cambios.
    Recomedación: Llamar sin espeficificar el argumento name, está ahí por cuestiones de depuración.
    """
    def __init__(self, _format, name="Main_list.txt"):
        """
        Recibe el formato y el nombre de una lista, este nuevo objeto tiene las siguientes propiedades:
        path: La ubicación de la lista.
        list: La lista de entradas (ver clase Entry)

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista, por defecto es "Main_list.txt
        """
        super().__init__(_format, name)
        self.Open()


class Playlist(Lists):
    """
    Hereda de Lists, por lo que sus propiedades son las mismas excepto por:
    self.path está modificado para acceder a la carpeta de playlists del formato,
        ("C:\\..\\..\\carpeta\\..\\playlists\\ejemplo.txt").
    """
    def __init__(self, _format, name):
        """
        Recibe el formato y el nombre de una lista de reproducción, para crear su archivo asociado,
        adicionalmente, hace una instancia del tipo Playlist que hereda de la clase Lists para manejar
        la lista de reproducción.

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista de reproducción SIN LA EXTENSIÓN.
        """
        super().__init__(_format, name)
        playlists = PlaylistList(_format).GetPlaylists()
        self.path = _format + os.sep + "playlists" + os.sep + name + ".txt"
        if name not in playlists:
            fileHandler = open(self.path, "a")
            fileHandler.close()
        else:
            self.Open()

    def DeletePlaylist(self):
        """
        Borra el archivo de la playlist.
        """
        os.remove(self.path)


class PlaylistList:
    """
    Clase para sacar la lista de listas de reproducción SIN la extensión.
    """
    def __init__(self, _format):
        """
        Recibe el formato y hace una lista de todas las playlists del formato.
        :param _format: (ver clase Lists)
        """
        path = _format + os.sep + "playlists"
        self.__playlists = []
        for root, directory, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    self.__playlists.append(file[:-4])

    def GetPlaylists(self):
        """
        Getter para la lista de playlists.

        :return: (list) lista de playlists en el formato.
        """
        return self.__playlists.copy()

    def SearchPlaylist(self, playlistName):
        """
        funcion que busca un nombre de una playlist dentro de todas
        las playlist existentes
        RETURN: lista de coincidencias
        """
        self.__playlistName = playlistName
        self.__itemsFoundList = []
        for item in self.__playlists:
            if self.__playlistName in item:
                self.__itemsFoundList.append(item)
        return sorted(self.__itemsFoundList)
