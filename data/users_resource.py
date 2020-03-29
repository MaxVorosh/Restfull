from flask import jsonify
from flask_restful import abort, Resource
from data import db_session
from data.User import User
from data.reqparse import parser_user


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f'Пользователь {user_id} не найден')


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'Users': users.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'Success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'Users': [
            item.to_dict(
                only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password')) for
            item in
            users]})

    def post(self):
        arg = parser_user.parse_args()
        session = db_session.create_session()
        user = User(
            name=arg['name'],
            surname=arg['surname'],
            age=arg['age'],
            position=arg['position'],
            speciality=arg['speciality'],
            address=arg['address'],
            email=arg['email'],
            hashed_password=arg['hashed_password']
        )
        session.add(user)
        session.commit()
        return jsonify({'Success': 'OK'})
