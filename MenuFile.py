#MenuFile
import Files
import PlaylistMenuFile
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
        self.__newElement = self.__TakeElementInfo()
        self.__mainList = MainList(self.__format)
        self.__mainList.AddEntry(self.__newElement)# mirar que es param Entry
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

    def __SortListMenu(self, objectList, listName):
        self.__listName = listName
        self.__objectList = objectList #objeto de la clase Lists
        print("\n===================0===================\n")
        print("\tVER "+ self.__listName.upper() +"\n")
        print(self.__SortListMenuOptions())
        self.__Answer(["0","1","2","3","4","5"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            self.__sortedList = self.__objectList.SortList("name")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                self.__wait = input("Pulse Enter para continuar...")
        elif self.__answer == "2":
            self.__sortedList = self.__objectList.SortList("author")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                self.__wait = input("Pulse Enter para continuar...")
        elif self.__answer == "3":
            self.__sortedList = self.__objectList.SortList("album")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                self.__wait = input("Pulse Enter para continuar...")
        elif self.__answer == "4":
            self.__sortedList = self.__objectList.SortList("year")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                self.__wait = input("Pulse Enter para continuar...")
        elif self.__answer == "5":
            self.__sortedList = self.__objectList.SortList("type")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                self.__wait = input("Pulse Enter para continuar...")
        self.__SortListMenu(self.__objectList, self.__listName)

    def __SortListMenuOptions(self):
	if self.__format == "music":
		return "1. Por nombre.\n2. Por artista.\n3. Por álbum.\n4. Por año.\n5. Por género.\n\n0. Atrás.\n"
	else:
		return "1. Por nombre.\n2. Por protagonista.\n3. Por álbum.\n4. Por año.\n5. Por tipo.\n\n0. Atrás.\n"

    def __emptyListMenu(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("No hay elementos en "+ self.__listName +".")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        wait = input("Pulse Enter para continuar...")
        return

    def __NotFoundMenu(self, listName):
        self.__listName = listName
        print("No se encontró ningún elemento en " + self.__listName +".\n")
        print("1. Volver a buscar.\n0. Atrás.\n")
        self.__Answer(["0","1"])
<<<<<<< HEAD
        return
=======
        return self.__answer
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb

    def __PrintList(self, _list):
        self.__list = _list
        self.__PrintListHead()
        for dicIndex in range(len(self.__list)):
            self.__PrintListElement(self.__list , dicIndex)

    def __PrintListElement(self, _list,dicIndex = 0):
        self.__list = _list
        self.__index = dicIndex
        self.__toPrint = "{0}.\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\t|\t{5}\n"
        self.__item = self.__list[self.__index]
        print(self.__toPrint.format(self.__index+1,self.__item.getName(),self.__item.getAuthor()
                                    ,self.__item.getAlbum(),self.__item.getYear(),self.__item.getType()))
        return

    def __PrintListHead(self):
        if self.__format == "music":
            print("No.\t|\tNombre\t|\tArtista\t|\tÁlbum\t|\tAño\t|\tGénero\n")
        else:
            print("No.\t|\tNombre\t|\tProtagonista\t|\tÁlbum\t|\tAño\t|\tTipo\n")
        return

    def __SelectListElement(self, listLength):
        self.__listLength = listLength
        print("\n¿Cuál desea seleccionar? ")
<<<<<<< HEAD
        self.__Answer([str(x) for x in range(1,listLength+1)])
        return int(self.__answer) - 1
=======
        self.__selectElement = self.__Answer([str(x) for x in range(1,self.__listLength+1)])
        return int(self.__selectElement) - 1
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb





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

    def __SecondMenu(self):
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
        if self.__answer == "0":
            return
        elif self.__answer == "1": #MODIFICAR
            MainList = MainList(self.__format)
            self.__SortListMenu( MainList ) #MENU DE ORDENAR LISTA
        elif self.__answer == "2":
            self.__SearchMenu()
        elif self.__answer == "3":
            AddElementMenu(_format)
        self.__ThirdMenu()

    def __SearchMenu(self):
        print("\n===================0===================\n")
    	print("\tBUSCAR EN MI" + self.__MenuFormat(False).upper()+ "\n")
    	toSearch = input("¿Qué desea buscar? ")
    	searchResults = Miscellaneous.SearchMainList(_format,toSearch)
    	if len(searchResults) == 0 :
    		NotFoundMenu(_format, "mi" + self.__MenuFormat(False))
    		if self.__answer == "0":
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
        self.__Answer(["0","1","2","3"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            AddToPlaylistMenu(_format,foundElement)
            return
        elif self.__answer == "2":
            files.DeleteEntry(foundElement, _format)
            print("Se ha eliminado el elemento. Volviendo a \"MI" + self.__MenuFormat(False).upper()+"\".")
            return
        elif self.__answer == "3":
            ModifyElementMenu(_format,foundElement)
            return

<<<<<<< HEAD
    def AddToPlaylistMenu(_format, toAddElement):
        playlistList = files.GetPlaylists(_format)
        if len(playlistList) == 0:
=======
    def __AddToPlaylistMenu(self, toAddElement): #ya esta corregido a objetos
        self.__playlists = PlaylistList(self.__format) #objeto tipo PlaylistList
        self.__playlistList = self.__playlists.GetPlaylists()
        self.__toAddElement = toAddElement
        if len(self.__playlistList) == 0:
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb
            print("No se encontraron listas de reproducción en "+ self.__MenuFormat()+".")
            return
        else:
            for playlistIndex in range(len(self.__playlistList)):
                print(str(playlistIndex+1)+"\t|\t"+ self.__playlistList[playlistIndex] )
            self.__playlistName = self.__playlistList[self.__SelectListElement(len(self.__playlistList))]
            self.__playlistObject = Playlist(self.__format, self.__playlistName) #objeto de tipo Playlist
            self.__playlistObject.AddEntry(self.__toAddElement) #mirar ques es param Entry
            print("Se añadió \""+self.__toAddElement.getName()+ "\" a " + self.__playlistName + ".")
            return

    def ModifyElementMenu(_format, oldElementDic):
        print("\nIngrese la nueva información del elemento.")
        newElementDic = TakeElementInfo()
        files.ModifyList(newElementDic,oldElementDic,_format)
        print("Se ha modificado la información del elemento. Volviendo a \"MI" + self.__MenuFormat(False).upper()+"\".")

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
                print("No hay listas de reproducción en " + self.__MenuFormat() + ".")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                wait = input("Pulse Enter para continuar...")
            else:
                for playlistIndex in range(len(playlists)):
                    print(str(playlistIndex+1)+"\t|\t"+playlists[playlistIndex] + ".\n")
                    print("\n1. Seleccionar una lista de reproducción.\n0. Atrás.\n")
                    self.__Answer(["0","1"])
                    if self.__answer == "1":
                        playlistName = playlists[SelectListElement(len(playlists))]
                        PlaylistMenu(_format, playlistName)
        elif self.__answer == "2":
            NewPlaylistMenu(_format) #falta pasar --> ya esta // corregir llamadas a esta función
        elif self.__answer == "3":
            SearchPlaylistMenu(_format) #falta pasar --> ya esta // corregir llamadas a esta función
        elif self.__answer == "4":
            SearchPlaylistMenu(_format,"eliminar") #faltapasar --> ya esta // corregir llamadas a esta función
        self.__FourthMenu(_format)

    def __SearchPlaylistMenu(self, toDo = "buscar"): #ya esta pasada a objetos //si quieres mirar instanciacion de objetos
        self.__toDo = toDo
        print("\n===================0===================\n")
        self.__toSearch = input("¿Qué lista de reproducción desea "+ self.__toDo +"? ")
        self.__playlists = PlaylistList(self.__format) #objeto tipo PlaylistList
        self.__results = self.__playlists.SearchPlaylist(self.__toSearch)
        if len(self.__results) == 0:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("No se encontró ninguna lista de reproducción en " + self.__MenuFormat() +".\n")
            print("1. Volver a buscar.\n0. Atrás.\n")
            self.__Answer(["0","1"])
            if self.__answer == "0":
                return
            elif self.__answer == "1":
<<<<<<< HEAD
                SearchPlaylistMenu(_format, toDo )
        elif len(results) == 1:
            foundPlaylist = results[0]
            if toDo == "eliminar":
                print("¿Desea eliminar "+foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
=======
                self.__SearchPlaylistMenu(self.__toDo )
        elif len(self.__results) == 1:
            self.__foundPlaylist = self.__results[0]
            if self.__toDo == "eliminar":
                print("¿Desea eliminar "+self.__foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb
                self.__Answer(["0","1"])
                if self.__answer == "0":
                    return
                elif self.__answer == "1":
<<<<<<< HEAD
                    files.DeletePlaylist(_format,foundPlaylist)
                    print("Se ha eliminado " + foundPlaylist +".")
=======
                    files.DeletePlaylist(_format,foundPlaylist) # funcion que elimine playlist
                    print("Se ha eliminado " + self.__foundPlaylist +".")
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb
                    return
            elif self.__toDo == "buscar":
                self.__playlist = PlaylistMenuFile(self.__format,self.__foundPlaylist) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.PlaylistMenu() #llama al método PlaylistMenu de ese objeto
                return
        else:
            print("Listas encontradas:\n")
<<<<<<< HEAD
            for foundPlaylistIndex in range(len(results)):
                print(str(foundPlaylistIndex+1)+"\t|\t"+results[foundPlaylistIndex])
            foundPlaylist = results[SelectListElement(len(results))]
            if toDo == "eliminar":
                print("¿Desea eliminar "+foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
=======
            for foundPlaylistIndex in range(len(self.__results)):
                print(str(foundPlaylistIndex+1)+"\t|\t"+self.__results[foundPlaylistIndex])
            self.__foundPlaylist = self.__results[self.__SelectListElement(len(self.__results))]
            if self.__toDo == "eliminar":
                print("¿Desea eliminar "+self.__foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb
                self.__Answer(["0","1"])
                if self.__answer == "0":
                    return
                elif self.__answer == "1":
<<<<<<< HEAD
                    files.DeletePlaylist(_format,foundPlaylist)
                    print("Se ha eliminado " + foundPlaylist +".")
=======
                    files.DeletePlaylist(_format,foundPlaylist) #funcion que elimine playlist
                    print("Se ha eliminado " + self.__foundPlaylist +".")
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb
                    return
                elif self.__toDo == "buscar":
                self.__playlist = PlaylistMenuFile(self.__format,self.__foundPlaylist) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.PlaylistMenu() #llama al método PlaylistMenu de ese objeto
                return

    def __NewPlaylistMenu(self): #ya esta pasada a objetos. Solo faltan algunas funciones de juan
        print("\n===================0===================\n")
        print("\tCREAR LISTA DE REPRODUCCIÓN\n")
        self.__playlistName = input("Nombre de la lista de reproducción: ")
        files.MakePlaylist(_format,playlistName) #función que cree una playlist por archivo
        print("La lista de reproducción ha sido creada.\n\n¿Desea añadir elementos a la lista?\n1. Aceptar.\n0. Cancelar.\n")
        self.__Answer(["0","1"])
        if self.__answer == "0":
            return
        else:
            self.__adding = True
            while self.__adding == True:
                self.__playlist = PlaylistMenuFile(self.__format,self.playlistName) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.AddPlaylistElement()
                print("¿Desea añadir otro elemento a la lista?\n1. Aceptar.\n0. Cancelar.\n")
<<<<<<< HEAD
                self._Answer(["0","1"])
                if self.__answer == "0":
                    adding = False
=======
                self.__Answer(["0","1"])
                if self.__answer == "0":
                    self.__adding = False
>>>>>>> 49c6e30da3f0010e1fbbfaefa93eac70c355c8fb
