import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # cria cliente de teste do Flask
        self.client = app.test_client()
        self.client.testing = True

    def test_home_status_code(self):
        """Página inicial deve retornar 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_sobre_status_code(self):
        """Página /sobre deve retornar 200"""
        response = self.client.get("/sobre")
        self.assertEqual(response.status_code, 200)

    def test_post_form(self):
        """Envio de formulário deve retornar nome no HTML"""
        response = self.client.post("/", data={"nome": "Pedro"})
        self.assertIn(b"Pedro", response.data)

if __name__ == "__main__":
    unittest.main()
