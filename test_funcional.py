import unittest
from flask import json
from app import app, collection


class TestFunctionalAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_funcionalidad_basica(self):
        payload = json.dumps({"nombre": "Funcional Ualabi", "edad": 4, "peso": 12.5})
        response = self.app.post(
            "/ualabis", headers={"Content-Type": "application/json"}, data=payload
        )
        self.assertEqual(response.status_code, 201)

        response = self.app.get("/ualabis")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Funcional Ualabi", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
