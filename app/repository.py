from typing import List, Optional, Dict
from schemas import MenuItem, Category, OrderCreate, OrderResponse, OrderItemResponse

class MenuRepository:
    def __init__(self):
        self._db: Dict[int, MenuItem] = {
            1: MenuItem(id=1, name="Burrito Clásico", description="Frijol, queso, carne asada y guacamole", price=18000.0, category=Category.BURRITO),
            2: MenuItem(id=2, name="Tacos al Pastor", description="Orden de 3 tacos con piña y cebolla", price=15000.0, category=Category.TACO),
            3: MenuItem(id=3, name="Agua de Jamaica", description="Refrescante agua natural casera", price=4500.0, category=Category.BEBIDA),
        }

    def get_all(self) -> List[MenuItem]:
        return list(self._db.values())

    def get_by_id(self, item_id: int) -> Optional[MenuItem]:
        return self._db.get(item_id)

class OrderRepository:
    def __init__(self, menu_repo: MenuRepository):
        self._db: Dict[int, OrderResponse] = {}
        self._current_id = 1
        self._menu_repo = menu_repo

    def create(self, order_create: OrderCreate) -> OrderResponse:
        order_items_response = []
        total = 0.0
        for item in order_create.items:
            menu_item = self._menu_repo.get_by_id(item.menu_item_id)
            if not menu_item:
                raise ValueError(f"ID {item.menu_item_id} no existe")
            subtotal = menu_item.price * item.quantity
            total += subtotal
            order_items_response.append(OrderItemResponse(menu_item=menu_item, quantity=item.quantity, subtotal=subtotal))
        
        order = OrderResponse(id=self._current_id, items=order_items_response, total=total, status="Preparando")
        self._db[self._current_id] = order
        self._current_id += 1
        return order

    def get_by_id(self, order_id: int) -> Optional[OrderResponse]:
        return self._db.get(order_id)