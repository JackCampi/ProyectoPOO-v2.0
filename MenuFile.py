#MenuFile
class MenuManagement:

    def __init__(self):
        pass

    def __Answer(self,options):
        self.__validAnswer = False
	    self.__answer = "x"
        while self.__validAnswer == False:
            self.__answer = input("Seleccione el número de la opción: ")
            if self.__answer in options:
                self.__validAnswer = True
            else:
                print("Respuesta inválida, por favor intente de nuevo.")
        return

    def __MenuFormat(self, onlyFormat = True):
        if self.__format == "music":
            if onlyFormat != True:
                return " música"
            return "música"
        elif self.__format == "pictures":
            if onlyFormat != True:
                return "s fotos"
            return "fotos"
        else:
            if onlyFormat != True:
                return "s videos"
            return "videos"

    def __AddElementMenu(self):
        print("\n===================0===================\n")
        print("\tAÑADIR A MI"+ self.__MenuFormat(False).upper() +"\n")
        newElementStr = self.__TakeElementInfo()
        files.AddEntry(newElementStr,self.__format) #Modificar
        print("\nEl elemento se ha añadido a \"mi{0}\".".format(self.__MenuFormat(False)))

    def __TakeElementInfo(self):
        name = input("Nombre: ")
        author = input("Autor: ")
        album = input("Álbum: ")
        year = input("Año: ")
        type = input("Género: ")
        path = input("Archivo: ")
        info = "¬".join([name, author, album, year, type, path])
        return info

    def __SortListMenu(self, listName , listObject):
        print("\n===================0===================\n")
        print("\tVER "+ listName.upper() +"\n") #LISTNAME
        print(self.__SortListMenuOptions())
        self.__Answer(["0","1","2","3","4","5"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            listToPrint = files.ReadFormat(_format,listPath)
            sortedList = Miscellaneous.SortList(listToPrint,"name")
            if len(sortedList) == 0:
                self.__emptyListMenu()
            else:
                PrintList(_format,sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "2":
            listToPrint = files.ReadFormat(_format,listPath)
            sortedList = Miscellaneous.SortList(listToPrint,"author")
            if len(sortedList) == 0:
                self.__emptyListMenu()
            else:
                PrintList(_format,sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "3":
            listToPrint = files.ReadFormat(_format,listPath)
            sortedList = Miscellaneous.SortList(listToPrint,"album")
            if len(sortedList) == 0:
                self.__emptyListMenu()
            else:
                PrintList(_format,sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "4":
            listToPrint = files.ReadFormat(_format,listPath)
            sortedList = Miscellaneous.SortList(listToPrint,"year")
            if len(sortedList) == 0:
                self.__emptyListMenu()
            else:
                PrintList(_format,sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "5":
            listToPrint = files.ReadFormat(_format,listPath)
            sortedList = Miscellaneous.SortList(listToPrint,"type")
            if len(sortedList) == 0:
                self.__emptyListMenu()
            else:
                PrintList(_format,sortedList)
                wait = input("Pulse Enter para continuar...")
            SortListMenu(_format, listName)

    def __SortListMenuOptions(self):
	if self.__format == "music":
		return "1. Por nombre.\n2. Por artista.\n3. Por álbum.\n4. Por año.\n5. Por género.\n\n0. Atrás.\n"
	else:
		return "1. Por nombre.\n2. Por protagonista.\n3. Por álbum.\n4. Por año.\n5. Por tipo.\n\n0. Atrás.\n"

    def __emptyListMenu(self, listName):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("No hay elementos en "+listName+".")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        wait = input("Pulse Enter para continuar...")
        return




class PincipalMenu (MenuManagement):

    def MainMenu(self):
        print("\n===================0===================\n")
        print("\tMENÚ PRINCIPAL\n\n1. Música.\n2. Fotos.\n3. Videos.\n\n0. Salir.\n")
        self.__Answer(["0","1","2","3"])
	    if self.__answer == "0":
            return
        elif self.__answer == "1":
            self.__format = "music"
            self.__SecondMenu()
        elif self.__answer == "2":
            self.__format = "pictures"
            self.__SecondMenu()
        elif self.__answer == "3":
            self.__format = "videos"
            self.__SecondMenu()
        self.MainMenu()

    def __SecondMenu(self): #FALTA MODIFICAR
        print("\n===================0===================\n")
        print("\t"+ self.__MenuFormat().upper()+"\n")
        print("1. Mi"+ self.__MenuFormat(False) +".\n2. Listas de reproducción.\n\n0. Atrás.\n")
        self.__Answer(["0","1","2"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            self.__ThirdMenu()
        elif self.__answer == "2":
            self.__FourthMenu()
        self.__SecondMenu()

    def __ThirdMenu(self):
        print("\n===================0===================\n")
        print("\tMI"+ self.__MenuFormat(False).upper()+"\n")
        print("1. Ver mi"+ self.__MenuFormat(False) +".\n2. Buscar.\n3. Añadir.\n\n0. Atrás.\n")
        self.__Answer(["0","1","2","3"])
        if answer3 == "0":
            return
        elif self.__answer == "1":
            listName = "mi"+ self.__MenuFormat(False)
            SortListMenu(_format, listName ) #MENU DE ORDENAR LISTA
        elif self.__answer == "2":
            SearchMenu(_format)
        elif self.__answer == "3":
            AddElementMenu(_format)
        self.__ThirdMenu()
