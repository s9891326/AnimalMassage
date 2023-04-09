import unittest

from fastapi.testclient import TestClient

from animal_massage.web.example_api import app


class ExampleApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.t: TestClient = TestClient(app)

    def tearDown(self) -> None:
        self.t.close()

    def test_http_get_read_item(self):
        response = self.t.get("/items/7788").json()
        self.assertEqual(dict(item_id=7788), response)

    def test_http_read_user_item_with_parameters(self):
        response = self.t.get("/items_with_params/7788?needy=c8763&limit=10").json()
        self.assertEqual(
            dict(item_id="7788", needy="c8763", skip=0, limit=10), response
        )

    def test_http_post(self):
        response = self.t.post(
            "/items",
            json=dict(name="my name is Yi", description="hello", price=10.5, tax=0.5),
        ).json()
        self.assertEqual(
            dict(name="my name is Yi", description="hello", price=10.5, tax=0.5),
            response,
        )

    def test_http_post_with_response_model(self):
        response = self.t.post(
            "/user",
            json=dict(
                username="Yi", password="123456", email="123@gmail.com", full_name="H"
            ),
        ).json()
        self.assertEqual(
            dict(username="Yi", email="123@gmail.com", full_name="H"), response
        )

    def test_http_patch(self):
        item_id = "foo"
        first_response = self.t.get(f"/items2/{item_id}").json()
        self.assertEqual(
            dict(name="Foo", description=None, price=50.2, tax=10.5, tags=[]),
            first_response,
        )

        patch_response = self.t.patch(
            f"/items2/{item_id}",
            json=dict(
                name="Foo2",
                description="patch_description",
                price=10.2,
                tax=8.7,
                tags=["a", "b"],
            ),
        ).json()
        self.assertEqual(
            dict(
                name="Foo2",
                description="patch_description",
                price=10.2,
                tax=8.7,
                tags=["a", "b"],
            ),
            patch_response,
        )

        second_response = self.t.get(f"/items2/{item_id}").json()
        self.assertEqual(
            dict(
                name="Foo2",
                description="patch_description",
                price=10.2,
                tax=8.7,
                tags=["a", "b"],
            ),
            second_response,
        )

    def test_http_delete(self):
        item_id = "bar"
        response = self.t.delete(f"/items2/{item_id}").json()
        self.assertTrue(response)

        try:
            get_response = self.t.get(f"/items2/{item_id}").json()
        except KeyError as e:
            self.assertEqual(item_id, e.args[0])
