from Indice import *
def inicializacion(arch,a):
    
    with open(arch) as f_obj:
            nombres=f_obj.readlines()
    
    n=a
    pr=[]
    for i in range (n):
        nombre=nombres[randint(0,999)]
        fechar=date(randint(2015,2020),randint(1,12),randint(1,28))
        fechav=date(randint(2020,2026),randint(1,12),randint(1,28))
        cant=randint(1,10)
        pr.append(Producto(nombre,fechar,fechav,cant))
    return pr

