from bson.json_util import dumps
from util.general import PROJECT_BASE_FOLDER, validate_json_schema
from bson import ObjectId
from json import loads

class ProductRepository:

    def __init__(self, db):
        self.db = db

    async def list_products(self):
        products = self.db.products.find({})
        if not products:
            return dumps({})

        products = await products.to_list(length=10)
        return dumps(products)


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

            return dumps({"success": "ok"})
        else:
            return dumps({"error": str(validation)})

    async def list_by_id(self, id_product):
        try:        
            product_for_update = await self.db.products.find_one({
                "_id": ObjectId(id_product)
            })

            return dumps(product_for_update)
        except Exception:
            return dumps({"error": "produto não encontrado"})

    async def update_product(self, body):
        id_product = body["id"]

        name = body["name"]
        price = body["price"]
        validity = body["validity"]
        category = body["category"]

        try:
            self.db.products.update_one(
            { "_id": ObjectId(id_product)},
            {
                "$set": {
                    "name": name,
                    "price": price,
                    "validity": validity,
                    "category": category
                }
            })
            return dumps({"success": "ok"})
        except Exception:
            return dumps({"error": "falha ao atualizar"})

    async def remove_product(self, body):
        id_product = body["id"]

        # try:
        self.db.products.delete_one({
                "_id": ObjectId(id_product)
            })
        return dumps({"success": "ok"})
        # except Exception:
        #     return dumps({"error": "falha ao excluir"})
