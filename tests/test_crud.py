import crud


def test_create_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}
    result = crud.create_product(product)
    assert result["name"] == "Laptop"


def test_read_products():
    # Create a product first
    product = {"id": 2, "name": "Mouse", "price": 50}
    crud.create_product(product)
    products = crud.read_products()
    assert isinstance(products, list)
    assert len(products) > 0


def test_update_product():
    # Create a product first
    product = {"id": 3, "name": "Keyboard", "price": 100}
    crud.create_product(product)
    updated = crud.update_product(3, {"price": 150})
    assert updated is not None
    assert updated["price"] == 150


def test_delete_product():
    # Create a product first
    product = {"id": 4, "name": "Monitor", "price": 200}
    crud.create_product(product)
    result = crud.delete_product(4)
    assert result is True
    # Verify it's deleted
    products = crud.read_products()
    assert not any(p.get("id") == 4 for p in products)
