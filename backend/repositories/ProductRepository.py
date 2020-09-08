from util.general import PROJECT_BASE_FOLDER, validate_json_schema, return_pretty_message
from json import loads
from util.mongo import MongoFunctions


class ProductRepository:

    def __init__(self, db):
        self.db = db
        self.mongoObject = MongoFunctions(self.db, self.db.products)

    async def list_products(self):
        products = await self.mongoObject.list_data()
        return return_pretty_message(products)

    async def insert_product(self, body):
        schema_for_validate = f"{PROJECT_BASE_FOLDER}/schemas/products/post_product.json"

        validation = validate_json_schema(schema_for_validate, body)

        try:
            if validation is None:
                new_product = {
                    "name": body["name"],
                    "price": body["price"],
                    "validity": body["validity"],
                    "category": body["category"]
                }

                await self.mongoObject.insert_data(new_product)
            return return_pretty_message(success="ok")
        except Exception:
            return return_pretty_message(error=str(validation))

    async def list_by_id(self, id_product):
        try:
            product = await self.mongoObject.list_one(id_product)
            return return_pretty_message(product)
        except Exception:
            return return_pretty_message(error="produto nao encontrado")

    async def update_product(self, body):
        id_product = body["id"]

        data = {
            "id": id_product,
            "name": body["name"],
            "price": body["price"],
            "validity": body["validity"],
            "category": body["category"]
        }

        product = await self.list_by_id(id_product)

        try:
            if not "_id" in product:
                return return_pretty_message(error=f"produto id:{id_product} não encontrado")
            else:
                self.mongoObject.update_data(**data)
                return return_pretty_message(success="ok", id_atualizado=id_product)
        except Exception:
            return return_pretty_message(error="falha ao atualizar")

    async def remove_product(self, body):
        id_product = body["id"]
        product = await self.list_by_id(id_product)
        product_object = loads(product)

        try:
            if not "_id" in product_object:
                return return_pretty_message(error=f"produto id:{id_product} não encontrado")
            else:
                await self.mongoObject.delete_data(id_product)
                return return_pretty_message(success="ok", id_excluido=id_product)
        except Exception:
            return return_pretty_message(error="falha ao excluir")
