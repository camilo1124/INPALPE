from Indice import *
to=time()
archivo='texto/productos.txt'
n=10000
p=inicializacion(archivo,n)
tf=time()
t=tf-to
print(t,'milisegundos')

#metodo para crear


print("Inventario para alimentos perecederos")
print("Opciones:")
print("1.Añadir:")
print("2.Actualizar:")
print("3.Eliminar:")
print("4.Consultar todo")
print("5.Consulta por elemento")
print("6.Salir")
opc= input()
op=int(opc)
while ( op < 5):
    if(op==1):
        print("Fecha de Vencimiento:")
        anio=input("Año:")
        mes=input("Mes:")
        dia=input("Dia:")
        fecha=date(anio,mes,dia)
        nombre=input("Nombre del producto")
        cant=input("Cantidad:") 
        to=time()
        p.append(Producto(nombre,date.today(),fecha,cant))
        tf=time()
        t=tf-to
        print(t,'milisegundos')
    elif(op==2):
        nombre=input("Producto a modificar")
        cantidad=input("Cantidad:")
        print("Fecha de vencimiento:") 
        anio=input("Año:")
        mes=input("Mes:")
        dia=input("Dia:")
        fecha=date(anio,mes,dia) 
        to=time()
        for i in range (len(p)):
            if (p[i].nombre==nombre):
                p[i].modificar(nombre,fecha,cantidad)
        tf=time()
        t=tf-to
        print(t,'milisegundos')
        
    elif(op==3):
        nombre=input("Producto a eliminar")
        to=time()
        for i in range (len(p)):
            if (p[i].nombre==nombre):
                del p[i]
        tf=time()
        t=tf-to
        print(t,'milisegundos')
    elif(op==4):
        to=time()
        for i in range (len(p)):
            p[i].mostrar_ele()
        tf=time()
        t=tf-to
        print(t,'milisegundos')
    elif(op==5):
        to=time()
        nombre=input("Busqueda por nombre/ingresar nombre:")
        for i in range (len(p)):
            if (p[i].nombre==nombre):
                p[i].mostrar_ele()
        tf=time()
        t=tf-to
        print(t,'milisegundos')
    print("Inventario para alimentos perecederos")
    print("Opciones:")
    print("1.Añadir:")
    print("2.Actualizar:")
    print("3.Eliminar:")
    print("4.Consultar todo")
    print("5.Consulta por elemento")
    print("6.Salir")
    opc= input()
    op=int(opc)
        
        
        


    

    
    







   

