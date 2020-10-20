from Indice import *
class Producto:
    def __init__(self,nombre,fecha_r,fecha_v,unidades):
        self.nombre=nombre
        self.fecha_r=fecha_r
        self.unidades=unidades
        self.fecha_v=fecha_r
        if self.fecha_v<=date.today():
            vencido= True
        else:
            vencido=False
    def info(self):       
        print(self.nombre)
        print(self.fecha_r)
        print(self.fecha_v)
        print(self.unidades)
    def esta_vencido(self):
        return vencido
    def modificar(self,nombre,fechav,cantidad):
        self.nombre=nombre
        self.fecha_v=fechav
        self.unidades=cantidad
    def mostrar_ele(self):
        print("Nombre:")
        print(self.nombre)
        print("Fecha de registro:")
        print(self.fecha_r)
        print("Fecha de vencimiento:")
        print(self.fecha_v)
        print("Cantidad:")
        print(self.unidades)
        
    
        
        