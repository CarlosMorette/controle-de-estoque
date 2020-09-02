import tornado.web
from pathlib import Path
from jsonschema import validate, exceptions
from json import load, loads
from bson.json_util import dumps


class AppException(tornado.web.HTTPError):
    pass


class BaseRequestHanlder(tornado.web.RequestHandler):
    def cors_allowed_methods(self):
        return ["GET", "POST", "PUT", "PATCH", "DELETE"]

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods",
                        ", ".join(self.cors_allowed_methods()))

    def post(self):
        self.write('some post')

    def get(self):
        self.write('some get')

    def put(self):
        self.write('some put')

    def delete(self):
        self.write('some delete')

    def options(self):
        self.set_status(204)
        self.finish()


def get_base_project_folder():
    cwd = Path.cwd()
    while cwd.name != "backend":
        cwd = cwd.parent
    return cwd


PROJECT_BASE_FOLDER = get_base_project_folder()


def validate_json_schema(schema, body):
    with open(schema) as schema_file:
        try:
            return validate(body, load(schema_file))
        except exceptions.ValidationError as error:
            return AppException(400, log_message=error.message)

def return_pretty_message(array=None, **kwargs):
    if not array:
        return dumps(kwargs)
    elif not kwargs:
        return dumps(array)
    
