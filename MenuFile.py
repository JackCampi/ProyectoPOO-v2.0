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
        return #listo

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
            return "videos" #listo

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

    def __SortListMenu(self, listObject):
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

    def NotFoundMenu(_format, listName ):
        print("No se encontró ningún elemento en " + listName +".\n")
        print("1. Volver a buscar.\n0. Atrás.\n")
        answer = Answer(["0","1"])
        return answer






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
            MainList = MainList(self.__format)
            self.__SortListMenu( MainList ) #MENU DE ORDENAR LISTA
        elif self.__answer == "2":
            self.__SearchMenu()
        elif self.__answer == "3":
            AddElementMenu(_format)
        self.__ThirdMenu()

    def __SearchMenu(self):
        print("\n===================0===================\n")
    	print("\tBUSCAR EN MI" + self.__MenuFormat(_format,False).upper()+ "\n")
    	toSearch = input("¿Qué desea buscar? ")
    	searchResults = Miscellaneous.SearchMainList(_format,toSearch)
    	if len(searchResults) == 0 :
    		answer = NotFoundMenu(_format, "mi" + MenuFormat(_format, False))
    		if answer == "0":
    			return
    		else:
    			SearchMenu(_format)
    			return
    	elif len(searchResults) == 1:
    		searchElement = searchResults[0]
    		self.__FoundElementMenu(_format, searchElement)
    		return
    	else:
    		PrintList(_format,searchResults)
    		searchElement = searchResults[SelectListElement(len(searchResults))]
    		self.__FoundElementMenu(_format, searchElement)
    		return

    def __FoundElementMenu(_format, foundElement):
        print("\n===================0===================\n")
        PrintListHead(_format)
        print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(foundElement["name"],foundElement["author"],foundElement["album"],foundElement["year"],foundElement["type"]))
        print("¿Qué desea hacer con este elemento?\n1. Añadir a lista de reproducción.\n2. Eliminar.\n3. Modificar información.\n\n0. Atrás.")
        answer = Answer(["0","1","2","3"])
        if answer == "0":
            return
        elif answer == "1":
            AddToPlaylistMenu(_format,foundElement)
            return
        elif answer == "2":
            files.DeleteEntry(foundElement, _format)
            print("Se ha eliminado el elemento. Volviendo a \"MI" + MenuFormat(_format,False).upper()+"\".")
            return
        elif answer == "3":
            ModifyElementMenu(_format,foundElement)
            return

    def AddToPlaylistMenu(_format, toAddElement):
        playlistList = files.GetPlaylists(_format)
        if len(playlistList) == 0:
            print("No se encontraron listas de reproducción en "+ MenuFormat(_format)+".")
            return
        else:
            for playlistIndex in range(len(playlistList)):
                print(str(playlistIndex+1)+"\t|\t"+ playlistList[playlistIndex] )
            playlistName = playlistList[SelectListElement(len(playlistList))]
            playlistPath = "playlists"+ os.sep + playlistName + ".txt"
            files.AddEntry(toAddElement ,_format , playlistPath)
            print("Se añadió \""+toAddElement["name"]+ "\" a " + playlistName + ".")
            return

    def ModifyElementMenu(_format, oldElementDic):
        print("\nIngrese la nueva información del elemento.")
        newElementDic = TakeElementInfo()
        files.ModifyList(newElementDic,oldElementDic,_format)
        print("Se ha modificado la información del elemento. Volviendo a \"MI" + MenuFormat(_format,False).upper()+"\".")

    def __FourthMenu(self):
        print("\n===================0===================\n")
        print("\tLISTAS DE REPRODUCCIÓN DE " + self.__MenuFormat().upper() + "\n")
        print("1. Mis listas.\n2. Crear lista.\n3. Buscar lista.\n4. Eliminar lista.\n\n0. Atrás.\n")
        self.__Answer(["0","1","2","3","4"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            playlists = files.GetPlaylists(_format) #hay que crear la función para esto
            if len(playlists) == 0:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                print("No hay listas de reproducción en " + MenuFormat(_format) + ".")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                wait = input("Pulse Enter para continuar...")
            else:
                for playlistIndex in range(len(playlists)):
                    print(str(playlistIndex+1)+"\t|\t"+playlists[playlistIndex] + ".\n")
                    print("\n1. Seleccionar una lista de reproducción.\n0. Atrás.\n")
                    answer1 = Answer(["0","1"])
                    if answer1 == "1":
                        playlistName = playlists[SelectListElement(len(playlists))]
                        PlaylistMenu(_format, playlistName)
        elif self.__answer == "2":
            NewPlaylistMenu(_format) #falta pasar
        elif self.__answer == "3":
            SearchPlaylistMenu(_format) #falta pasar
        elif self.__answer == "4":
            SearchPlaylistMenu(_format,"eliminar") #faltapasar
        self.__FourthMenu(_format)

    def SearchPlaylistMenu(_format, toDo = "buscar"):
        print("\n===================0===================\n")
        toSearch = input("¿Qué lista de reproducción desea "+ toDo +"? ")
        results = Miscellaneous.SearchItemInList(files.GetPlaylists(_format),toSearch)
        if len(results) == 0:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("No se encontró ninguna lista de reproducción en " + MenuFormat(_format) +".\n")
            print("1. Volver a buscar.\n0. Atrás.\n")
            answer = Answer(["0","1"])
            if answer == "0":
                return
            elif answer == "1":
                SearchPlaylistMenu(_format, toDo )
        elif len(results) == 1:
            foundPlaylist = results[0]
            if toDo == "eliminar":
                print("¿Desea eliminar "+foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
                answer1 = Answer(["0","1"])
                if answer1 == "0":
                    return
                elif answer1 == "1":
                    files.DeletePlaylist(_format,foundPlaylist)
                    print("Se ha eliminado " + foundPlaylist +".")
                    return
            elif toDo == "buscar":
                PlaylistMenu(_format, foundPlaylist)
                return
        else:
            print("Listas encontradas:\n")
            for foundPlaylistIndex in range(len(results)):
                print(str(foundPlaylistIndex+1)+"\t|\t"+results[foundPlaylistIndex])
            foundPlaylist = results[SelectListElement(len(results))]
            if toDo == "eliminar":
                print("¿Desea eliminar "+foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
                answer1 = Answer(["0","1"])
                if answer1 == "0":
                    return
                elif answer1 == "1":
                    files.DeletePlaylist(_format,foundPlaylist)
                    print("Se ha eliminado " + foundPlaylist +".")
                    return
            elif toDo == "buscar":
                PlaylistMenu(_format, foundPlaylist)
                return

    def NewPlaylistMenu(_format):
        print("\n===================0===================\n")
        print("\tCREAR LISTA DE REPRODUCCIÓN\n")
        playlistName = input("Nombre de la lista de reproducción: ")
        files.MakePlaylist(_format,playlistName)
        print("La lista de reproducción ha sido creada.\n\n¿Desea añadir elementos a la lista?\n1. Aceptar.\n0. Cancelar.\n")
        answer = Answer(["0","1"])
        if answer == "0":
            return
        else:
            adding = True
            while adding == True:
                AddPlaylistElement(_format, playlistName)
                print("¿Desea añadir otro elemento a la lista?\n1. Aceptar.\n0. Cancelar.\n")
                answer1 = Answer(["0","1"])
                if answer1 == "0":
                    adding = False
