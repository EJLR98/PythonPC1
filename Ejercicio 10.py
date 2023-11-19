# Definir la lista original
lista_original = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Elementos a eliminar por valor
elementos_a_eliminar = ['Rojo', 'Rosa', 'Amarillo']

# Eliminar elementos por valor usando el método remove
for elemento in elementos_a_eliminar:
    lista_original.remove(elemento)

# Mostrar la lista después de la eliminación
print(lista_original)