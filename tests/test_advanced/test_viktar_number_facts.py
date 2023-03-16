from unittest.mock import MagicMock

import pytest
import requests
from pytest_mock import mocker

from number_facts import get_number_fact


class MockedResponse:
    def __init__(self, json_body, status_code):
        self.json_body = json_body
        self.status_code = status_code
        self.nasty = "nasty"

    def json(self):
        return self.json_body

    def foo(self):
        return "viktar"


# mock_response = MagicMock()

class TestNumberFacts:

    @pytest.mark.parametrize("number, response_text",
                             [(1, "1 is the number of dimensions of a line."),
                              (5, "5 is the number of interlocked rings in the "
                                  "symbol of the Olympic Games, representing the "
                                  "number of inhabited continents represented by the Olympians "
                                  "(counting North America and South America as one continent)."),
                              (10, "10 is the number of letters used in the traditional "
                                   "Snellen chart."),
                              ])
    def test_get_number_fact(self, monkeypatch, number, response_text):

        response_model = {"text": response_text}

        def mock_get(*args, **kwargs):
            return MockedResponse(response_model, 200)

        # monkeypatch.setattr(requests, "get", mock_get)
        monkeypatch.setattr("requests.get", mock_get)

        url = f"http://numbersapi.com/{number}?json"
        responce = requests.get(url)
        json_response = responce.json()

        assert responce.status_code == 200
        # assert responce["text"] == response_text
        assert json_response["text"] == response_text
        assert responce.foo() == "viktar"
        assert responce.nasty == "nasty"



class TestNumberFactsMagicMock:

    @pytest.mark.parametrize("number, response_text",
                             [(1, "1 is the number of dimensions of a line."),
                              (5, "5 is the number of interlocked rings in the "
                                  "symbol of the Olympic Games, representing the "
                                  "number of inhabited continents represented by the Olympians "
                                  "(counting North America and South America as one continent)."),
                              (10, "10 is the number of letters used in the traditional "
                                   "Snellen chart."),
                              ])
    def test_get_number_fact(self, mocker, monkeypatch, number, response_text):
        mock_get = MagicMock()
        # mock_get = mocker.Mock
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"text": response_text}
        mock_get.return_value.name = "viktar"
        mock_get.return_value.foo.return_value = "nasty"

        monkeypatch.setattr("requests.get", mock_get)

        url = f"http://numbersapi.com/{number}?json"
        response = requests.get(url)

        json_response = response.json()
        # print("-------mock_get------:", mock_get.__dict__)
        # print("-------response.status_code------:", response.status_code)

        assert response.status_code == 200
        assert json_response["text"] == response_text
        assert response.name == "viktar"
        assert response.foo() == "nasty"





