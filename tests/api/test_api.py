""" Here I learned how to send API requests and verify response parameters """

import pytest
import requests


@pytest.mark.api
def test_fitst_request():
    response = requests.get("https://api.github.com/zen")
    print(f"\nResponse is: {response.text}")


@pytest.mark.api
def test_second_request():
    response = requests.get("https://api.github.com/users/defunkt")
    body = response.json()
    headers = response.headers

    assert body["name"] == "Chris Wanstrath", "Name does not equal to - Chris Wanstrath"
    assert response.status_code == 200, "Status code is not - 200"
    assert headers["Server"] == "GitHub.com" - "Server name is not - GitHub.com"


@pytest.mark.api
def test_status_code_request():
    response = requests.get("https://api.github.com/users/pavlo_lekhitskyi")

    assert response.status_code == 404, "Status code is not - 404"
