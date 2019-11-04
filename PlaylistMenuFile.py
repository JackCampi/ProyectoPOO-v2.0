
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
    		self.PrintPlaylist()
    		wait = input("Pulse Enter para continuar...")
    		self.PlaylistMenu()
    		return
    	elif self.__answer == "2":
    		self.__AddPlaylistElement()
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
    		self.__option = self.__NotFoundMenu("mi" + self.__MenuFormat(False))
    		if self.__option == "0":
    			return
    		else:
    			self.__AddPlaylistElement()
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


	"""Esta función se encarga de buscar un elemento del formato que se está
	trabajando y añadirlo a la lista de reproducción. Antes de añadirlo le
	pide al usuario confirmar que desea añadir el elemento.
	- Como argumentos recibe el formato sobre el que se está trabajando y el
	nombre de la lista de reproducción a la cual se le va a añadir el elemento.
	- Al terminar, vuelve al menú específico de la lista."""
    def PrintPlaylist(self):
        self.__SortListMenu(self.__playlist, self.__playListName)
 	   return
	       """Esta función construye la ruta de la lista de reproducción para pasarla
	como argumento en el menú de listas ordenadas, donde el usuario puede escoger
	el orden por el cual desea visualizar el contenido de la lista.
	-Como argumento recibe el formato sobre el que se está trabajando y el nombre
	de la lista.
	- Al terminar vuelve al menú específico de la lista."""

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

	"""Esta función se encarga de buscar un elemento en la lista de reproducción
	para eliminarlo.
	- Como argumentos recibe el formato sobre el que se está trabajando y el
	nombre de la lista de reproducción.
	- En el caso de no encontrar el elemento en la lista, le da la opción al
	usuario de volver a buscar o salir.
	- Antes de eliminar un elemento le pide al usuario confirmar la acción.
	- Al terminar, vuelve al menú específico de la lista."""
    def NewPlaylistMenu(self):
        print("\n===================0===================\n")
    	print("\tCREAR LISTA DE REPRODUCCIÓN\n")

	"""Esta función se encarga de crear una nueva lista de reproducción y de
	agregar elementos a esta.
	- Como parametro recibe el formato sobre el que se está trabajando.
	- Contiene un bucle que termina cuando el usuario deja de añadir elementos
	a la lista.
	- Al terminar, vuelve al cuarto menú."""

	print("\n===================0===================\n")
	print("\tCREAR LISTA DE REPRODUCCIÓN\n")
	playlistName = input("Nombre de la lista de reproducción: ")
	files.MakePlaylist(_format, playlistName)
	print("La lista de reproducción ha sido creada.\n\n¿Desea añadir elementos a la lista?\n1. Aceptar.\n0. Cancelar.\n")
	answer = Answer(["0", "1"])
	if answer == "0":
		return
	else:
		adding = True
		while adding == True:
			AddPlaylistElement(_format, playlistName)
			print("¿Desea añadir otro elemento a la lista?\n1. Aceptar.\n0. Cancelar.\n")
			answer1 = Answer(["0", "1"])
			if answer1 == "0":
				adding = False
