from repositories.ProductRepository import ProductRepository
from util.general import BaseRequestHanlder
from bson.json_util import dumps
import tornado


class Product(BaseRequestHanlder):

    def productRepository(self):
        return ProductRepository(self.settings["db"])

    async def get(self):
        ProductList = await self.productRepository().list_products()
        self.write(ProductList)

    async def post(self):
        body = tornado.escape.json_decode(self.request.body)
        ProductInsert = await self.productRepository().insert_product(body)
        self.write(ProductInsert)

    async def put(self):
        body = tornado.escape.json_decode(self.request.body)
        ProductUpdate = await self.productRepository().update_product(body)
        self.write(ProductUpdate)

    async def delete(self):
        body = tornado.escape.json_decode(self.request.body)
        ProductDelete = await self.productRepository().remove_product(body)
        self.write(ProductDelete)
