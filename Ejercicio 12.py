def obtener_tipo_mime(nombre_archivo):
    # Definir el diccionario de mapeo de extensiones a tipos MIME
    mapeo_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip',
    }

    # Obtener la extensión del archivo
    _, extension = nombre_archivo.rsplit('.', 1) if '.' in nombre_archivo else (None, None)

    # Determinar el tipo MIME
    tipo_mime = mapeo_mime.get(extension.lower(), 'application/octet-stream')

    return tipo_mime

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"Tipo MIME para {nombre_archivo}: {tipo_mime}")