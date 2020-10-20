from Indice import *
to=time()
archivo='texto/productos.txt'
n=1000
p=inicializacion(archivo,n)
tf=time()
t=tf-to
print(t,'milisegundos')


archivo_texto=open("archivo.txt","a")
for i in range(len(p)):
    archivo_texto.write(p[i].get_nombre())   
    archivo_texto.write(p[i].get_fecha_r())
    archivo_texto.write('\n')
    archivo_texto.write(p[i].get_fecha_v())
    archivo_texto.write('\n')
    archivo_texto.write(p[i].get_unidades())
    archivo_texto.write('\n')
    archivo_texto.write('\n')
archivo_texto.close()



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
while ( op < 6):
    if(op==1):
        print("Fecha de Vencimiento:")
        anio=int(input("Año:"))
        mes=int(input("Mes:"))
        dia=int(input("Dia:"))
        fecha=date(anio,mes,dia)
        nombre=input("Nombre del producto:")
        cant=int(input("Cantidad:")) 
        to=time()
        p.append(Producto(nombre,date.today(),fecha,cant))        
        archivo_texto=open("archivo.txt","a")
        archivo_texto.write(p[len(p)-1].get_nombre())   
        archivo_texto.write(p[len(p)-1].get_fecha_r())
        archivo_texto.write('\n')
        archivo_texto.write(p[len(p)-1].get_fecha_v())
        archivo_texto.write('\n')
        archivo_texto.write(p[len(p)-1].get_unidades())
        archivo_texto.write('\n')
        archivo_texto.write('\n')
        archivo_texto.close()
        tf=time()
        t=tf-to
        print(t,'milisegundos')
    elif(op==2):
        nombre=input("Producto a modificar:")
        cantidad=input("Cantidad:")
        print("Fecha de vencimiento:") 
        anio=int(input("Año:"))
        mes=int(input("Mes:"))
        dia=int(input("Dia:"))
        fecha=date(anio,mes,dia) 
        to=time()
        for i in range (len(p)):
            if (p[i].nombre==nombre):
                p[i].modificar(nombre,fecha,cantidad)
        tf=time()
        t=tf-to
        print(t,'milisegundos')
        
    elif(op==3):
        nombre=input("Producto a eliminar:")
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
        esta=False
        for i in range (len(p)):
            if (p[i].nombre==nombre):
                esta=True
                p[i].mostrar_ele()
        if(esta==False):
            print("El producto que solicita no esta registrado")
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
        
        
        


    

    
    







   

