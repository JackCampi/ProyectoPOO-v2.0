from module_files.Files import Playlist, PlaylistList, MainList
import os
from module_files import Format

class MenuManagement:

    def __init__(self):
        pass

    def Answer(self,options):
        self.__validAnswer = False
        self.answer = "x"
        while self.__validAnswer == False:
            self.answer = input("Seleccione el número de la opción: ")
            if self.answer in options:
                self.__validAnswer = True
            else:
                print("Respuesta inválida, por favor intente de nuevo.")
        return #listo

    def MenuFormat(self, onlyFormat = True):
        if self.format == "music":
            if onlyFormat != True:
                return " música"
            return "música"
        elif self.format == "pictures":
            if onlyFormat != True:
                return "s fotos"
            return "fotos"
        else:
            if onlyFormat != True:
                return "s videos"
            return "videos" #listo

    def AddElementMenu(self):
        print("\n===================0===================\n")
        print("\tAÑADIR A MI"+ self.MenuFormat(False).upper() +"\n")
        self.newElement = self.TakeElementInfo()
        self.mainList = MainList(self.format)
        self.mainList.AddEntry(self.newElement)
        print("\nEl elemento se ha añadido a \"mi{0}\".".format(self.MenuFormat(False)))

    def TakeElementInfo(self):
        name = input("Nombre: ")
        author = input("Autor: ")
        album = input("Álbum: ")
        year = input("Año: ")
        type = input("Género: ")
        path = input("Archivo: ")
        if self.format == "music":
            Element = Format.Music(name, author, album, year, type, path)
        elif self.format == "pictures":
            Element = Format.Pictures(name, author, album, year, type, path)
        else:
            Element = Format.Videos(name, author, album, year, type, path)
        return Element #construye un objeto de tipo format

    def SortListMenu(self, objectList, listName):
        self.listName = listName
        self.objectList = objectList #objeto de la clase Lists
        print("\n===================0===================\n")
        print("\tVER "+ self.listName.upper() +"\n")
        print(self.SortListMenuOptions())
        self.Answer(["0","1","2","3","4","5"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            self.sortedList = self.objectList.SortList("name")
            if len(self.sortedList) == 0:
                self.EmptyListMenu()
            else:
                self.PrintList(self.sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.answer == "2":
            self.sortedList = self.objectList.SortList("author")
            if len(self.sortedList) == 0:
                self.EmptyListMenu()
            else:
                self.PrintList(self.sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.answer == "3":
            self.sortedList = self.objectList.SortList("album")
            if len(self.sortedList) == 0:
                self.EmptyListMenu()
            else:
                self.PrintList(self.sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.answer == "4":
            self.sortedList = self.objectList.SortList("year")
            if len(self.sortedList) == 0:
                self.EmptyListMenu()
            else:
                self.PrintList(self.sortedList)
                wait = input("Pulse Enter para continuar...")
        elif self.answer == "5":
            self.sortedList = self.objectList.SortList("type")
            if len(self.sortedList) == 0:
                self.EmptyListMenu()
            else:
                self.PrintList(self.sortedList)
                wait = input("Pulse Enter para continuar...")
        self.SortListMenu(self.objectList, self.listName)

    def SortListMenuOptions(self):
        if self.format == "music":
            return "1. Por nombre.\n2. Por artista.\n3. Por álbum.\n4. Por año.\n5. Por género.\n\n0. Atrás.\n"
        else:
            return "1. Por nombre.\n2. Por protagonista.\n3. Por álbum.\n4. Por año.\n5. Por tipo.\n\n0. Atrás.\n"

    def EmptyListMenu(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("No hay elementos en "+ self.listName +".")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        wait = input("Pulse Enter para continuar...")
        return

    def NotFoundMenu(self, listName):
        self.listName = listName
        print("No se encontró ningún elemento en " + self.listName +".\n")
        print("1. Volver a buscar.\n0. Atrás.\n")
        self.Answer(["0","1"])
        return

    def PrintList(self, _list):
        self._list = _list
        self.PrintListHead()
        for dicIndex in range(len(self._list)):
            self.PrintListElement(self._list , dicIndex)

    def PrintListElement(self, _list,dicIndex = 0):
        self._list = _list
        self.index = dicIndex
        self.toPrint = "{0}.\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\t|\t{5}\n"
        self._item = self._list[self.index] #cada item es un objeto de tipo Format
        print(self.toPrint.format(self.index+1,self._item.getName(),self._item.getAuthor(),self._item.getAlbum(),self._item.getYear(),self._item.getType()))
        return

    def PrintListHead(self):
        if self.format == "music":
            print("No.\t|\tNombre\t|\tArtista\t|\tÁlbum\t|\tAño\t|\tGénero\n")
        else:
            print("No.\t|\tNombre\t|\tProtagonista\t|\tÁlbum\t|\tAño\t|\tTipo\n")
        return

    def SelectListElement(self, listLength):
        self.listLength = listLength
        print("\n¿Cuál desea seleccionar? ")
        self.Answer([str(x) for x in range(1,self.listLength+1)])
        return int(self.answer) - 1





class PrincipalMenu (MenuManagement):

    def MainMenu(self):
        print("\n===================0===================\n")
        print("\tMENÚ PRINCIPAL\n\n1. Música.\n2. Fotos.\n3. Videos.\n\n0. Salir.\n")
        self.Answer(["0","1","2","3"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            self.format = "music"
            self.__SecondMenu()
        elif self.answer == "2":
            self.format = "pictures"
            self.__SecondMenu()
        elif self.answer == "3":
            self.format = "videos"
            self.__SecondMenu()
        self.MainMenu() #listo

    def __SecondMenu(self):
        print("\n===================0===================\n")
        print("\t"+ self.MenuFormat().upper()+"\n")
        print("1. Mi"+ self.MenuFormat(False) +".\n2. Listas de reproducción.\n\n0. Atrás.\n")
        self.Answer(["0","1","2"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            self.__ThirdMenu()
        elif self.answer == "2":
            self.__FourthMenu()
        self.__SecondMenu() #listo

    def __ThirdMenu(self):
        print("\n===================0===================\n")
        print("\tMI"+ self.MenuFormat(False).upper()+"\n")
        print("1. Ver mi"+ self.MenuFormat(False) +".\n2. Buscar.\n3. Añadir.\n\n0. Atrás.\n")
        self.Answer(["0","1","2","3"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            _MainList = MainList(self.format)
            self.SortListMenu(_MainList , "Mi"+self.MenuFormat(False)) #MENU DE ORDENAR LISTA
        elif self.answer == "2":
            self.__SearchMenu()
        elif self.answer == "3":
            self.AddElementMenu()
        self.__ThirdMenu()

    def __SearchMenu(self):
        print("\n===================0===================\n")
        print("\tBUSCAR EN MI" + self.MenuFormat(False).upper()+ "\n")
        toSearch = input("¿Qué desea buscar? ")
        _MainList = MainList(self.format)
        searchResults = _MainList.Search(toSearch)
        if len(searchResults) == 0 :
            self.NotFoundMenu( "mi" + self.MenuFormat(False))
            if self.answer == "0":
                return
            else:
                self.__SearchMenu()
                return
        elif len(searchResults) == 1:
            self.__searchElement = searchResults[0]
            self.__FoundElementMenu(self.__searchElement)
            return
        else:
            self.PrintList(searchResults)
            self.__searchElement = searchResults[self.SelectListElement(len(searchResults))]
            self.__FoundElementMenu(self.__searchElement)
            return

    def __FoundElementMenu(self, foundElement):
        self.__foundElement = foundElement
        print("\n===================0===================\n")
        self.PrintListHead()
        print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(self.__foundElement.getName(),self.__foundElement.getAuthor(),self.__foundElement.getAlbum(),self.__foundElement.getYear(),self.__foundElement.getType()))
        print("¿Qué desea hacer con este elemento?\n1. Añadir a lista de reproducción.\n2. Eliminar.\n3. Modificar información.\n\n0. Atrás.")
        self.Answer(["0","1","2","3"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            self.__AddToPlaylistMenu(foundElement)
            return
        elif self.answer == "2":
            _MainList = MainList(self.format)
            _MainList.DeleteEntry(foundElement)
            print("Se ha eliminado el elemento. Volviendo a \"MI" + self.MenuFormat(False).upper()+"\".")
            return
        elif self.answer == "3":
            self.__ModifyElementMenu(foundElement)
            return

    def __AddToPlaylistMenu(self, toAddElement): #toAddElement es el objeto de tipo format
        self.__playlists = PlaylistList(self.format) #objeto tipo PlaylistList
        self.__playlistList = self.__playlists.GetPlaylists()
        self.__toAddElement = toAddElement
        if len(self.__playlistList) == 0:
            print("No se encontraron listas de reproducción en "+ self.MenuFormat()+".")
            return
        else:
            for playlistIndex in range(len(self.__playlistList)):
                print(str(playlistIndex+1)+"\t|\t"+ self.__playlistList[playlistIndex] )
            self.playlistName = self.__playlistList[self.SelectListElement(len(self.__playlistList))]
            self.__playlistObject = Playlist(self.format, self.playlistName) #objeto de tipo Playlist
            self.__playlistObject.AddEntry(self.__toAddElement) #mirar ques es param Entry
            print("Se añadió \""+self.__toAddElement.getName()+ "\" a " + self.playlistName + ".")
            return

    def __ModifyElementMenu(self, oldElementObject):
        print("\nIngrese la nueva información del elemento.")
        newElementObject = self.TakeElementInfo()
        _MainList = MainList(self.format)
        _MainList.ModifyList(newElementObject,oldElementObject)
        print("Se ha modificado la información del elemento. Volviendo a \"MI" + self.MenuFormat(False).upper()+"\".")

    def __FourthMenu(self):
        print("\n===================0===================\n")
        print("\tLISTAS DE REPRODUCCIÓN DE " + self.MenuFormat().upper() + "\n")
        print("1. Mis listas.\n2. Crear lista.\n3. Buscar lista.\n4. Eliminar lista.\n\n0. Atrás.\n")
        self.Answer(["0","1","2","3","4"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            self.__playlists = PlaylistList(self.format) #objeto tipo PlaylistList
            self.__playlistList = self.__playlists.GetPlaylists()
            if len(self.__playlistList) == 0:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                print("No hay listas de reproducción en " + self.MenuFormat() + ".")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                wait = input("Pulse Enter para continuar...")
            else:
                for playlistIndex in range(len(self.__playlistList)):
                    print(str(playlistIndex+1)+"\t|\t"+self.__playlistList[playlistIndex] + ".\n")
                print("\n1. Seleccionar una lista de reproducción.\n0. Atrás.\n")
                self.Answer(["0","1"])
                if self.answer == "1":
                    self.playlistName = self.__playlistList[self.SelectListElement(len(self.__playlistList))]
                    FifthMenu = PlaylistMenu(self.format, self.playlistName) #crea el objeto de meú de playlist
                    FifthMenu.PlaylistMenu()
        elif self.answer == "2":
            self.__NewPlaylistMenu() #falta pasar --> ya esta // corregir llamadas a esta función
        elif self.answer == "3":
            self.__SearchPlaylistMenu() #falta pasar --> ya esta // corregir llamadas a esta función
        elif self.answer == "4":
            self.__SearchPlaylistMenu("eliminar") #faltapasar --> ya esta // corregir llamadas a esta función
        self.__FourthMenu()

    def __SearchPlaylistMenu(self, toDo = "buscar"): #ya esta pasada a objetos //si quieres mirar instanciacion de objetos
        self.__toDo = toDo
        print("\n===================0===================\n")
        self.__toSearch = input("¿Qué lista de reproducción desea "+ self.__toDo +"? ")
        self.__playlists = PlaylistList(self.format) #objeto tipo PlaylistList
        self.__results = self.__playlists.SearchPlaylist(self.__toSearch)
        if len(self.__results) == 0:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("No se encontró ninguna lista de reproducción en " + self.MenuFormat() +".\n")
            print("1. Volver a buscar.\n0. Atrás.\n")
            self.Answer(["0","1"])
            if self.answer == "0":
                return
            elif self.answer == "1":
                self.__SearchPlaylistMenu(self.__toDo )
        elif len(self.__results) == 1:
            self.__foundPlaylist = self.__results[0]
            if self.__toDo == "eliminar":
                print("¿Desea eliminar "+self.__foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
                self.Answer(["0","1"])
                if self.answer == "0":
                    return
                elif self.answer == "1":
                    toDeletePlaylist = Playlist(self.format, self.__foundPlaylist)
                    toDeletePlaylist.DeletePlaylist() # funcion que elimine playlist
                    print("Se ha eliminado " + self.__foundPlaylist +".")
                    return
            elif self.__toDo == "buscar":
                self.__playlist = PlaylistMenu(self.format,self.__foundPlaylist) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.PlaylistMenu() #llama al método PlaylistMenu de ese objeto
                return
        else:
            print("Listas encontradas:\n")
            for foundPlaylistIndex in range(len(self.__results)):
                print(str(foundPlaylistIndex+1)+"\t|\t"+self.__results[foundPlaylistIndex])
            self.__foundPlaylist = self.__results[self.SelectListElement(len(self.__results))]
            if self.__toDo == "eliminar":
                print("¿Desea eliminar "+self.__foundPlaylist+"?\n1. Aceptar.\n0. Cancelar.")
                self.Answer(["0","1"])
                if self.answer == "0":
                    return
                elif self.answer == "1":
                    toDeletePlaylist = Playlist(self.format, self.__foundPlaylist)
                    toDeletePlaylist.DeletePlaylist() # funcion que elimine playlist
                    print("Se ha eliminado " + self.__foundPlaylist +".")
            elif self.__toDo == "buscar":
                self.__playlist = PlaylistMenu(self.format,self.__foundPlaylist) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.PlaylistMenu() #llama al método PlaylistMenu de ese objeto
                return

    def __NewPlaylistMenu(self): #ya esta pasada a objetos. Solo faltan algunas funciones de juan
        print("\n===================0===================\n")
        print("\tCREAR LISTA DE REPRODUCCIÓN\n")
        self.playlistName = input("Nombre de la lista de reproducción: ")
        playlist = Playlist(self.format,self.playlistName)
        print("La lista de reproducción ha sido creada.\n\n¿Desea añadir elementos a la lista?\n1. Aceptar.\n0. Cancelar.\n")
        self.Answer(["0","1"])
        if self.answer == "0":
            return
        else:
            self.__adding = True
            while self.__adding == True:
                self.__playlist = PlaylistMenu(self.format,self.playlistName) #instancia un objeto tipo PlaylistMenuFile
                self.__playlist.AddPlaylistElement()
                print("¿Desea añadir otro elemento a la lista?\n1. Aceptar.\n0. Cancelar.\n")
                self.Answer(["0","1"])
                if self.answer == "0":
                    self.__adding = False

class PlaylistMenu(MenuManagement):

    def __init__(self,_format, playlistName):
        self.format = _format
        self.playlistName = playlistName
        self.__playlist = Playlist(self.format, self.playlistName)

    def PlaylistMenu(self):
        print("\n===================0===================\n")
        print("\t" + self.playlistName.upper() + "\n")
        print("1. Ver contenido de la lista.\n2. Añadir un elemento.\n3. Eliminar un elemento.\n4. Eliminar lista.\n\n0. Atrás.\n")
        self.Answer(["0", "1", "2", "3", "4"])
        if self.answer == "0":
            return
        elif self.answer == "1":
            self.__PrintPlaylist()
            wait = input("Pulse Enter para continuar...")
            self.PlaylistMenu()
            return
        elif self.answer == "2":
            self.AddPlaylistElement()
            self.PlaylistMenu()
            return
        elif self.answer == "3":
            self.__DeletePlaylistElement()
            self.PlaylistMenu()
            return
        elif self.answer == "4":
            self.__playlist.DeletePlaylist()
            print("La lista fue eliminada.")
            return

    def AddPlaylistElement(self):
        self.__element = input("¿Qué elemento desea agregar a la lista? ")
        self.mainList = MainList(self.format)
        self.__results = self.mainList.Search(self.__element)
        if len(self.__results) == 0:
            self.NotFoundMenu("mi" + self.MenuFormat(False))
            if self.answer == "0":
                return
            else:
                self.AddPlaylistElement()
        elif len(self.__results) == 1:
            self.__finalElement = self.__results[0]
            self.PrintListHead()
            self.PrintListElement(self.__results)
            print("¿Desea añadir este elemento a " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("\nNo se añadió el elemento.\n")
                return
            else:
                self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                print("\nSe añadió \""+ self.__finalElement.getName() + "\" a " + self.playlistName + ". Volviendo al menú de la lista de reproducción.\n")
        else:
            self.PrintList(self.__results)
            self.index = self.SelectListElement(len(self.__results))
            self.__finalElement = self.__results[self.index]
            self.PrintListHead()
            self.PrintListElement(self.__results,self.index)
            print("¿Desea añadir este elemento a " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("\nNo se añadió el elemento.\n")
                return
            else:
                self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                print("\nSe añadió \""+ self.__finalElement.getName() + "\" a " + self.playlistName + ". Volviendo al menú de la lista de reproducción.\n")


    def __PrintPlaylist(self):
        self.SortListMenu(self.__playlist, self.playlistName)
        return

    def __DeletePlaylistElement(self):
        self.__element = input("¿Qué elemento desea eliminar? ")
        self.__results = self.__playlist.Search(self.__element)
        if len(self.__results) == 0:
            self.NotFoundMenu(self.playlistName)
            if self.answer == "0":
                return
            else:
                self.__DeletePlaylistElement()
        elif len(self.__results) == 1:
            self.__finalElement = self.__results[0]
            self.PrintListHead()
            self.PrintListElement(self.__results)
            print("¿Desea eliminar este elemento de " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("El elemento no se eliminó.\n")
                return
            else:
                self.__playlist.DeleteEntry(self.__finalElement)#mirar que es param Entry
                print("Se eliminó el elemento de " + self.playlistName + ". Volviendo al menú de la lista de reproducción.")
        else:
            self.PrintListHead()
            self.PrintList(self.__results)
            self.index = self.SelectListElement(len(self.__results))
            self.__finalElement = self.__results[self.index]
            self.PrintListHead()
            self.PrintListElement(self.results,self.index)
            print("¿Desea eliminar este elemento de " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("El elemento no se eliminó.\n")
                return
            else:
                self.__playlist.DeleteEntry(self.__finalElement)#mirar que es param Entry
                print("Se eliminó el elemento de " + self.playlistName + ". Volviendo al menú de la lista de reproducción.")
