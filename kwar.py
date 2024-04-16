def buscar_datos(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, **kwargs):
    for key, value in kwargs.items():
        if (value["primer_nombre"] == primer_nombre and value["segundo_nombre"] == segundo_nombre and value["primer_apellido"] == primer_apellido and value["segundo_apellido"] == segundo_apellido):
            return True
    return False

database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    }
}

print(buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database))  # Debería imprimir True
print(buscar_datos("a", "b", "c", "d", **database))  # Debería imprimir False