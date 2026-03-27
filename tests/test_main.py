from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_menu():
    # Arrange & Act
    response = client.get("/menu")
    # Assert
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_crear_pedido_aaa():
    # Arrange
    payload = {"items": [{"menu_item_id": 1, "quantity": 2}]} # 18000 * 2 = 36000
    # Act
    response = client.post("/pedidos", json=payload)
    # Assert
    assert response.status_code == 201
    assert response.json()["total"] == 36000.0