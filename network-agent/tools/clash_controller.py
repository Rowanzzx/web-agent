import requests
from config import CLASH_API, CLASH_SECRET

headers = {
    "Authorization": f"Bearer {CLASH_SECRET}"
}

class ClashController:

    def get_proxies(self):
        r = requests.get(f"{CLASH_API}/proxies", headers=headers)
        return r.json()

    def switch_proxy(self, group, proxy):
        url = f"{CLASH_API}/proxies/{group}"

        data = {
            "name": proxy
        }

        r = requests.put(url, headers=headers, json=data)
        return r.text

    def test_delay(self, proxy_name):
        url = f"{CLASH_API}/proxies/{proxy_name}/delay"

        params = {
            "timeout": 5000,
            "url": "https://www.gstatic.com/generate_204"
        }

        r = requests.get(url, headers=headers, params=params)
        return r.json()
