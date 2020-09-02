from util.general import PROJECT_BASE_FOLDER, validate_json_schema, return_pretty_message
from bson import ObjectId
from json import loads


class ProductRepository:

    def __init__(self, db):
        self.db = db

    async def list_products(self):
        products = self.db.products.find({})
        if not products:
            return return_pretty_message({})

        products = await products.to_list(length=10)
        return return_pretty_message(products)

    def insert_product(self, body):
        schema_for_validate = f"{PROJECT_BASE_FOLDER}/schemas/products/post_product.json"

        validation = validate_json_schema(schema_for_validate, body)

        if validation is None:
            new_product = {
                "name": body["name"],
                "price": body["price"],
                "validity": body["validity"],
                "category": body["category"]
            }

            self.db.products.insert_one(new_product)

            return return_pretty_message(success="ok")
        else:
            return return_pretty_message(error=str(validation))

    async def list_by_id(self, id_product):
        try:
            product = await self.db.products.find_one({
                "_id": ObjectId(id_product)
            })
            return return_pretty_message(product)
        except Exception:
            return return_pretty_message(error="produto nao encontrado")

    async def update_product(self, body):
        id_product = body["id"]

        name = body["name"]
        price = body["price"]
        validity = body["validity"]
        category = body["category"]

        product = await self.list_by_id(id_product)

        try:
            if not "_id" in product:
                return return_pretty_message(error=f"produto id:{id_product} não encontrado")
            else:
                self.db.products.update_one(
                    {"_id": ObjectId(id_product)},
                    {
                        "$set": {
                            "name": name,
                            "price": price,
                            "validity": validity,
                            "category": category
                        }
                    })
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
                self.db.products.delete_one({
                    "_id": ObjectId(id_product)
                })

            return return_pretty_message(success="ok", id_excluido=id_product)
        except Exception:
            return return_pretty_message(error="falha ao excluir")
