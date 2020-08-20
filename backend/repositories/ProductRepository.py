from bson.json_util import dumps
from util.general import PROJECT_BASE_FOLDER, validate_json_schema

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

            return dumps({"success": "Ok!"})
        else:
            return dumps({"error": str(validation)})

