class Format:
    def __init__ (self, name, author, album, year, type, path):
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

    def Print(self, spaces, dicIndex=0):
        toPrint = str(dicIndex + 1) + "\t|"
        toPrint += self.__name + (" " * (spaces["name"] - len(self.__name))) + "|"
        toPrint += self.__author + (" " * (spaces["author"] - len(self.__author))) + "|"
        toPrint += self.__album + (" " * (spaces["album"] - len(self.__album))) + "|"
        toPrint += self.__year + (" " * (spaces["year"] - len(self.__year))) + "|"
        toPrint += self.__type + (" " * (spaces["type"] - len(self.__type))) + "|"
        print(toPrint)

class Music(Format):
    pass

class Pictures(Format):
    pass

class Videos(Format):
    pass
