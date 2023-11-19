# Asignar dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú
print("Menú:")
print("1. Suma de dos números")
print("2. Resta de dos números (el primero menos el segundo)")
print("3. Multiplicación de dos números")

# Solicitar al usuario que elija una opción
opcion = input("Elija una opción (1, 2 o 3): ")

# Realizar la operación y mostrar el resultado
if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")