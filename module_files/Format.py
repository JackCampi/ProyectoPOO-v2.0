"""En este módulo se encuentran las clases de los formatos multimedia que se
manejan en la aplicación: Música, Fotos o Videos."""

class Format:
    """En esta clase se encuentran los métodos y propiedades comúes de los tres
    formatos, tales como el nombre, el autor, el álbum, el año, el archivo, el género
    y los settes y getters de cada propiedad."""

    def __init__ (self, name, author, album, year, type, path):
        """En el constructor de la clase se les asigna un valor a las propiedades
        de la clase. Dichas propiedades son privadas y sólamente se pueden acceder
        a ellas mediante los métodos de setters y getters.
        -También crea una propiedad que corresponde a un string que junta todas
        las propiedades en un string separado por el símbolo "¬"."""
        self.__name = name
        self.__author = author
        self.__year = year
        self.__album = album
        self.__type = type
        self.__path = path
        self.string = "¬".join((name, author, album, year, type, path))
        nameL, authorL, yearL, albumL, typeL = map(len, (name, author, year, album, type))
        self.lengths = {"name": nameL, "author": authorL, "year": yearL, "album": albumL, "type": typeL}

    def setName(self,newName):
        """Este método corresponde al de asignación externa del parámetro Name."""
        self.__name = newName
        return

    def getName(self):
        """Este método corresponde al de acceso externo del parámetro Name."""
        return self.__name

    def setAuthor(self,newAuthor):
        """Este método corresponde al de asignación externa del parámetro Author."""
        self.__author = newAuthor
        return

    def getAuthor(self):
        """Este método corresponde al de acceso externo del parámetro Author."""
        return self.__author

    def setYear(self,newYear):
        """Este método corresponde al de asignación externa del parámetro year."""
        self.__year = newYear
        return

    def getYear(self):
        """Este método corresponde al de acceso externo del parámetro Year."""
        return self.__year

    def setAlbum(self,newAlbum):
        """Este método corresponde al de asignación externa del parámetro Album."""
        self.__album = newAlbum
        return

    def getAlbum(self):
        """Este método corresponde al de acceso externo del parámetro Album."""
        return self.__album

    def setType(self,newType):
        """Este método corresponde al de asignación externa del parámetro Type."""
        self.__type = newType
        return

    def getType(self):
        """Este método corresponde al de acceso externo del parámetro Type."""
        return self.__type

    def setPath(self,newPath):
        """Este método corresponde al de asignación externa del parámetro Path."""
        self.__path = newPath
        return

    def getPath(self):
        """Este método corresponde al de acceso externo del parámetro Path."""
        return self.__path

    def Print(self, spaces, dicIndex=0):
        toPrint = str(dicIndex + 1) + "\t|"
        toPrint += self.__name + (" " * (spaces["name"] - len(self.__name))) + "|"
        toPrint += self.__author + (" " * (spaces["author"] - len(self.__author))) + "|"
        toPrint += self.__album + (" " * (spaces["album"] - len(self.__album))) + "|"
        toPrint += self.__year + (" " * (spaces["year"] - len(self.__year))) + "|"
        toPrint += self.__type + (" " * (spaces["type"] - len(self.__type))) + "|"
        print(toPrint)

class Music(Format):
    """Esta clase crea los objetos de tipo Music con métodos y propiedades de la
    clase Format."""
    pass

class Pictures(Format):
    """Esta clase crea los objetos de tipo Pictures con métodos y propiedades de la
    clase Format."""
    pass

class Videos(Format):
    """Esta clase crea los objetos de tipo Videos con métodos y propiedades de la
    clase Format."""
    pass
