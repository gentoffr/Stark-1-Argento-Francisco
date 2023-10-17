from data_stark import *
import os
for i in lista_personajes:
    i['altura'], i["peso"], i["fuerza"] = float(i["altura"]), float(i["peso"]), float(i["fuerza"])
def print_nombres(lista):
    for i in lista:
        print(f"""Nombre: {i['nombre']}
    Identidad: {i['identidad']}
    Empresa: {i['empresa']}
    Altura: {i['altura']}
    Peso: {i['peso']}
    Genero: {i['genero']}
    Color de ojos: {i['color_ojos']}
    Color de pelo: {i['color_pelo']}
    Fuerza: {i['fuerza']}
    Inteligencia: {i['inteligencia']}
    ----------------------------------""")
    
def mayor_fuerza(lista, mayor=True, menor=False):
    flag = True
    mayor_num = 0
    for i in lista:
        if mayor:
            if i['fuerza'] > mayor_num or flag:
                mayor_num = i['fuerza']
                nombre_mayor = i["nombre"]
                identidad_mayor = i["identidad"]
                peso_mayor = i["peso"]
                flag = False
    print(f"""El heroe mas fuerte es: 
{nombre_mayor} ({identidad_mayor}) 
Peso: {peso_mayor} 
Fuerza: {mayor_num}""")

def mas_bajo(lista, bajito=True):
    flag = True
    for i in lista:
        if bajito:
            if i["altura"] < bajito or flag:
                bajito = i["altura"]
                nombre_bajo = i["nombre"]
                identidad_bajo = i["identidad"]
                flag = False
    print(f"El heroe mas bajo es: {nombre_bajo} ({identidad_bajo})")

def sacar_promedio(datos, llave: str, genero="_"):
    suma = 0
    count = 0
    for i in datos:
        if i["genero"] == genero:
            suma += i[llave]
            count += 1
        elif genero == "_":
            suma += i[llave]
            count += 1
    promedio = round(suma / count, 2)
    return promedio


def promedio_peso(lista):
    print(f"El promedio de peso es {(sacar_promedio(lista, 'peso'))}, kg")

def punto_e_re_random_el_nombre_de_la_funcion(lista):
    promedio = sacar_promedio(lista, "fuerza", "F")
    rando = []
    print("Los heroes con fuerza sobre el promedio de fuerza femenino son:") 
    for i in lista:        
        if i["genero"] == "M":
            if i["fuerza"] > promedio:
                rando.append({"nombre": i["nombre"], "peso": i["peso"]})
        print(f"{i['nombre']}, peso {i['peso']}kg")     
    # print(f"""Los heroes con fuerza sobre el promedio de fuerza femenino son: """, * rando, sep=', ')


flag = True
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----------------------------------")

while flag or pregunta == "s":
    clear_console()
    print("""1. Mostrar nombres
2. Mayor fuerza
3. Mas bajo
4. Promedio de peso
5. Promedio de fuerza por genero""")
    eleccion = input("Elija una opcion: ")
    match eleccion:
        case "1":
            clear_console()
            print_nombres(lista_personajes)
        case "2":
            clear_console()
            mayor_fuerza(lista_personajes)
        case "3":
            clear_console()
            mas_bajo(lista_personajes)
        case "4":
            clear_console()
            promedio_peso(lista_personajes)
        case "5":
            clear_console()
            punto_e_re_random_el_nombre_de_la_funcion(lista_personajes)
        case "_":
            print("Opcion incorrecta")
            
    pregunta = input("Desea continuar? (s/n): ").lower()
    flag = False
            
