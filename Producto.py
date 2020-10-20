from Indice import *
class Producto:
    def __init__(self,nombre,fecha_r,unidades,fecha_v):
        self.nombre=nombre
        self.fecha_r=fecha_r
        self.unidades=unidades
        self.fecha_v=fecha_r
    def imprimir(self):       
        print(self.nombre)
        print(self.fecha_r)
        print(self.unidades)
        print(self.fecha_v)