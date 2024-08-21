# test_inventario.py
import pytest
from inventario import Inventario

@pytest.fixture
def inventario():
    return Inventario()

def test_agregar_producto(inventario):
    inventario.agregar_producto("Laptop", 10, 1200.00)
    assert inventario.buscar_producto("Laptop") == {'cantidad': 10, 'precio': 1200.00}

def test_agregar_producto_existente(inventario):
    inventario.agregar_producto("Laptop", 10, 1200.00)
    with pytest.raises(ValueError, match="El producto ya existe en el inventario."):
        inventario.agregar_producto("Laptop", 5, 1150.00)

def test_actualizar_stock(inventario):
    inventario.agregar_producto("Laptop", 10, 1200.00)
    inventario.actualizar_stock("Laptop", 15)
    assert inventario.buscar_producto("Laptop") == {'cantidad': 15, 'precio': 1200.00}

def test_actualizar_stock_producto_no_existe(inventario):
    with pytest.raises(KeyError, match="El producto no existe en el inventario."):
        inventario.actualizar_stock("Tablet", 5)

def test_eliminar_producto(inventario):
    inventario.agregar_producto("Laptop", 10, 1200.00)
    inventario.eliminar_producto("Laptop")
    assert inventario.buscar_producto("Laptop") is None

def test_eliminar_producto_no_existe(inventario):
    with pytest.raises(KeyError, match="El producto no existe en el inventario."):
        inventario.eliminar_producto("Tablet")

def test_buscar_producto_no_existe(inventario):
    assert inventario.buscar_producto("Tablet") is None
