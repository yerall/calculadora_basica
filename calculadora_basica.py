
def suma(a, b):
    print(f"\nEl resultado de la suma de {a} y {b} es: {a + b}")

def resta(a, b):
    print(f"\nEl resultado de la resta de {a} y {b} es: {a - b}")

def multiplicacion(a, b):
    print(f"\nEl resultado de la multiplicación de {a} y {b} es: {a * b}")

def division(a, b):
    if b != 0:
        print(f"\nEl resultado de la división de {a} entre {b} es: {a / b}")
    else:
        print("\nError: No se puede dividir entre cero.")

def division_exacta(a, b):
    if b != 0:
        print(f"\nEl resultado de la división exacta de {a} entre {b} es: {a // b}")
    else:
        print("\nError: No se puede dividir entre cero.")

def exponente(a, b):
    print(f"\nEl resultado de {a} elevado a la potencia de {b} es: {a ** b}")

def obtener_numeros():
    while True:
        try:
            n1 = float(input("\nIngrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            return n1, n2
        except ValueError:
            print("Por favor, ingrese números válidos.")

def menu_principal():
    print("""
== CALCULADORA SIMPLE ==

1) Sumar dos números
2) Restar dos números
3) Multiplicar dos números
4) Dividir dos números
5) División exacta de dos números
6) Elevar un número a otro
7) Salir del programa
""")

opciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: division_exacta,
    6: exponente
}

while True:
    menu_principal()
    try:
        opcion = int(input("Ingrese la opción: "))
        if opcion in opciones:
            n1, n2 = obtener_numeros()
            opciones[opcion](n1, n2)
        elif opcion == 7:
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
    except ValueError:
        print("\nError: Por favor, ingrese un número válido.")
