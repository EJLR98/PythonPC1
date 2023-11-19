# Solicitar al usuario que ingrese la hora en formato de 24 horas
hora_usuario = input("Ingrese la hora en formato de 24 horas (por ejemplo, 08:30): ")

# Extraer la hora y los minutos de la entrada del usuario
hora, minutos = map(int, hora_usuario.split(':'))

# Definir los rangos de tiempo para desayuno, almuerzo y cena
rangos_comida = [(7, 8), (12, 13), (18, 19)]

# Verificar si es hora de desayunar, almorzar o cenar
for rango in rangos_comida:
    if rango[0] <= hora < rango[1]:
        print(f"¡Es hora de {'desayunar' if rango[0] == 7 else 'almorzar' if rango[0] == 12 else 'cenar'}!")
        break
else:
    # No es hora de comer
    pass