import requests

SERVER = "http://localhost:8000"

def send_score(data):
    try:
        r = requests.post(SERVER + "/scores", json=data, timeout=3)
        return r.status_code == 201

    except requests.RequestException:

        return False     # serveris izslēgts
