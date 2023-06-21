from fastapi.testclient import TestClient
from fastapi import status


def test_converter(client: TestClient):
    response = client.get('/0')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'ok',
        'result': 32,
    }
