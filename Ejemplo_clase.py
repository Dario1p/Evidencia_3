class Videojuego:

    def _init_(self, titulo, genero, precio, plataforma, horas_jugadas):
        self.__titulo = titulo
        self.__genero = genero
        self.__precio = precio
        self.__plataforma = plataforma
        self.__horas_jugadas = horas_jugadas

    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def get_genero(self):
        return self.__genero
    def set_genero(self, nuevo_genero):
        self.__genero = nuevo_genero
    
    def get_precio(self):
        return self.__precio
    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def get_plataforma(self):
        return self.__plataforma
    def set_plataforma(self, nueva_plataforma):
        self.__plataforma = nueva_plataforma

    def get_horas_jugadas(self):
        return self.__horas_jugadas
    def set_horas_jugadas(self, nuevas_horas):
        self.__horas_jugadas = nuevas_horas
        