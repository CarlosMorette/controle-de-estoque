import tornado.web
from pathlib import Path
from jsonschema import validate, exceptions
from json import load


class AppException(tornado.web.HTTPError):
    pass


class BaseRequestHanlder(tornado.web.RequestHandler):
    def cors_allowed_methods(self):
        return ["GET", "POST", "PUT", "DELETE"]

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origins", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods",
                        ", ".join(self.cors_allowed_methods()))


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
