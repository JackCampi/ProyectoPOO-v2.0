class Format:
    def __init__ (self, name, author, year, album, type, path):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__album = album
        self.__type = type
        self.__path = path

    def setName(self,newName):
        self.__name = newName
        return

    def getName(self):
        return self.__name

    def setAuthor(self,newAuthor):
        self.__author = newAuthor
        return

    def getAuthor(self):
        return self.__author

    def setYear(self,newYear):
        self.__year = newYear
        return

    def getYear(self):
        return self.__year

    def setAlbum(self,newAlbum):
        self.__album = newAlbum
        return

    def getAlbum(self):
        return self.__album

    def setType(self,newType):
        self.__type = newType
        return

    def getType(self):
        return self.__type

    def setPath(self,newPath):
        self.__path = newPath
        return

    def getPath(self):
        return self.__path

class Music(Format):
    pass

class Pictures(Format):
    pass

class Videos(Format):
    pass
