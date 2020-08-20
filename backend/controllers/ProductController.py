from repositories.ProductRepository import ProductRepository
from util.general import BaseRequestHanlder
from bson.json_util import dumps
import tornado

class Product(BaseRequestHanlder):        

    async def get(self):
        ProductObject = ProductRepository(self.settings["db"])
        ProductList = await ProductObject.list_products()
        self.write(ProductList)


    async def post(self):

        body = tornado.escape.json_decode(self.request.body)
        ProductObject = ProductRepository(self.settings["db"])
        ProductInsert = ProductObject.insert_product(body)
        self.write(ProductInsert)
        

    def put(self):
        pass

    def delete(self):
        pass
