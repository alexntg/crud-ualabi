import unittest
import time
from app import app


class TestPerformanceAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_tiempo_respuesta_crear_ualabi(self):
        start_time = time.time()

        payload = {"nombre": "Fast Ualabi", "edad": 2, "peso": 9.5}
        response = self.app.post(
            "/ualabis", headers={"Content-Type": "application/json"}, json=payload
        )

        end_time = time.time()
        total_time = end_time - start_time

        self.assertLess(total_time, 1)
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
