from starlette.testclient import TestClient

from main import app

client = TestClient(app)
class TestCalculationEndpoint:

    def test_return_sum_post(self, test_client):
        test_data = {
            "first_val": 10,
            "second_val": 8
        }

        response = test_client.post("/sum/", json=test_data)
        assert response.status_code == 200
        assert response.json() == 18

    def test_return_difference(self, test_client):
        test_data = {
            "first_val": 100,
            "second_val": 80
        }

        response = test_client.post("/subtract/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 20


    def test_return_product(self, test_client):
        test_data = {
            "first_val": 5,
            "second_val": 6
        }

        response = test_client.post("/multiplication/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 30

    def test_return_division(self, test_client):
        test_data = {
            "first_val": 30,
            "second_val": 6
        }

        response = test_client.post("/division/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 5




