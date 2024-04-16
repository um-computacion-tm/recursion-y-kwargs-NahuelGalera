import unittest

database = {"Persona_1": {"Primer Nombre": "Pablo","Segundo Nombre": "Diego", "Primer Apellido": "Ruiz", "Segundo Apellido": "Picasso" },
            "Persona_2": {"Primer Nombre": "Ale","Segundo Nombre": "Seba", "Primer Apellido": "Sanchez", "Segundo Apellido": "Castelino" },
            "Persona_3": {"Primer Nombre": "Nahuel","Segundo Nombre": "Ian", "Primer Apellido": "Galera", "Segundo Apellido": "Suarez"}
            }

buscar_datos = [(("Pablo", "Diego", "Ruiz", "Picasso", database), True),
                (("a", "b", "c", "d", database), False),
                (("Padre", "Loco", "A", "B", database), False),
                (("Nahuel", "Ian", "Galera", "Suarez", database), True)]

def buscar_persona(*args, **kwargs):
    primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, database = args

    for _, datos in database.items():
        if (datos["Primer Nombre"] == primer_nombre and
            datos["Segundo Nombre"] == segundo_nombre and
            datos["Primer Apellido"] == primer_apellido and
            datos["Segundo Apellido"] == segundo_apellido):            
            return True
    return False

class TestBuscarPersona(unittest.TestCase):
    def test_buscar_persona(self):
        for args, resultado in buscar_datos:
            self.assertEqual(buscar_persona(*args), resultado)

if __name__ == '__main__':
    unittest.main()





