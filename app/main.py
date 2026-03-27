from fastapi import FastAPI, HTTPException, Depends
from typing import List
from .schemas import MenuItem, OrderCreate, OrderResponse
from .repository import MenuRepository, OrderRepository

app = FastAPI(title="C&C Food Hause API")

# Inyección de dependencias
menu_repo = MenuRepository()
order_repo = OrderRepository(menu_repo)

@app.get("/menu", response_model=List[MenuItem])
def listar_menu():
    return menu_repo.get_all()

@app.post("/pedidos", response_model=OrderResponse, status_code=201)
def crear_pedido(pedido: OrderCreate):
    try:
        return order_repo.create(pedido)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/pedidos/{pedido_id}", response_model=OrderResponse)
def consultar_pedido(pedido_id: int):
    pedido = order_repo.get_by_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    return pedido