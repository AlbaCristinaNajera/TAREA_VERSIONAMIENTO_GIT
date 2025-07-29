print("*****BIENVENIDO A LA CALCULADORA DE OPERACIONES BÁSICAS******")
print("Esta es una calculadora que realiza operaciones básicas como suma, resta, multiplicación y división.")

#PRIMERA VERSION DEL CODIGO
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola, {nombre}!, bienvenid@ a tu calculadora de confianza")
print()

print("Para comenzar, por favor ingresa dos números enteros.")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print()
salir = False

while salir != True:
    print()
    print("Qué operacion quieres realizar?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == 2: #CUARTA VERSION DEL CÓDIGO, NUEVAS FUNCIONALIDADES
        resta = num1 -num2
        print(f"La resta de {num1} y {num2} es: {resta}")
    elif opcion == 3:
        multiplicacion = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    elif opcion == 4 : #QUINTA VERSION DEL CÓDIGO, NUEVAS FUNCIONALIDADES
        if num2 != 0:
            division = num1 /num2
            print(f"La división de {num1} y {num2} es: {division}")
        elif num2 == 0:
            print("Error: No se puede dividir por cero.")
    elif opcion == 5:
        salir = True
        print("Saliendo de la calculadora. Hasta luego", nombre)
    else:
        print("Operación no válida. Por favor, selecciona una opción válida.")



