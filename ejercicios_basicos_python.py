# Ejercicios básicos en Python 

import math

def ejercicio1():
    print("Hola, ya se imprimir frases")

def ejercicio2():
    print(273)

def ejercicio3():
    print(5.3)


def ejercicio4():
    print(1234 + 532)

def ejercicio5():
    print(1234 - 532)

def ejercicio6():
    print(1234 * 532)

def ejercicio7():
    print(1234 / 532)

def ejercicio8():
    print(1)
    print(2)
    print(3)

def ejercicio9():
    for i in range(1, 10):
        print(i)

def ejercicio10():
    for i in range(1, 10001):
        print(i)

def ejercicio11():
    for i in range(5, 11):
        print(i)

def ejercicio12():
    for i in range(5, 16):
        print(i)

def ejercicio13():
    for i in range(5, 15001):
        print(i)

def ejercicio14():
    for i in range(200):
        print("hola")

def ejercicio15():
    for i in range(1, 31):
        print(i * i)

def ejercicio16():
    resultado = 1
    for i in range(1, 21):
        resultado *= i
    print(resultado)

def ejercicio17():
    suma = 0
    for i in range(1, 101):
        suma += i * i
    print(suma)

def ejercicio18():
    numero = int(input("Escribe un número: "))
    suma = 0
    for i in range(1, 101):
        suma += numero + i
    print(suma)

def ejercicio19():
    euros = float(input("Cantidad en euros: "))
    dolares = euros * 1.08
    print("Eso son", dolares, "dólares")

def ejercicio20():
    altura = float(input("Altura del rectángulo: "))
    anchura = float(input("Anchura del rectángulo: "))
    print("Área:", altura * anchura)

def ejercicio21():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    if a > b:
        print("El mayor es", a)
        print("El menor es", b)
    elif b > a:
        print("El mayor es", b)
        print("El menor es", a)
    else:
        print("Los dos números son iguales")

def ejercicio22():
    n = int(input("Escribe un número: "))
    for i in range(1, n):
        if i % 2 != 0:
            print(i)

def ejercicio23():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    while b != 0:
        a, b = b, a % b
    print("El MCD es", a)

def ejercicio24():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Soluciones:", x1, "y", x2)
    elif d == 0:
        x = -b / (2*a)
        print("Una solución:", x)
    else:
        print("No hay soluciones reales")

def ejercicio25():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    print("Factorial de 5:", factorial(5))

def ejercicio26():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    c = int(input("Tercer número: "))
    print("Mayor:", max(a, b, c))
    print("Menor:", min(a, b, c))

def ejercicio27():
    while True:
        f = float(input("Temperatura en Fahrenheit (999 para salir): "))
        if f == 999:
            break
        c = (5/9) * (f - 32)
        print("En Celsius:", c)

def ejercicio28():
    for i in range(1, 4):
        if i == 1:
            print("Caso 1")
        elif i == 2:
            print("Caso 2")
        elif i == 3:
            print("Caso 3")

def ejercicio29():
    print("Escribe números. Ctrl+D (Linux/Mac) o Ctrl+Z (Windows) para terminar.")
    try:
        while True:
            numero = int(input())
            print("Leído:", numero)
    except EOFError:
        print("Fin de entrada")

def ejercicio30():
    for num in range(2, 101):
        es_primo = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

# llamar a los ejercicios:
ejercicio30()