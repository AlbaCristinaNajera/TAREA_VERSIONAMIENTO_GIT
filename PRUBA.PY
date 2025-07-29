#PRIMERA VERSION DEL CODIGO
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola, {nombre}!, bienvenid@ a la primera version del código")
print()
edad = int(input("Por favor ingresa tu edaad: "))
# SEGUNDA VERSION DEL CODIGO
print("Tu edad actual es: ", edad, "años", "y esta es la segunda versión del código")
print()
# TERCERA VERSION DEL CODIGO
print("CALCULADORA BÁSICA")
num1 = int(input("Por favor, ingresa un número: "))
num2 = int(input("Por favor, ingresa otro número: "))

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
    else:
        print("Operación no válida. Por favor, selecciona una opción válida.")



