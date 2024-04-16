database = {"Persona_1": {"Primer Nombre": "Pablo","Segundo Nombre": "Diego", "Primer Apellido": "Ruiz", "Segundo Apellido": "Picasso" },
            "Persona_2": {"Primer Nombre": "Ale","Segundo Nombre": "Seba", "Primer Apellido": "Sanchez", "Segundo Apellido": "Castelino" },
            "Persona_3": {"Primer Nombre": "Nahuel","Segundo Nombre": "Ian", "Primer Apellido": "Galera", "Segundo Apellido": "Suarez"}
            }


def buscar_datos(persona, database):
    if "" in persona.values():
        print("Dato erróneo")
        return False
    
    for key, value in database.items():
        if persona == value:
            print(f"Persona encontrada, clave: {key}\n{value}\n")
            return True
    print("Persona no encontrada")
    return False


persona = {"Primer Nombre": "Pablo","Segundo Nombre": "Diego", "Primer Apellido": "Ruiz", "Segundo Apellido": "Picasso"}
buscar_datos(persona, database)

persona = {"Primer Nombre": "Ale","Segundo Nombre": "Seba", "Primer Apellido": "Sanchez", "Segundo Apellido": "Castelino" }
buscar_datos(persona, database)

persona = {"Primer Nombre": "Nahuel","Segundo Nombre": "Ian", "Primer Apellido": "Galera", "Segundo Apellido": "Suarez"}
buscar_datos(persona, database)



