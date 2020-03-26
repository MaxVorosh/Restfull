from flask import Flask
from flask_restful import Api


from data import db_session, users_resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/mars_explorer.db")
    # для списка объектов
    api.add_resource(users_resource.UserListResource, '/api/v2/users')

    # для одного объекта
    api.add_resource(users_resource.UserResource, '/api/v2/users/<int:user_id>')

    app.run()


if __name__ == '__main__':
    main()
