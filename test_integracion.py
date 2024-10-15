import unittest
from flask import json
from app import app, collection
from bson.objectid import ObjectId


class TestIntegrationAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_flujo_completo_ualabi(self):
        payload = json.dumps({"nombre": "Test Ualabi", "edad": 2, "peso": 14.3})
        create_response = self.app.post(
            "/ualabis", headers={"Content-Type": "application/json"}, data=payload
        )
        self.assertEqual(create_response.status_code, 201)

        ualabi_id = json.loads(create_response.data)["id"]

        read_response = self.app.get(f"/ualabis/{ualabi_id}")
        self.assertEqual(read_response.status_code, 200)
        self.assertIn("Test Ualabi", read_response.get_data(as_text=True))

        update_payload = json.dumps(
            {"nombre": "Updated Ualabi", "edad": 3, "peso": 16.1}
        )
        update_response = self.app.put(
            f"/ualabis/{ualabi_id}",
            headers={"Content-Type": "application/json"},
            data=update_payload,
        )
        self.assertEqual(update_response.status_code, 200)
        self.assertIn("Ualabi actualizado", update_response.get_data(as_text=True))

        delete_response = self.app.delete(f"/ualabis/{ualabi_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn("Ualabi eliminado", delete_response.get_data(as_text=True))

    def tearDown(self):
        collection.delete_many({})


if __name__ == "__main__":
    unittest.main()
