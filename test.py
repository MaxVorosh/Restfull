from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())  # База изначально пуста
print(get('http://localhost:5000/api/v2/users/1').json())
print(post('http://localhost:5000/api/v2/users', json={
    'name': 'Max',
    'surname': 'Voroshilov',
    'age': 15,
    'position': 'No',
    'speciality': 'Student',
    'address': 'Kostroma',
    'email': 'MaxVor@mail.ru',
    'hashed_password': '121211221'
}).json())
print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
print(delete('http://localhost:5000/api/v2/users/1').json())
print(delete('http://localhost:5000/api/v2/users/1000000').json())  # Такого нет
print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
