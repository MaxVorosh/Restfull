from flask_restful import reqparse
from datetime import datetime

parser_user = reqparse.RequestParser()
parser_user.add_argument('surname', required=True, type=str)
parser_user.add_argument('name', required=True, type=str)
parser_user.add_argument('age', required=True, type=int)
parser_user.add_argument('position', required=True, type=str)
parser_user.add_argument('speciality', required=True, type=str)
parser_user.add_argument('address', required=True, type=str)
parser_user.add_argument('email', required=True, type=str)
parser_user.add_argument('hashed_password', required=True, type=str)

parser_jobs = reqparse.RequestParser()
parser_jobs.add_argument('team_leader', required=True, type=int)
parser_jobs.add_argument('job', required=True, type=str)
parser_jobs.add_argument('work_size', required=True, type=int)
parser_jobs.add_argument('collaborators', required=True, type=str)
parser_jobs.add_argument('start_date', required=True, type=datetime)
parser_jobs.add_argument('end_date', required=True, type=datetime)
parser_jobs.add_argument('is_finished', required=True, type=bool)
