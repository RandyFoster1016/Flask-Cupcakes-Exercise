from unittest import TestCase

from app import app
from models import db, Cupcake

app.config['SQLALCHEMY_DATABASE_URL'] = 'posgtresql://cupcakes_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

db.drop_all()
db.create_all()

CUPCAKE_DATA = {
    "flavor": "TestFlavor",
    "size": "TestSize",
    "rating": 5,
    "image": "http://test.com/cupcake.jpg"
}

CUPCAKE_DATA_2 = {
    "flavor": "TestFlavor2",
    "size": "TestSize2",
    "rating": 10,
    "image": "http://test.com/cupcake2.jpg"
}

class CupcakeViewsTestCase(TestCase):
    """Test for views of API."""

    def setUp(self):
        """Makes demo data."""

        Cupcake.query.delete()

        cupcake = Cupcake(**CUPCAKE_DATA)
        db.session.add(cupcake)
        db.session.commit()

        self.cupcake = cupcake

    def tearDown(self):
        """Clean up fouled transactions."""

        db.sessions.rollback()

    def test_list_cupcake(self):
        with app.test_client() as client:
            resp= client.get("/api/cupcakes")

            self.assertEqual(resp.status_code, 200)

            data = resp.json
            self.assertEqual(data, {
                "cupcakes": [
                {
                    "id": self.cupcate.id,
                    "flavor": "TestFlavor",
                    "size": "TestSize",
                    "rating": 5,
                    "image": "http://test.com/cupcake.jpg"
                }
                ]
            })

def test_get_cupcake(self):
    with app.test_client() as client:
        url = f"/api/cupcakes/{self.cupcake.id}"
        resp = client.get(url)

        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertEqual(data, {
            "cupcake": {
                "id": self.cupcake.id,
                "flavor": "TestFlavor",
                "size": "TestSize",
                "rating": 5, 
                "image": "http://test.com/cupcake.jpg"
            }
        })    

def test_get_cupcake_missing(self):
    with app.test_client() as client:
        url = f"/api/cupcakes/99999"
        resp = client.get(url)

        self.assertequal(resp.status_code, 404)

def test_create_cupcake(self):
    with app.test_client() as client:
        url = "/api/cupcakes"
        resp = client.post(url, json=CUPCAKE_DATA_2)

        self.assertEqual(resp.staus_code, 201)

        data = resp.json

        self.assertIsInstance(data['cupcake']['id'], int)
        del data['cupcake']['id']

        self.assertEqual(data, {
            "cupcake": {
                "flavor": "TestFlavor2",
                "size": "TestFlavor2",
                "rating": 10,
                "image": "http://test.com/cupcake2.jpg"
            }
        })

        self.assertEqual(Cupcake.query.count(), 1)

def test_update_cupcake_missing(self):
    with app.test_client() as client:
        url = f"/api/cupcakes/99999"
        resp = client.patch(url, json=CUPCAKE_DATA_2)

        self.assertEqual(resp.status_code, 404)

def test_delete_cupcake(self):
    with app.test_client()as client:
        url = f"/api/cupcakes/{self.cupcake.id}"
        resp = client.delete(url)

        self.assertEqual(resp.status_code, 200)

        data = resp.json
        self.assertEqual(Cupcake.query.count(),0)

def test_delete_cupcake_missing(self):
    with app.test_client() as client:
        url = f"/api/cupcakes/99999"
        resp = client.delete(url)

        self.assertEqual(resp.status_code, 404)

