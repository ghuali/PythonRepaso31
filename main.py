import copy
import sys
import random

Lista1 = ["Sol badguy", "Angel", "Neon"]
Lista2 = Lista1.copy()
print(f"{Lista1}, y la duplicada es, {Lista2}")

listavieja = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listanueva = copy.copy(listavieja)

print("Vieja list:", listavieja)
print("Nueva list:", listanueva)

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)

Listaapended = ["Sol badguy", "Neon", "Ekko"]
print(Listaapended)
Listaapended.append("Zeri")
print(Listaapended)

Listapopped = ["Sol badguy", "Neon", "Ekko"]
print(Listapopped)
Listapopped.pop()
print(Listapopped)

listadel = ["Sol badguy", "Neon", "Ekko"]
print(listadel)
listadel.remove("Neon")
print(listadel)

listaordenada = ["Sol badguy", "Angel", "Zeri", "Neon", "ekko", "Aatrox", "Jett"]
print(listaordenada[-4:])

stringGenerica = "Hola soy un string generico"
print(stringGenerica.split(" "))

"""Hola soy un comentario"""

"""Hola soy
    un buen comentario"""


def suma(a, b):
    return a + b


print(suma(input("Dame un numero: "), input("Dame otro numero: ")))


def cambios(Listacambio):
    for i in range(len(Listacambio)):
        Listacambio[i] *= 2


Listanum = [3, 4]
cambios(Listanum)
print(Listanum)


def noCambio(ListaNocambio):
    listaResult = ListaNocambio[:]
    for i in range(len(listaResult)):
        listaResult[i] *= 2
    return listaResult


Listanum2 = [3, 4]
print(noCambio(Listanum2))
print(Listanum2)


def MenuLista(opcion):
    Usuarios = ["Angel", "Sol badguy"]
    Contraseñas = ["Angel123", "Sol badguy123"]

    if opcion == 1:
        Usuarios, Contraseñas = contraseñaNueva(Usuarios, Contraseñas)
    elif opcion == 2:
        Usuarios, Contraseñas = LoginLista(Usuarios, Contraseñas)
    else:
        print("Opción no válida")


def LoginLista(Usuarios, Contraseñas):
    Usuario = input("Dame tu nombre de usuario: ")
    Contraseña = input("Dame tu contraseña: ")

    if Usuario in Usuarios:
        indice = Usuarios.index(Usuario)
        if Contraseñas[indice] == Contraseña:
            print("Bienvenido")
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario o contraseña incorrectos")

    return Usuarios, Contraseñas


def contraseñaNueva(Usuarios, Contraseñas):
    usuario = str(input("Dame tu nombre de usuario: "))
    contraseña = str(input("Dame tu contraseña: "))

    usuario.append(Usuarios)
    contraseña.append(Contraseñas)

    print(f'{Usuarios} y {Contraseñas}')

    return Usuarios, Contraseñas


# print(MenuLista(int(input("Dame una opcion: "))))




def Logins():
    LoginDicc = [
        {
            "Usuario": "Angel",
            "Contraseña": "Angel123"
        },
        {
            "Usuario": "Sol badguy",
            "Contraseña": "Sol badguy123"
        }]

    Usuario = input("Dame tu nombre de usuario: ")
    Contraseña = input("Dame tu contraseña: ")

    for login in LoginDicc:
        if Usuario == login["Usuario"] and Contraseña == login["Contraseña"]:
            print("Bienvenido")
        elif Usuario == login["Usuario"] and Contraseña != login["Contraseña"]:
            print("Usuario o contraseña incorrectos")
            print("Quieres añadirlo a la lista de usuarios? 1.Si 2.No")
            opcion = input()
            if opcion == '1':
                LoginDicc.append({
                    "Usuario": Usuario,
                    "Contraseña": Contraseña
                })
                print(LoginDicc)
            else:
                print("Hasta luego")


print(Logins())

# "is": Compara si dos objetos son el mismo en memoria.
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)

# "not": Invierte el valor booleano de una expresión.
x = True
y = False

print(not x)
print(not y)

n = 10
print(not n == 10)

# "in": Verifica si un elemento está presente en una secuencia o estructura
frutas = ["manzana", "banana", "cereza"]

print("manzana" in frutas)
print("naranja" in frutas)

for x in range(len(sys.argv)):
    print(len(sys.argv[x]))


def sumas(*args):
    return sum(args)


# Usos:
print(sumas(1, 2))
print(sumas(1, 2, 3, 4, 5))
print(sumas())

datos = [
    [170, 70],
    [180, 90],
    [170, 65],
    [160, 60],
    [180, 80],
    [160, 55]
]


def clave_ordenacion(elemento):
    return (-elemento[0], elemento[1])


datos_ordenados = sorted(datos, key=clave_ordenacion)

print(datos_ordenados)


class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"El color del coche con matrícula {self.matricula} ha sido cambiado a {nuevo_color}")

    def obtener_info(self):
        return f"Coche Matrícula: {self.matricula}, Color: {self.color}"


colores = ["rojo", "blanco", "negro", "rosa", "azul"]

n = int(input("Introduce el número de coches que quieres crear: "))

coches = []

for i in range(1, n + 1):
    color_aleatorio = random.choice(colores)
    coche = Car(matricula=i, color=color_aleatorio)
    coches.append(coche)

print(f"\nMostrando los primeros {min(n, 10)} coches:")
for coche in coches[:10]:
    coche.imprimir()

suma = lambda x, y: x + y

resultado = suma(5, 3)
print(resultado)

from functools import reduce

cadena = input("Introduce una cadena de números separados por espacios: ")
numeros = list(map(int, cadena.split()))
print(f"Lista de números: {numeros}")

numeros_filtrados = list(filter(lambda x: x >= 10, numeros))
print(f"Lista filtrada (números >= 10): {numeros_filtrados}")

if numeros_filtrados:
    multiplicacion = reduce(lambda x, y: x * y, numeros_filtrados)
    print(f"Multiplicación de los números filtrados: {multiplicacion}")
else:
    print("No hay suficientes números mayores o iguales a 10 para multiplicar.")







