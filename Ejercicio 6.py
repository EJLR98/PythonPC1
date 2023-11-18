# Asignar el valor de la edad a una variable
edad_cliente = 25  # Puedes cambiar este valor según sea necesario

# Calcular el precio de la entrada según la edad
precio_entrada = 0 if edad_cliente < 4 else 5 if 4 <= edad_cliente <= 18 else 10

# Mostrar el precio de la entrada
print(f"El precio de la entrada es: ${precio_entrada}")