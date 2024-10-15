import unittest
from flask import json
from app import app


class TestSecurityAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_inyeccion_mongo(self):
        payload = json.dumps(
            {
                "nombre": {"$ne": "Test"},
                "edad": 3,
                "peso": 10.5,
            }
        )
        response = self.app.post(
            "/ualabis", headers={"Content-Type": "application/json"}, data=payload
        )
        self.assertEqual(response.status_code, 400) 

    def test_xss_proteccion(self):
        payload = json.dumps(
            {"nombre": "<script>alert('hack')</script>", "edad": 3, "peso": 10.5}
        )
        response = self.app.post(
            "/ualabis", headers={"Content-Type": "application/json"}, data=payload
        )
        self.assertEqual(response.status_code, 201)
        self.assertNotIn("<script>", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
