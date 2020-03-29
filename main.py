from flask import Flask
from flask_restful import Api


from data import db_session, users_resource, jobs_resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/mars_explorer.db")
    api.add_resource(users_resource.UserListResource, '/api/v2/users')
    api.add_resource(users_resource.UserResource, '/api/v2/users/<int:user_id>')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
    api.add_resource(jobs_resource.JobListResource, '/api/v2/jobs')
    app.run()


if __name__ == '__main__':
    main()
