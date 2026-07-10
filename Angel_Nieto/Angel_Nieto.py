def menu():
    print(" Menu Principal ".center(30, "-")) 
    print("1. Cupos por Genero")
    print("2. Busqueda de peliculas")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese una opcion: "))
            if 1<=opcion<=6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
                return False
        except ValueError:
            print("Debe seleccionar una opcion valida")
            return False

def validar_codigo(valor, peliculas):
    if len(valor)<1:
        return False
    if " " in valor:
        return False
    if valor in peliculas:
        return False
    return True

def validar_textovacio(valor):
    if len(valor)<0:
        return False
    return True

def validar_clasificacion(valor):
    return valor.upper() in ("A", "B", "C")

def validar_es_3d(valor):
    return valor.lower() in ("s", "n")

def validar_precio(valor):
    try:
        costo=input(valor)
        return costo>0
    except ValueError:
        return False
    
def validar_cupos(valor):
    return valor.isdigit() and int(valor)>=0

def validar_busqueda_precio(p_min, p_max):
    return p_min>=0 and p_max>=0 and p_min<=p_max

def buscar_codigo(codigo, peliculas):
    if codigo in peliculas:
        return True
    return False

def cupos_genero(cartelera, peliculas):
    print(" Cupos Por Genero ".center(30, "-"))
    cupo_buscado=input("Ingrese Genero de pelicula que busca: ").strip()
    total_cupos=0
    encontro_pelicula=False
    for codigo in peliculas:
        genero_actual=peliculas[codigo][1]
        if genero_actual==cupo_buscado:
            encontro_pelicula=True
            total_cupos = total_cupos + cartelera[codigo][1]
    
    if encontro_pelicula:
        print(f"Total cupos para '{cupo_buscado}', {total_cupos}")

def busqueda_rango_precio(cartelera, peliculas):
    print(" Busqueda Rango de Precio ".center(30, "-"))
    while True:
        try:
            p_min=input("Ingrese valor minimo: ")
            p_max=input("Ingrese valor maximo: ")
            if validar_busqueda_precio(p_min, p_max):
                break
            else:
                print("No hay peliculas en ese rango de precio")
        except ValueError:
            print("Debe ingresar valores enteros")
    resultados=[]
    for codigo in peliculas:
        precio_pelicula=cartelera[codigo][0]
        cupos_disponibles=cartelera[codigo][1]
        if p_min<=precio_pelicula<=p_max and cupos_disponibles>0:
            titulo=peliculas[codigo][0]
            resultados.append(f"{titulo} -- {codigo}")
    resultados.sort()

    if len(resultados)==0:
        print("No se encontraron peliculas con esos cupos")
        return
    
    print("peliculas encontradas")
    for item in resultados:
        print(item)

def actualizar_precio(cartelera):
    print(" Actualizar precio de pelicula ".center(30, "-"))
    while True:
        codigo=input("Ingrese codigo de la pelicula para actualizar precio: ").strip()
        existe=buscar_codigo(codigo)
        if existe:
            while True:
                nuevo_precio=input("Ingrese el nuevo costo: ").strip()
                if validar_precio(nuevo_precio):
                    cartelera[codigo][0]=float(nuevo_precio)
                    print("Precio actualizado")
                    return True
                else:
                    print("El nuevo precio no puede ser un espacio en blanco ")
        else:
            print(f"El codigo {codigo} no existe")
            return False

        while True:
            respuesta=input("Desea actualizar otro costo? (s/n): ").strip().lower()
            if respuesta in ("s", "n"):
                break
            else:
                print("debe responder con 's' o 'n'")
        if respuesta == "n":
            break
        
def agregar_pelicula(peliculas, cartelera):
    print(" Agregar  pelicula ".center(30, "-"))
    while True:
        codigo=input("Ingrese codigo de la pelicula: ").strip()
        if validar_codigo(codigo, peliculas):
            break
        else:
            print("No puede estar vacio y no puede repetirse")

    while True:
        titulo=input("Ingrese titulo de la pelicula: ")
        if validar_textovacio(titulo):
            break
        else:
            print("No puede estar vacio")

    while True:
        genero=("Ingrese genero de la pelicula: ")
        if validar_textovacio(genero):
            break
        else:
            print("no  puede estar vacio")

    while True:
        idioma=("Ingrese idioma de la pelicula: ")
        if validar_textovacio(idioma):
            break
        else:
            print("No puede estar vacio")

    while True:
        duracion=("Ingrese duracion de la pelicula: ")
        if validar_textovacio(duracion):
            break
        else:
            print("Debe ser un numero mayor que 0") 

    while True:
        clasificacion=input("Ingrese calificacion de la pelicula (A/B/C): ")
        if validar_clasificacion(clasificacion):
            clasificacion=clasificacion.upper()
            break
        else:
            print("debe responder con 'A', 'B' o 'C'")

    while True:
        es_3d=input("Es 3D? (s/n): ").strip()
        if validar_es_3d(es_3d):
            es_3d=True if es_3d.lower() == "s" else False
            break
        else:
            print("debe responder con 's' o 'n'")

    while True:
        precio=input("Ingrese precio de pelicula: ")
        if validar_precio(precio):
            break
        else:
            print("Debe ser mayor que 0")

    while True:
        total_cupos=input("Ingrese cupos disponibles ").strip()
        if validar_cupos(total_cupos):
            break
        else:
            print("debe ser numerico y mayor que 0")

    peliculas[codigo]=[titulo, genero, duracion, idioma, clasificacion, es_3d]
    cartelera[codigo]=[precio,total_cupos]

    print("Se agrego la pelicula correctamente")

def eliminar_pelicula(peliculas, cartelera):
    print(" Eliminar Pelicula ".center(30, "-"))
    codigo=input("Ingrese codigo de pelicula que quiere eliminar: ")
    existe=buscar_codigo(codigo, peliculas)

    if existe:
        peliculas.pop(codigo)
        cartelera.pop(codigo)

        print("se elimino la mascota correctamnete")
    else:
        print(f"El codigo {codigo} no se encuentra registrado")

def main():
    peliculas={}
    cartelera={}
    while True:
        menu()
        opcion=int(input("Ingrese una opcion: "))
        opcion(leer_opcion)

        if opcion==1:
            cupos_genero(cartelera, peliculas)
        elif opcion==2:
            busqueda_rango_precio(cartelera, peliculas)
        elif opcion==3:
            if len(cartelera>0):
                actualizar_precio(cartelera)
            else:
                print("No hay peliculas para actualizar precio")
        elif opcion==4:
            agregar_pelicula(peliculas, cartelera)
        elif opcion==5:
            if len(peliculas)>0:
                eliminar_pelicula(peliculas, cartelera)
            else:
                print("no hay peliculas para eliminar")
        elif opcion==6:
            print("Programa finalizado")
            break

main()