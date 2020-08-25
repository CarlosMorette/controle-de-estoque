import motor
import json
import tornado.ioloop
import tornado.web
from controllers.ProductController import Product


def make_app(DB):
    return tornado.web.Application([
        (r"/produto", Product),
    ],
        db=DB.dev,
        autoreload=True
    )


if __name__ == "__main__":

    with open("config.json") as configuration_file:
        string_connection = json.load(configuration_file)["DB"]
        db = motor.motor_tornado.MotorClient(string_connection)
        print("Iniciou")
        app = make_app(db)
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()
