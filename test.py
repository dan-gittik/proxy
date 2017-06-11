import requests

import proxy


def test_proxy():
    with proxy.tor_proxy('ru', 7000):
        response = requests.get('http://ip-api.com/json')
        assert response.json()['country'] == 'Russia'
