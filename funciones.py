print("Ejemplo de funciones")
# declarando funciones 
def hola():
    print("Alguien uso la funcion hola")
def chat(mensa):
    print(f"Roger(Pedófilo) {mensa}")
def ellacontesta(mensa):
    print(f"Niña de 9 años {mensa}")
def name(ap,n):
    print(f"Roger(Pederasta en potencia) {n}{ap}")
def suma(a,b):
    s=a+b
    return s
def resta(a,b):
    s1=a-b
    return s1
def multi(a,b):
    s11=a*b
    return s11
def div(a,b):
    s111=a/b
    return s111
## llamadas a funciones 
hola()
chat("Hola niña")
ellacontesta("Alejate de mi")
print("Acompañame" "a mi casa")
print("Operaciones básicas")
c1=int(input("Ingresa un número: "))
c11=int(input("Ingresa otro número: "))
damesuma=suma(c1, c11)
print(f"La suma de {c1} + {c11} = {damesuma}")
c1=int(input("Ingresa un número: "))
c11=int(input("Ingresa otro número: "))
damesuma1=resta(c1, c11)
print(f"La resta de {c1} - {c11} = {damesuma1}")
c1=int(input("Ingresa un número: "))
c11=int(input("Ingresa otro número: "))
damesuma11=multi(c1, c11)
print(f"La multiplicacion de {c1} * {c11} = {damesuma11}")
c1=int(input("Ingresa un número: "))
c11=int(input("Ingresa otro número: "))
damesuma111=div(c1, c11)
print(f"La division de {c1} / {c11} = {damesuma111}")








