from requests import get, post, delete
from datetime import datetime

print(get('http://localhost:5000/api/v2/jobs').json())  # База изначально пуста
print(get('http://localhost:5000/api/v2/jobs/1').json())
print(post('http://localhost:5000/api/v2/jobs', json={
    'team_leader': 1,
    'job': 'Nothing',
    'work_size': 15,
    'collaborators': '',
    'start_date': datetime(2020, 3, 29, 19, 20, 59),
    'end_date': datetime(2020, 3, 30, 10, 20, 59),
    'is_finished': True,
}).json())
print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/1').json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())
print(delete('http://localhost:5000/api/v2/jobs/1000000').json())  # Такого нет
print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/1').json())
