import Playlist from Files
import MainList from Files
import os
import Format

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
        self.__mainList.AddEntry(self.__newElement)
        print("\nEl elemento se ha añadido a \"mi{0}\".".format(self.__MenuFormat(False)))

    def __TakeElementInfo(self):
        name = input("Nombre: ")
        author = input("Autor: ")
        album = input("Álbum: ")
        year = input("Año: ")
        type = input("Género: ")
        path = input("Archivo: ")
        if self.__format == "music":
            Element = Format.Music(name, author, album, year, type, path)
        elif self.__format == "pictures":
            Element = Format.Pictures(name, author, album, year, type, path)
        else:
            Element = Format.Videos(name, author, album, year, type, path)
        return Element #construye un objeto de tipo format

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
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "2":
            self.__sortedList = self.__objectList.SortList("author")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "3":
            self.__sortedList = self.__objectList.SortList("album")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "4":
            self.__sortedList = self.__objectList.SortList("year")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.__answer == "5":
            self.__sortedList = self.__objectList.SortList("type")
            if len(self.__sortedList) == 0:
                self.__emptyListMenu()
            else:
                self.__PrintList(self.__sortedList)
                wait = input("Pulse Enter para continuar...")
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
        return

    def __PrintList(self, _list):
        self.__list = _list
        self.__PrintListHead()
        for dicIndex in range(len(self.__list)):
            self.__PrintListElement(self.__list , dicIndex)

    def __PrintListElement(self, _list,dicIndex = 0):
        self.__list = _list
        self.__index = dicIndex
        self.__toPrint = "{0}.\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\t|\t{5}\n"
        self.__item = self.__list[self.__index] #cada item es un objeto de tipo Format
        print(self.__toPrint.format(self.__index+1,self.__item.getName(),self.__item.getAuthor(),self.__item.getAlbum(),self.__item.getYear(),self.__item.getType()))
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
        self.__Answer([str(x) for x in range(1,self.__listLength+1)])
        return int(self.__answer) - 1





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
        self.MainMenu() #listo

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
        self.__SecondMenu() #listo

    def __ThirdMenu(self):
        print("\n===================0===================\n")
        print("\tMI"+ self.__MenuFormat(False).upper()+"\n")
        print("1. Ver mi"+ self.__MenuFormat(False) +".\n2. Buscar.\n3. Añadir.\n\n0. Atrás.\n")
        self.__Answer(["0","1","2","3"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            MainList = MainList(self.__format)
            self.__SortListMenu(MainList , "Mi"+self.__MenuFormat(False)) #MENU DE ORDENAR LISTA
        elif self.__answer == "2":
            self.__SearchMenu()
        elif self.__answer == "3":
            self.__AddElementMenu()
        self.__ThirdMenu()

    def __SearchMenu(self):
        print("\n===================0===================\n")
    	print("\tBUSCAR EN MI" + self.__MenuFormat(False).upper()+ "\n")
    	toSearch = input("¿Qué desea buscar? ")
        MainList = MainList(self.__format)
    	searchResults = MainList.Search(toSearch)
    	if len(searchResults) == 0 :
    		self.__NotFoundMenu( "mi" + self.__MenuFormat(False))
    		if self.__answer == "0":
    			return
    		else:
    			self.__SearchMenu()
    			return
    	elif len(searchResults) == 1:
    		self.__searchElement = searchResults[0]
    		self.__FoundElementMenu(self.__searchElement)
    		return
    	else:
    		self.__PrintList(searchResults)
    		self.__searchElement = searchResults[self.__SelectListElement(len(searchResults))]
    		self.__FoundElementMenu(self.__searchElement)
    		return

    def __FoundElementMenu(self, foundElement):
        self.__foundElement = foundElement
        print("\n===================0===================\n")
        self.__PrintListHead()
        print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(self.__foundElement.getName(),self.__foundElement.getAuthor(),self.__foundElement.getAlbum(),self.__foundElement.getYear(),self.__foundElement.getType()))
        print("¿Qué desea hacer con este elemento?\n1. Añadir a lista de reproducción.\n2. Eliminar.\n3. Modificar información.\n\n0. Atrás.")
        self.__Answer(["0","1","2","3"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            self.__AddToPlaylistMenu(foundElement)
            return
        elif self.__answer == "2":
            MainList = MainList(self.__format)
            MainList.DeleteEntry(foundElement)
            print("Se ha eliminado el elemento. Volviendo a \"MI" + self.__MenuFormat(False).upper()+"\".")
            return
        elif self.__answer == "3":
            self.__ModifyElementMenu(foundElement)
            return

    def __AddToPlaylistMenu(self, toAddElement): #toAddElement es el objeto de tipo format
        self.__playlists = PlaylistList(self.__format) #objeto tipo PlaylistList
        self.__playlistList = self.__playlists.GetPlaylists()
        self.__toAddElement = toAddElement
        if len(self.__playlistList) == 0:
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

    def __ModifyElementMenu(self, oldElementObject):
        print("\nIngrese la nueva información del elemento.")
        newElementObject = self.__TakeElementInfo()
        MainList = MainList(self.__format)
        MainList.ModifyList(newElementObject,oldElementObject)
        print("Se ha modificado la información del elemento. Volviendo a \"MI" + self.__MenuFormat(False).upper()+"\".")

    def __FourthMenu(self):
        print("\n===================0===================\n")
        print("\tLISTAS DE REPRODUCCIÓN DE " + self.__MenuFormat().upper() + "\n")
        print("1. Mis listas.\n2. Crear lista.\n3. Buscar lista.\n4. Eliminar lista.\n\n0. Atrás.\n")
        self.__Answer(["0","1","2","3","4"])
        if self.__answer == "0":
            return
        elif self.__answer == "1":
            self.__playlists = PlaylistList(self.__format) #objeto tipo PlaylistList
            self.__playlistList = self.__playlists.GetPlaylists()
            if len(self.__playlistList) == 0:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                print("No hay listas de reproducción en " + self.__MenuFormat() + ".")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                wait = input("Pulse Enter para continuar...")
            else:
                for playlistIndex in range(len(self.__playlistList)):
                    print(str(playlistIndex+1)+"\t|\t"+self.__playlistList[playlistIndex] + ".\n")
                    print("\n1. Seleccionar una lista de reproducción.\n0. Atrás.\n")
                    self.__Answer(["0","1"])
                    if self.__answer == "1":
                        self.__playlistName = self.__playlistList[self.__SelectListElement(len(self.__playlistList))]
                        FifthMenu = PlaylistMenu(self.__format, self.__playlistName) #crea el objeto de meú de playlist
                        FifthMenu.PlaylistMenu()
        elif self.__answer == "2":
            self.__NewPlaylistMenu() #falta pasar --> ya esta // corregir llamadas a esta función
        elif self.__answer == "3":
            SearchPlaylistMenu(_format) #falta pasar --> ya esta // corregir llamadas a esta función
        elif self.__answer == "4":
            SearchPlaylistMenu(_format,"eliminar") #faltapasar --> ya esta // corregir llamadas a esta función
        self.__FourthMenu()

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
                self.__SearchPlaylistMenu(self.__toDo )
        elif len(self.__results) == 1:
            self.__foundPlaylist = self.__results[0]
            if self.__toDo == "eliminar":
                print("¿Desea eliminar "+self.__foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
                self.__Answer(["0","1"])
                if self.__answer == "0":
                    return
                elif self.__answer == "1":
                    files.DeletePlaylist(_format,foundPlaylist) # funcion que elimine playlist
                    print("Se ha eliminado " + self.__foundPlaylist +".")
                    return
            elif self.__toDo == "buscar":
                self.__playlist = PlaylistMenuFile(self.__format,self.__foundPlaylist) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.PlaylistMenu() #llama al método PlaylistMenu de ese objeto
                return
        else:
            print("Listas encontradas:\n")
            for foundPlaylistIndex in range(len(self.__results)):
                print(str(foundPlaylistIndex+1)+"\t|\t"+self.__results[foundPlaylistIndex])
            self.__foundPlaylist = self.__results[self.__SelectListElement(len(self.__results))]
            if self.__toDo == "eliminar":
                print("¿Desea eliminar "+self.__foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
                self.__Answer(["0","1"])
                if self.__answer == "0":
                    return
                elif self.__answer == "1":
                    files.DeletePlaylist(_format,foundPlaylist) #funcion que elimine playlist
                    print("Se ha eliminado " + self.__foundPlaylist +".")
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
                self.__Answer(["0","1"])
                if self.__answer == "0":
                    self.__adding = False

class PlaylistMenu(MenuManagement):

    def __init__(self,_format, playlistName):
        self.__format = _format
        self.__playListName = playlistName
        self.__playlist = Playlist(self.__format, self.__playListName)

    def PlaylistMenu(self):
        print("\n===================0===================\n")
    	print("\t" + self.__playlistName.upper() + "\n")
    	print("1. Ver contenido de la lista.\n2. Añadir un elemento.\n3. Eliminar un elemento.\n4. Eliminar lista.\n\n0. Atrás.\n")
    	self.__Answer(["0", "1", "2", "3", "4"])
        if answer == "0":
    		return
    	elif self.__answer == "1":
    		self.__PrintPlaylist()
    		wait = input("Pulse Enter para continuar...")
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "2":
    		self.AddPlaylistElement()
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "3":
    		self.__DeletePlaylistElement()
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "4":
            self.__playlist.DeletePlaylist()
    		print("La lista fue eliminada.")
    		return

    def AddPlaylistElement(self):
        self.__element = input("¿Qué elemento desea agregar a la lista? ")
        self.__mainList = MainList(self.__format)
        self.__results = self.__mainList.Search(self.__element)
        if len(self.__results) == 0:
    		self.__option = self.__NotFoundMenu("mi" + self.__MenuFormat(False))
    		if self.__option == "0":
    			return
    		else:
    			self.AddPlaylistElement()
        elif len(self.__results) == 1:
            self.__finalElement = self.__results[0]
            self.__PrintListHead()
            self.__PrintListElement(self.__results)
            print("¿Desea añadir este elemento a " + self.__playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.__Answer(["0", "1"])
            if self.__answer == 0:
                print("No se añadió el elemento.\n")
                return
            else:
                self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                print("Se añadió \""+ self.__finalElement.getName() + "\" a " + self.__playlistName + ". Volviendo al menú de la lista de reproducción.")
        else:
            self.__PrintListHead()
            self.__PrintList(self.__results)
            self.__index = self.__SelectListElement(len(self.__results))
            self.__finalElement = self.__results[self.__index]
            self.__PrintListHead()
            self.__PrintListElement(self.__results,self.__index)
            print("¿Desea añadir este elemento a " + self.__playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.__Answer(["0", "1"])
            if self.__answer == 0:
                print("No se añadió el elemento.\n")
                return
            else:
    			self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
    			print("Se añadió \""+ self.__finalElement.getName() + "\" a " + self.__playlistName + ". Volviendo al menú de la lista de reproducción.")


    def __PrintPlaylist(self):
        self.__SortListMenu(self.__playlist, self.__playListName)
 	   return

    def __DeletePlaylistElement(self):
    	self.__element = input("¿Qué elemento desea eliminar? ")
    	self.__results = self.__playlist.Search(self.__element)
        if len(self.__results) == 0:
    		self.__option = self.__NotFoundMenu(self.__playlistName)
    		if self.__option == "0":
    			return
    		else:
    			self.__DeletePlaylistElement()
        elif len(self.__results) == 1:
            self.__finalElement = self.__results[0]
            self.__PrintListHead()
            self.__PrintListElement(self.__results)
    		print("¿Desea eliminar este elemento de " + self.__playlistName + "?\n1. Confirmar.\n0. Cancelar.")
    		self.__Answer(["0", "1"])
    		if self.__answer == 0:
    			print("El elemento no se eliminó.\n")
    			return
    		else:
                self.__playlist.DeleteEntry(self.__finalElement)#mirar que es param Entry
    			print("Se eliminó el elemento de " + self.__playlistName + ". Volviendo al menú de la lista de reproducción.")
        else:
    		self.__PrintListHead
            self.__PrintList(self.__results)
            self.__index = self.__SelectListElement(len(self.__results))
    		self.__finalElement = self.__results[self.__index]
    		self.__PrintListHead()
            self.__PrintListElement(self.results,self.__index)
    		print("¿Desea eliminar este elemento de " + self.__playlistName + "?\n1. Confirmar.\n0. Cancelar.")
    		self.__Answer(["0", "1"])
    		if self.__answer == 0:
    			print("El elemento no se eliminó.\n")
    			return
    		else:
    			self.__playlist.DeleteEntry(self.__finalElement)#mirar que es param Entry
    			print("Se eliminó el elemento de " + self.__playlistName + ". Volviendo al menú de la lista de reproducción.")
