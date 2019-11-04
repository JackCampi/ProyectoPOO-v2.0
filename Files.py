"""Módulo Files, maneja todo lo relacionado con los archivos y la
    representación interna de los elementos"""
import os
import Format


class Lists:
    def __init__(self, _format, name="Main_list.txt"):
        """
        Recibe el formato y el nombre de una lista, este nuevo objeto tiene las siguientes propiedades:
        path: La ubicación de la lista.
        list: La lista de entradas (ver clase Entry)

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista, por defecto es "Main_list.txt
        """
        self.format = _format
        self.name = name
        self.path = self.format + os.sep + self.name
        self.list = []
        self.length = 0

    def Update(self):
        """
        Actualiza la lista de entradas.
        """
        self.length = len(self.list)

    def WriteList(self):
        """
        Solo sobrescribe la información de la lista de diccionarios en el archivo.
        """
        fileHandler = open(self.path, "w")
        for i in self.list:
            fileHandler.write(i.ToString() + "\n")
        fileHandler.close()
        self.Update()

    def AddEntry(self, newEntry):
        """
        Recibe una entrada y la añade a la lista de entradas.

        :param newEntry: Entrada que será agregada (ver clase Entry).
        """
        self.list.append(newEntry)
        self.WriteList()

    def DeleteEntry(self, entry):
        """
        Recibe una entrada y la elimina de la lista de entradas.

        :param entry: Entrada que será eliminada (ver clase Entry).
        """
        self.list.remove(entry)
        self.WriteList()

    def ModifyList(self, newEntry, oldEntry):
        """
        Sobrescribe la información de la nueva entrada en la vieja entrada.

        :param newEntry: Nueva entrada (ver clase Entry).
        :param oldEntry: Vieja entrada (ver clase Entry).
        """
        self.DeleteEntry(oldEntry)
        self.AddEntry(newEntry)


class Mainlist(Lists):
    def __init__(self, _format, name="Main_list.txt"):
        """
        Recibe el formato y el nombre de una lista, este nuevo objeto tiene las siguientes propiedades:
        path: La ubicación de la lista.
        list: La lista de entradas (ver clase Entry)

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista, por defecto es "Main_list.txt
        """
        super().__init__(_format, name)
        fileHandler = open(self.path, "r")
        self.list = []
        constructor = None
        if _format == "music":  # Escoger el constructor adecuado
            constructor = Format.Music
        elif _format == "videos":
            constructor = Format.Videos
        elif _format == "pictures":
            constructor = Format.Pictures

        for line in fileHandler:
            name, author, album, year, _type, path = line.split("¬")
            entry = constructor(name, author, album, year, _type, path)
            self.list.append(entry)

        self.length = len(self.list)
        fileHandler.close()


class Playlist(Lists):
    def __init__(self, _format, name):
        """
        Recibe el formato y el nombre de una lista de reproducción, para crear su archivo asociado,
        adicionalmente, hace una instancia del tipo Playlist que hereda de la clase Lists para manejar
        la lista de reproducción.

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista de reproducción.
        """
        super().__init__(_format, name)
        self.path = _format + os.sep + "playlists" + os.sep + name
        fileHandler = open(self.path, "w")
        fileHandler.close()

    def DeletePlaylist(self):
        """
        Borra el archivo de la playlist.
        """
        os.remove(self.path)


class PlaylistList:
    """
    Clase para sacar la lista de listas de reproducción.
    """
    def __init__(self, _format):
        path = _format + os.sep + "playlists"
        self.__playlists = []
        for root, directory, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    self.__playlists.append(file[:-4])

    def GetPlaylists(self):
        return self.__playlists.copy()


# PRUEBAS
