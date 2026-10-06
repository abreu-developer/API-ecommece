import pytest # pyright: ignore[reportMissingImports]
from src.models.sqlite.settings.connection import SqliteConnectHandler
from .products_repository import ProductsRepository


conn_handler = SqliteConnectHandler()
conn = conn_handler.connect()

@pytest.mark.skip(reason="interaçao com o bd")
def test_insert_product():
    repo = ProductsRepository(conn)

    name = "cafe"
    price = 12.12
    quantity = 10

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason="interaçao com o bd")
def test_find_product():
    repo = ProductsRepository(conn)

    response = repo.find_product_by_name("cafe")

    assert response is not None
    assert response[1] == "cafe"
    assert response[2] == 12.12
    assert response[3] == 10
