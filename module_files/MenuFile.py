""" En este módulo se encuentran las clases correspondientes a los menús de la
aplicación. Cuenta con tres clases: MenuManagement, que contiene los métodos y
propiedades que son utilizadas en las otras clases; PrincipalMenu, que, como
su nombre lo indica, crea objetos de tipo menú principal donde comienzan las
ramas de los menús que el usuario ve en consola; y por último, PlaylistMenu,
que corresponde a los menús de las listas de reproducción con sus respectivos
métodos y propiedades.

Este módulo requiere de los módulos Files.py y Format.py."""

from module_files.Files import Playlist, PlaylistList, MainList
import os
from module_files import Format

class MenuManagement:
    """Esta clase contiene los métodos y propiedades que comparten las clases de
    menús. Algunos de ellos tienen que ver con esperar la respuesta del usuario,
    imprimir los elementos de una lista, ordenar una lista por alguna característica,
    entre otros."""

    def __init__(self):
        pass

    def Answer(self,options):
        """Este método pide la entrada del usuario y la evalúa de manera que esta
        corresponda a las opciones disponibles en cada menú.
        - Recibe como parámetro la lista de los números de las opciones que el
         usuario tiene disponibles.
        - Si la Respuesta no es válida, el método se encarga de pedir una nueva
        entrada.
        - No retorna ningún valor; le asigna a la propiedad self.answer la Respuesta
        del usuario para que esta sea evaluada luego de que este método se haya
        llamado."""
        self.__validAnswer = False
        self.answer = "x"
        while self.__validAnswer == False:
            self.answer = input("Seleccione el número de la opción: ")
            if self.answer in options:
                self.__validAnswer = True
            else:
                print("Respuesta inválida, por favor intente de nuevo.")
        return

    def MenuFormat(self, onlyFormat = True):
        """
        Esta función devuelve strings que son utilizados en los menús para
        completar los textos de los títulos o las opciones. De manera general,
        devuelve una traducción del formato. El segundo argumento de esta función
        hace que el string que se devuelve tenga los caracteres para completar
        frases como "mi música" o "mis videos" (la letra s y un espacio).
        """
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
            return "videos"

    def AddElementMenu(self):
        """Este método toma los datos de un nuevo elemento para meterlo en la
        lista principal del formato que se esté trabajando. Para ello llama al
        método self.TakeElementInfo, el cual retorna un objeto del formato que
        corresponda.
        - Dentro de la clase se instancia un objeto de tipo MainList para Añadir
        la nueva entrada.
        - La función no retorna ningún valor, pero imprime un mensaje en consola
        que avisa cuando el elemento se haya añadido."""
        print("\n===================0===================\n")
        print("\tAÑADIR A MI"+ self.MenuFormat(False).upper() +"\n")
        self.newElement = self.TakeElementInfo()
        self.mainList = MainList(self.format)
        self.mainList.AddEntry(self.newElement)
        print("\nEl elemento se ha añadido a \"mi{0}\".".format(self.MenuFormat(False)))

    def TakeElementInfo(self):
        """
        Esta función corresponde al menú donde se toman los datos de un elemento
        (nombre, autor, album, etc.) y devuelve un objeto del fotmato trabajado.
        - RETURN: objeto del tipo del formato con todas sus caracteristicas iniciadas.
        """
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
        return Element

    def SortListMenu(self, objectList, listName):
        """Este método corresponde al menú donde se ordenan las listas según la
        característica que el usuario escoja. Una vez ordenada la lista, la imprime
        y se vuelve a llamar a sí misma.
        - Recibe como argumento la lista de objetos y el nombre de la lista a ordenar.
        - Se pueden ordenar las listas por nombre, por autor, por álbum, por año y
        por tipo o género"""
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
        """
        Esta función devuelve las opciones para el menú de ordenar listas
        según el formato que se esté usando.
        - Devuelve un strings con las opciones que el usuario puede escoger en el
        menú de ordenar listas (Varían para música).
        """
        if self.format == "music":
            return "1. Por nombre.\n2. Por artista.\n3. Por álbum.\n4. Por año.\n5. Por género.\n\n0. Atrás.\n"
        else:
            return "1. Por nombre.\n2. Por protagonista.\n3. Por álbum.\n4. Por año.\n5. Por tipo.\n\n0. Atrás.\n"

    def EmptyListMenu(self):
        """Este método es llamado cuando hay una lista vacía. Imprime en consola
        el mensaje que le indica al usuario cuando no hay elementos en la lista
        que está manejando."""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("No hay elementos en "+ self.listName +".")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        wait = input("Pulse Enter para continuar...")
        return

    def NotFoundMenu(self, listName):
        """
        Cada vez que hay una busqueda y no se encuentren resultados se llama
        a esta función que corresponde al menú donde el usuario escoge si
        desea volver a buscar o salir al menú anterior.
        Retorna la opción que el usuario ingrese para que esta pueda ser utilizada
        en el método donde fue llamado.
        """
        self.listName = listName
        print("No se encontró ningún elemento en " + self.listName +".\n")
        print("1. Volver a buscar.\n0. Atrás.\n")
        self.Answer(["0","1"])
        return

    def GetPrintLength(self, _list):
        """
        Recibe una lista de diccionarios.

        Devuelve un diccionario con las llaves ("name", "author", "album", "year", "type"),
        el valor de cada llave es un entero con el tamaño de la cadena más grande encontrada
        en esa columna de la lista.
        """
        keys = ("name", "author", "album", "year", "type")
        spanishKeys = ("Nombre", "Artista", "Álbum", "Año", "Género")
        ans = {}
        for i in range(len(keys)):
            temp = [len(spanishKeys[i])]
            for entry in _list:
                temp.append(entry.lengths[keys[i]])
            ans[keys[i]] = max(temp)
        return ans

    def PrintList(self, _list):
        """
        Esta función se encarga de llamar a los demás métodos para imprimir cualquier
        lista por consola en el orden adecuado
        """
        self._list = _list
        spaces = self.GetPrintLength(_list)
        self.PrintListHead(spaces)
        for dicIndex in range(len(self._list)):
            self._list[dicIndex].Print(spaces, dicIndex)

    def PrintListHead(self, spaces=None):
        """Este método imprime en consola el encabezado de una lista con sus
        elementos."""
        if self.format == "music":
            author = "Artista"
            _type = "Género"
        else:
            author = "Protagonista"
            _type = "Género"

        if spaces == None:
            print("No.\t|\tNombre\t|\t{0}\t|\tÁlbum\t|\tAño\t|\t{1}\n".format(author, _type))
        else:
            toPrint = "No.\t|"
            toPrint += "Nombre" + (" " * (spaces["name"] - len("Nombre"))) + "|"
            toPrint += author + (" " * (spaces["author"] - len(author))) + "|"
            toPrint += "Álbum" + (" " * (spaces["album"] - len("Álbum"))) + "|"
            toPrint += "Año" + (" " * (spaces["year"] - len("Año"))) + "|"
            toPrint += _type + (" " * (spaces["type"] - len(_type))) + "|\n"
            print(toPrint)
        return

    def SelectListElement(self, listLength):
        """
        Esta función recibe el largo de una lista y devuelve el indice del
        elemento que el usuario escoja.
        """
        self.listLength = listLength
        print("\n¿Cuál desea seleccionar? ")
        self.Answer([str(x) for x in range(1,self.listLength+1)])
        return int(self.answer) - 1





class PrincipalMenu (MenuManagement):
    """En esta clase se encuentran los métodos de los menús principales de la
    aplicación. Desde esta clase comienzan las ramas de los menús, comenzando
    desde el menú principal, hasta el menú de las listas de reproducción. Tiene
    métodos adicionales que corresponden a los menús de búsqueda, los menús de
    elementos específicos, los menús de añadir a lista de reproducción, etc.
    - Esta clase hereda de MenuManagement, lo que implica que puede manejar los
    métodos contenidos en esta."""

    def MainMenu(self):
        """Esta función corresponde al menú principal en el cual el usuario
        tiene la opción de seleccionar el formato al que quiere acceder (Música,
        Fotos o Videos).
        - Este menú le asigna el formato a la propiedad self.format, sobre el cual
        se trabaja en el resto de menús. Luego llama al segundo menú.
        - Se llama a sí misma una vez el método llamada termine."""
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
        """Este método se encarga de mostrar el segundo menú y las opciones para
        que el usuario pueda ver sus archivos multimedia o las listas de reproducción.
        - La primera opción hace un llamado al tercer menú.
        - La segunda opción llama al cuarto menú.
        - Se llama a sí misma cuando las funciones llamadas se acaban."""
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
        self.__SecondMenu()

    def __ThirdMenu(self):
        """Este método corresponde al tecer menú, en el cual el usuario puede
        escoger entre ver de manera ordenada todas sus canciones fotos o videos,
        buscar un elemento o añadir uno nuevo.
        - La primera opción llama al método SortListMenu.
        - La segunda opción llama al menú de búsqueda.
        - La tercera opción llama al menú de añadir elemento.
        - Se llama a sí misma cuando las funciones llamadas se acaban."""
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
        """Este método corresponde al menú de búsqueda, en el cual el usuario
        introduce una información sobre un elemento, ya sea el nombre, el álbum, el
        año, etc. y se imprimen las posibles opciones para dicha búsqueda.
        - En el caso de no haber resultados llama a NotFoundMenu y le pregunta al
        usuario si desea realizar la búsqueda de nuevo o salir al tercer menú.
        - En el caso de haber más de un resultado, le pide al usuario seleccionar
        algún elemento.
        - Con el elemento encontrado llama a FoundElementMenu, donde el usuario
        dispone de más opciones.
        - Al terminar, vuelve al tercer menú."""
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
        """Esta función corresponde al menú que el usuario dispone cuando encuentra
        un elemento. Desde este menú puede añadir dicho elemento a una lista de
        reproducción, eliminarlo o modificar su información.
        - Recibe como argumentos el objeto del elemento que se encontró en el SearchMenu.
        - La primera opción lleva al usuario a un menú donde seleccionará la lista
        a la que quiere añadir el elemento encontrado.
        - La segunda opción elimina el elemento mediante el método DeleteEntry de
        la clase MainList.
        - La tercera opción lleva al menú de modificación, donde se ingresa la nueva
        información del elemento y se reemplaza por la información del viejo elemento.
        - Al terminar, vuelve al tercer menú."""
        self.__foundElement = foundElement
        print("\n===================0===================\n")
        self.PrintList([self.__foundElement])
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

    def __AddToPlaylistMenu(self, toAddElement):
        """Esta función corresponde al menú donde el usuario selecciona la lista de
        reproducción a la que quiera añadir el elemento encontrado.
        - Como argumento recibe el objeto del elmento encontrado en el menú anterior.
        - El programa avisa cuando no hay listas de reproducción.
        - Esta función llama a AddEntry de la librería files para añadir el elemento
        a la lista.
        - Al terminar, el programa se devuelve al tecer menú."""
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
            self.__playlistObject.AddEntry(self.__toAddElement)
            print("Se añadió \""+self.__toAddElement.getName()+ "\" a " + self.playlistName + ".")
            return

    def __ModifyElementMenu(self, oldElementObject):
        """Esta función corresponde al menú donde el usuario ingresa la nueva
        información de un elemento para modificarlo.
        -Recibe como argumento el objeto del elemento que se desea modificar.
        - Llama a TakeElementInfo para tomar la nueva información, y a ModifyList
        de la clase MainList para reemplazar el archivo principal.
        - Al terminar, vuelve al tercer menú."""
        print("\nIngrese la nueva información del elemento.")
        newElementObject = self.TakeElementInfo()
        _MainList = MainList(self.format)
        _MainList.ModifyList(newElementObject,oldElementObject)
        print("Se ha modificado la información del elemento. Volviendo a \"MI" + self.MenuFormat(False).upper()+"\".")

    def __FourthMenu(self):
        """Este método corresponde al CUARTO menú, en el cual se encuentran las
        diferentes opciones para las listas de reproducción.
        - La primera opción muestra las playlist creadas y le pregunta al usuario si
        desea seleccionar alguna. En el caso de seleccionar alguna, crea un objeto
        de tipo PlaylistMenu, donde se despliega un menú para una lista en
        específico. Del caso contrario, el método se llama a sí mismo.
        - La segunda opción llama al menú donde se crean nuevas listas de reproducción.
        - La tecrcera opción permite buscar listas de reproducción.
        - La cuarta opción elimina alguna playlist.
        - Cuando las funciones terminan, el método se llama a sí mismo hasta que el
        usuario introduce la opción '0'."""
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

    def __SearchPlaylistMenu(self, toDo = "buscar"):
        """Esta función sirve para buscar una lista de reproducción y eliminarla o
		ir a su menú específico, dependiendo del argumento toDo:
			° "buscar" (PREDERETMINADO): Crea el objeto del menú específico de
			playlist luego de encontrar la lista de reproducción.
			° "eliminar": Elimina la lista encontrada luego de confirmar si el usuario
			desea eliminarla.
		-Esta función no retorna ningún valor. Al terminar vuelve al cuarto menú."""
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

    def __NewPlaylistMenu(self):
        """Este método se encarga de crear una nueva lista de reproducción y de
        agregar elementos a esta.
        - Contiene un bucle que termina cuando el usuario deja de añadir elementos
        a la lista.
        - Al terminar, vuelve al cuarto menú."""
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
            return

class PlaylistMenu(MenuManagement):
    """
    La siguiente clase esta relacionada con todo el manejo de los menús de las playlist
    se encuentra el metodo PlaylistMenu que imprime el menú para cada playlist,
    además se definen los métodos nesesarios para el correcto manejo de
    dichas listas(añadir y eliminar elementos, imprimir la playlist, etc...)
    esta clase hereda de MenuManagement puesto que es una clase que añade
    varios métodos para manejar todos los menús y se utilizan sus
    funciones y propiedades heredadas.
    """

    def __init__(self,_format, playlistName):
        """
        Función que inicializa un objeto del tipo menú de playlist, aqui se defien el formato de la playlist y el nombre.
        Una vez teniendo el nombre se inicializa un objeto tipo playlist para enlazarlo y ser utilizado más adelante
        para acceder a la lista y al archivo .txt.
        """
        self.format = _format
        self.playlistName = playlistName
        self.__playlist = Playlist(self.format, self.playlistName)

    def PlaylistMenu(self):
        """
        Esta función corresponde al menú específico de las listas de reproducción,
        desde aquí el usuario tiene más opciones que puede ejecutar sobre estas.
        - La primera opción permite ver el contenido ordenado de la lista.
        - La segunda opción permite añadir un elemento a la lista.
        - La tercera opción busca un elemento dentro de la lista para eliminarlo.
        - La cuarta opción elimina la lista de reproducción y retorna al cuarto menú.
        """
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
        """
        Función que se encarga de preguntarle al usuario qué elementos desea añadir a una
        playlist, busca los elementos que el usuario introdujo por consola dentro
        de la mainlist del formato y los añade a la playlist seleccionada.
        (en caso de encontrar varias coincidencias con la busqueda, se le pide al usuario
        que seleccione una de esas)
        -Antes de añadirlo le pide al usuario confirmar que desea añadir el elemento.
        -Al terminar, vuelve al menú específico de la lista.
        """
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
            self.PrintList(self.__results)
            print("\n¿Desea añadir este elemento a " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.\n")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("\nNo se añadió el elemento.\n")
                return
            else:
                self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                print("\nSe añadió \""+ self.__finalElement.getName() + "\" a " + self.playlistName + ". Volviendo al menú de la lista de reproducción.\n")
        else:
            self.PrintList(self.__results)
            print("")
            self.index = self.SelectListElement(len(self.__results))
            self.__finalElement = self.__results[self.index]
            self.PrintList([self.__finalElement])
            print("\n¿Desea añadir este elemento a " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.\n")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("\nNo se añadió el elemento.\n")
                return
            else:
                self.__playlist.AddEntry(self.__finalElement)#mirar que es param Entry
                print("\nSe añadió \""+ self.__finalElement.getName() + "\" a " + self.playlistName + ". Volviendo al menú de la lista de reproducción.\n")


    def __PrintPlaylist(self):
        """
        Método que se encarga de imprimir la playlist en consola por medio de un
        método definido en la clase padre.
        el metodo lo redirige a un menú donde pregunta en que orden desea visualizar
        la información y lo imprime.
        - Al terminar vuelve al menú específico de la lista.
        """
        self.SortListMenu(self.__playlist, self.playlistName)
        return

    def __DeletePlaylistElement(self):
        """
        Esta función se encarga de buscar un elemento en la lista de reproducción
        y llama a un metodo para elimininar este elemento del archivo .txt.
        - En el caso de no encontrar el elemento en la lista, le da la opción al
        usuario de volver a buscar o salir.
        - Antes de eliminar un elemento le pide al usuario confirmar la acción.
        - Al terminar, vuelve al menú específico de la lista.
        """
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
            self.PrintList(self.__results)
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
            self.PrintList([self.__finalElement])
            print("¿Desea eliminar este elemento de " + self.playlistName + "?\n1. Confirmar.\n0. Cancelar.")
            self.Answer(["0", "1"])
            if self.answer == 0:
                print("El elemento no se eliminó.\n")
                return
            else:
                self.__playlist.DeleteEntry(self.__finalElement)#mirar que es param Entry
                print("Se eliminó el elemento de " + self.playlistName + ". Volviendo al menú de la lista de reproducción.")
