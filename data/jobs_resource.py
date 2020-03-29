from flask import jsonify
from flask_restful import abort, Resource
from data.Jobs import Jobs
from data import db_session
from data.reqparse import parser_jobs


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        abort(404, message=f'Работа {job_id} не найдена')


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify({'Jobs': jobs.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'Success': 'OK'})


class JobListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'Jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for item
                                 in jobs]})

    def post(self):
        arg = parser_jobs.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=arg['team_leader'],
            job=arg['job'],
            work_size=arg['work_size'],
            collaborators=arg['collaborators'],
            start_date=arg['start_date'],
            end_date=arg['end_date'],
            is_finished=arg['is_finished']
        )
