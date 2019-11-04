
import MenuManagement from MenuFile
import Playlist from Files
import MainList from Files
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
    		self.PrintPlaylist(self.__format, self.__playlistName) #cambiar el llamado cuando este lista
    		wait = input("Pulse Enter para continuar...")
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "2":
    		self.__AddPlaylistElement()
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "3":
    		self.DeletePlaylistElement(self.__format, self.__playlistName)
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "4":
            self.__playlist.DeletePlaylist()
    		print("La lista fue eliminada.")
    		return
	"""Esta función corresponde al menú específico de las listas de reproducción,
	desde aquí el usuario tiene más opciones que puede ejecutar sobre estas.
	- Como argumento recibe el formato dobre el que se está trabajando y el
	nombre de la lista de reproducción.
	- La primera opción permite ver el contenido ordenado de la lista.
	- La segunda opción permite añadir un elemento a la lista.
	- La tercera opción busca un elemento dentro de la lista para eliminarlo.
	- La cuarta opción elimina la lista de reproducción y retorna al cuarto menú."""


    def __AddPlaylistElement(self):
        self.__element = input("¿Qué elemento desea agregar a la lista? ")
        self.__mainList = MainList(self.__format)
        self.__results = self.__mainList.Search(self.__element)
        if len(self.__results) == 0:
    		option = NotFoundMenu(_format, "mi" + self.__MenuFormat(False))#esperar a cambiar NotFoundMenu
    		if option == "0":
    			return
    		else:
    			self.__AddPlaylistElement()
        elif len(self.__results) == 1:
    		self.__finalElement = self.__results[0]
    		PrintListHead(_format)#mirar como funciona esta funcion/esperar a que la cambien
            #mirar como se llaman las propiedades de los objetos, se puede cambiar por un PrintListElement
    		print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(finalElement["name"],finalElement["author"],finalElement["album"],finalElement["year"],finalElement["type"]))
    		print("¿Desea añadir este elemento a " + self.__playlistName + "?\n1. Confirmar.\n0. Cancelar.")
    		self.__Answer(["0", "1"])
    		if self.__answer == 0:
    			print("No se añadió el elemento.\n")
    			return
    		else:
                self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                #cambiar .name por getter
    			print("Se añadió \""+ self.__finalElement.name + "\" a " + self.__playlistName + ". Volviendo al menú de la lista de reproducción.")
        else:
            #añadir in PrintListHead
            #añardir un PrintList con los resultados
    		self.__finalElement = results[SelectListElement(len(results))]#cuando cambien SelectListElement
    		PrintListHead(_format)#cuando cambien PrintListHead
            #mirar como se llaman las propiedades de los objetos, se puede cambiar por un PrintListElement
    		print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(finalElement["name"],finalElement["author"],finalElement["album"],finalElement["year"],finalElement["type"]))
    		print("¿Desea añadir este elemento a " + self.__playlistName + "?\n1. Confirmar.\n0. Cancelar.")
    		self.__Answer(["0", "1"])
    		if self.__answer == 0:
    			print("No se añadió el elemento.\n")
    			return
    		else:
    			self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                #cambiar .name por getter
    			print("Se añadió \""+ self.__finalElement.name + "\" a " + self.__playlistName + ". Volviendo al menú de la lista de reproducción.")


	"""Esta función se encarga de buscar un elemento del formato que se está
	trabajando y añadirlo a la lista de reproducción. Antes de añadirlo le
	pide al usuario confirmar que desea añadir el elemento.
	- Como argumentos recibe el formato sobre el que se está trabajando y el
	nombre de la lista de reproducción a la cual se le va a añadir el elemento.
	- Al terminar, vuelve al menú específico de la lista."""
    def PrintPlaylist(self, _format, playlistName): #toca modificar completamente esta funcion/ mirar SortListMenu

	       """Esta función construye la ruta de la lista de reproducción para pasarla
	como argumento en el menú de listas ordenadas, donde el usuario puede escoger
	el orden por el cual desea visualizar el contenido de la lista.
	-Como argumento recibe el formato sobre el que se está trabajando y el nombre
	de la lista.
	- Al terminar vuelve al menú específico de la lista."""

	   playlistPath = "playlists" + os.sep + playlistName + ".txt"
	   SortListMenu(_format, playlistName, playlistPath)
	   return

    def DeletePlaylistElement(_format, playlistName):

	"""Esta función se encarga de buscar un elemento en la lista de reproducción
	para eliminarlo.
	- Como argumentos recibe el formato sobre el que se está trabajando y el
	nombre de la lista de reproducción.
	- En el caso de no encontrar el elemento en la lista, le da la opción al
	usuario de volver a buscar o salir.
	- Antes de eliminar un elemento le pide al usuario confirmar la acción.
	- Al terminar, vuelve al menú específico de la lista."""

	playlistPath = "playlists" + os.sep + playlistName + ".txt"
	playlistList = files.ReadFormat(_format, playlistPath)
	element = input("¿Qué elemento desea eliminar? ")
	results = Miscellaneous.SearchItemInList(playlistList, element)
	if len(results) == 0:
		option = NotFoundMenu(_format, playlistName)
		if option == "0":
			return
		else:
			DeletePlaylistElement(_format, playlistName)
	elif len(results) == 1:
		finalElement = results[0]
		PrintListHead(_format)
		print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(finalElement["name"],finalElement["author"],finalElement["album"],finalElement["year"],finalElement["type"]))
		print("¿Desea eliminar este elemento de " + playlistName + "?\n1. Confirmar.\n0. Cancelar.")
		answer = Answer(["0", "1"])
		if answer == 0:
			print("El elemento no se eliminó.\n")
			return
		else:
			files.DeleteEntry(finalElement, _format, playlistPath)
			print("Se eliminó el elemento de " + playlistName + ". Volviendo al menú de la lista de reproducción.")
	else:
		finalElement = results[SelectListElement(len(results))]
		PrintListHead(_format)
		print("1.\t|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\n".format(finalElement["name"],finalElement["author"],finalElement["album"],finalElement["year"],finalElement["type"]))
		print("¿Desea eliminar este elemento de " + playlistName + "?\n1. Confirmar.\n0. Cancelar.")
		answer = Answer(["0", "1"])
		if answer == 0:
			print("El elemento no se eliminó.\n")
			return
		else:
			files.DeleteEntry(finalElement, _format, playlistPath)
			print("Se eliminó el elemento de " + playlistName + ". Volviendo al menú de la lista de reproducción.")
