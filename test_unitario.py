import unittest
from flask import json
from app import app, collection

class TestUalabiAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_crear_ualabi_exito(self):
        payload = json.dumps({
            "nombre": "Test Ualabi",
            "edad": 3,
            "peso": 15.5
        })
        response = self.app.post('/ualabis', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Ualabi creado', response.get_data(as_text=True))

    def test_crear_ualabi_error(self):
        payload = json.dumps({
            "nombre": "Test Ualabi",
            "edad": 3

        })
        response = self.app.post('/ualabis', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Faltan datos necesarios', response.get_data(as_text=True))

    def test_leer_ualabis(self):
        response = self.app.get('/ualabis')
        self.assertEqual(response.status_code, 200)
        self.assertIn('nombre', response.get_data(as_text=True))

    def test_leer_ualabi_no_existe(self):
        response = self.app.get('/ualabis/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Ualabi no encontrado', response.get_data(as_text=True))

    def tearDown(self): 
        collection.delete_many({}) 

if __name__ == '__main__':
    unittest.main()
