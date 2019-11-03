"""Módulo Files, maneja todo lo relacionado con los archivos y la
    representación interna de los elementos"""
import os


class Entry:
    def __init__(self, string):
        """
        Crea un objeto del tipo entrada con las siguientes características:
        order: tupla que indica el orden de la entrada.
        entry: diccionario que contiene la información organizada.

        :param string: La cadena que contiene la información de la nueva entrada,
              tiene que estar en el siguiente orden "nombre, autor, album,
              año, género". Además tiene que estar separada por el caracter "¬".
        """
        self.order = ("name", "author", "album", "year", "type", "path")
        elements = string.strip("\n").split("¬")
        self.entry = {}
        assert len(elements) == len(self.order), "Entrada inválida"
        for i in range(len(self.order)):
            self.entry[self.order[i]] = elements[i]

    def ToString(self):
        """
        Devuelve la representación de string de la entrada.

        :return: Una lista separada por el caracter ¬, que contiene la información de una
        entrada en el siguiente orden "nombre, autor, album, año, género, ubicación."
        """
        ans = ""
        for i in self.entry:
            ans += str(self.entry[i])
            ans += "¬"
        return ans[:-1]

    def __str__(self):
        # Esto es para encontrar errores con facilidad
        return str(self.entry)


class Format:
    def __init__(self, _format):
        """
        Crea un objeto del tipo Format.
        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        """
        self.format = _format

    def GetPlaylists(self):
        """
        :return: Lista con los nombres de las playlist del formato.
        """
        root = self.format
        path = root + os.sep + "playlists"
        ans = []
        for root, directory, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    ans.append(file[:-4])
        return ans


class Lists:
    def __init__(self, _format, name="Main_list.txt"):
        """
        Recibe el formato y el nombre de una lista, este nuevo objeto tiene las siguientes propiedades:
        path: La ubicación de la lista.
        list: La lista de entradas (ver clase Entry)

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista, por defecto es "Main_list.txt
        """
        root = _format
        self.path = root + os.sep + name
        fileHandler = open(self.path, "r")
        self.list = []
        for line in fileHandler:
            entry = Entry(line)
            self.list.append(entry)
        fileHandler.close()

    def UpdateList(self):
        """
        Actualiza la lista de entradas.
        """
        fileHandler = open(self.path, "r")
        self.list = []
        for line in fileHandler:
            entry = Entry(line)
            self.list.append(entry)
        fileHandler.close()

    def WriteList(self):
        """
        Solo sobrescribe la información de la lista de diccionarios en el archivo.
        """
        fileHandler = open(self.path, "w")
        for i in self.list:
            fileHandler.write(i.ToString() + "\n")
        fileHandler.close()

    def AddEntry(self, newEntry):
        """
        Recibe una entrada y la añade a la lista de entradas.

        :param newEntry: Entrada que será agregada (ver clase Entry).
        """
        self.list.append(newEntry)
        self.list.sort(key=lambda entr: entr.entry["name"])
        self.WriteList()

    def DeleteEntry(self, entry):
        """
        Recibe una entrada y la elimina de la lista de entradas.

        :param entry: Entrada que será eliminada (ver clase Entry).
        """
        fileHandler = open(self.path, "w")
        for i in self.list:
            if i != entry:
                fileHandler.write(i.ToString() + "\n")
        fileHandler.close()
        self.UpdateList()

    def ModifyList(self, newEntry, oldEntry):
        """
        Sobrescribe la información de la nueva entrada en la vieja entrada.

        :param newEntry: Nueva entrada (ver clase Entry).
        :param oldEntry: Vieja entrada (ver clase Entry).
        """
        self.DeleteEntry(oldEntry)
        self.AddEntry(newEntry)


class Playlist(Lists):
    def __init__(self, _format, name):
        """
        Recibe el formato y el nombre de una lista de reproducción, para crear su archivo asociado,
        adicionalmente, hace una instancia del tipo Playlist que hereda de la clase Lists para manejar
        la lista de reproducción.

        :param _format: El formato de la lista, puede ser "music", "pictures", o "videos."
        :param name: El nombre del archivo de la lista de reproducción.
        """
        root = _format
        self.path = root + os.sep + "playlists" + os.sep + name + ".txt"
        self.list = []
        fileHandler = open(self.path, "w")
        fileHandler.close()

    def DeletePlaylist(self):
        """
        Borra el archivo de la playlist.
        """
        os.remove(self.path)


# PRUEBAS

l = Lists("music")
n = Entry("abd¬agh¬tre¬ojk¬ear¬jhg")
n2 = Entry("ogf¬agh¬tre¬ojk¬ear¬jhg")
n3 = Entry("0fg¬agh¬tre¬ojk¬ear¬jhg")

pl = Playlist("music", "hola")

