from src.models.sqlite.repository.interfaces.products_repository import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class ProductCreate:
    def __init__(self,
        redis_repo: RedisRepositoryInterface,
        sqlite_repo: ProductsRepositoryInterface
        ) -> None:

        self.__redis_repo = redis_repo
        self.__sqlite_repo = sqlite_repo


    def create(self, http_request: HttpRequest ) -> HttpResponse:
        body = http_request.body

        name = body.get("name")
        price = body.get("price")
        quantity = body.get("quantity")

        self.insert_product_in_sql(name,price,quantity)
        self.insert_in_cache(name,price,quantity)

        return self.__format_response()


    def insert_product_in_sql(self, name: str, price: float, quantity: int) -> None:
        self.__sqlite_repo.insert_product(name,price,quantity)

    def insert_in_cache(self, name: str, price: float, quantity: int ) -> None:
        product_key = name
        value = f"{price},{quantity}"
        self.__redis_repo.insert_ex(product_key,value,ex=60)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "type": "PRODUCT",
                "count": 1,
                "message": "created"
            }
        )
