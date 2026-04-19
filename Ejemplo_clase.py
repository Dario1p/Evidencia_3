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

    def info(self):
        print(f"El titulo del juego es: {self.get_titulo()}")
        print(f"El genero del juego es: {self.get_genero()}")
        print(f"El precio del juego es: {self.get_precio()}")
        print(f"La plataforma del juego es: {self.get_plataforma()}")
        print(F"Tus horas jugadas en el juego son: {self.get_horas_jugadas()}")

    def descuento(self, porcentaje):
        precio_actual = self.get_precio()
        descuento = precio_actual * porcentaje
        descuento = descuento / 100
        self.set_precio(precio_actual - descuento)
        print(f"Oferta aplicada, el descuento fue de {porcentaje}%")

    def registrar_horas_jugadas(self, horas):
        total_horas = self.get_horas_jugadas() + horas
        self.set_horas_jugadas(total_horas)
        print(f"Sumaste {horas} el total de horas jugadas ahora son: {self.get_horas_jugadas()}")

    