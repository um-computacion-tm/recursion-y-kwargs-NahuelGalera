import unittest

database = {"Persona_1": {"Primer Nombre": "Pablo","Segundo Nombre": "Diego", "Primer Apellido": "Ruiz", "Segundo Apellido": "Picasso" },
            "Persona_2": {"Primer Nombre": "Ale","Segundo Nombre": "Seba", "Primer Apellido": "Sanchez", "Segundo Apellido": "Castelino" },
            "Persona_3": {"Primer Nombre": "Nahuel","Segundo Nombre": "Ian", "Primer Apellido": "Galera", "Segundo Apellido": "Suarez"}
            }


def buscar_datos(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, database):
    persona = {"Primer Nombre": primer_nombre, "Segundo Nombre": segundo_nombre, "Primer Apellido": primer_apellido, "Segundo Apellido": segundo_apellido}
    
    if "" in persona.values():
        return False
    
    for key, value in database.items():
        if persona == value:
            return True
    return False

class TestBuscarPersona(unittest.TestCase):
    def test_0(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database)
        self.assertEqual(resultado, True)
    def test_1(self):
        resultado = buscar_datos("a", "b", "c", "d", database)
        self.assertEqual(resultado, False)
    def test_2(self):
        resultado = buscar_datos("Nahuel", "Ian", "Galera", "Suarez", database)
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()









