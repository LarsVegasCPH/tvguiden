from src import tvguiden
import requests

def test_baseurl():
    response = requests.head(url=tvguiden._baseURL)
    assert response.ok


