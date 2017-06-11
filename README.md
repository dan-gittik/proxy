# Proxy

Context managers to route Python via proxies, or specifically via TOR.

```python
import requests

from proxy import tor_proxy

with tor_proxy('ru', port=7000):
    response = requests.get('http://ip-api.com/json')
    country  = response.json()['country']
    assert country == 'Russia'
```
