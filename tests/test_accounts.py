
import unittest

from service import create_app
from service.routes import reset_accounts


class AccountsApiTestCase(unittest.TestCase):
    def setUp(self):
        reset_accounts()
        self.app = create_app({"TESTING": True})
        self.client = self.app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_create_and_read(self):
        response = self.client.post(
            "/accounts",
            json={"name": "Jane", "email": "jane@example.com"}
        )
        self.assertEqual(response.status_code, 201)
        account_id = response.get_json()["id"]

        read = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(read.status_code, 200)
        self.assertEqual(read.get_json()["name"], "Jane")

    def test_list_accounts(self):
        self.client.post(
            "/accounts",
            json={"name": "Jane", "email": "jane@example.com"}
        )
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_update(self):
        created = self.client.post(
            "/accounts",
            json={"name": "Jane", "email": "jane@example.com"}
        ).get_json()

        response = self.client.put(
            f"/accounts/{created['id']}",
            json={"name": "Janet"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Janet")

    def test_delete(self):
        created = self.client.post(
            "/accounts",
            json={"name": "Jane", "email": "jane@example.com"}
        ).get_json()

        response = self.client.delete(
            f"/accounts/{created['id']}"
        )
        self.assertEqual(response.status_code, 204)

        missing = self.client.get(f"/accounts/{created['id']}")
        self.assertEqual(missing.status_code, 404)

    def test_missing_required_fields(self):
        response = self.client.post(
            "/accounts",
            json={"name": "Jane"}
        )
        self.assertEqual(response.status_code, 400)

    def test_not_found(self):
        response = self.client.get("/accounts/999")
        self.assertEqual(response.status_code, 404)

    def test_security_header(self):
        response = self.client.get("/health")
        self.assertIn("Content-Security-Policy", response.headers)


if __name__ == "__main__":
    unittest.main()
