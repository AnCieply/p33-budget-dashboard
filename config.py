from os import urandom, environ, path


# Root folder of the project
base_directory = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = urandom(24)
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")\
        or "sqlite:///" + path.join(base_directory, "app.db")

