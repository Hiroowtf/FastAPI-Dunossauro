from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_dunossauro.app import app


def test_read_root_should_return_OK_and_hello_world():
    client = TestClient(app)  # Arrange (organização)

    response = client.get("/")  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Olar, Mundo"}
