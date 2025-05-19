from http.client import responses
from unittest import TestCase
from application import app
from application.database import session, Account, BaseModel, engine


class AuthTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)


    def test_login_page_exists(self):
        response = self.client.get("/auth/login")
        self.assertEqual(response.status_code, 200, "response != 200")
        self.assertIn("login", response.get_data(as_text=True), "incorrect html data")



    def test_registration_page_exists(self):
        response = self.client.get("/auth/registration")
        self.assertEqual(response.status_code, 200, "response != 200")
        self.assertIn("registration", response.get_data(as_text=True), "incorrect html data")

    def test_registration_form_submit(self):
        form_data = {
            "username": "Alex5",
            "password": "qwerty1234"
        }
        response = self.client.post("/auth/registration", data=form_data)
        self.assertEqual(response.status_code, 200, "invalid status code")
        self.assertIn("Success", response.get_data(as_text=True), "incorrect response")
        test_account_data = session.query(Account).where(Account.username==form_data["username"]).first()
        self.assertIsNotNone(test_account_data)


    def test_login_form_submit(self):
        test_account = Account(username="Andrew", password="87654321")
        session.add(test_account)
        session.commit()
        response = self.client.post("/auth/login", data={"username": test_account.username, "password": test_account.password})
        self.assertEqual(response.status_code, 200, "invalid status code")
        self.assertIn("Success", response.get_data(as_text=True), "incorrect response")



