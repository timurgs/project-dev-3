import requests


# response = requests.get('http://127.0.0.1:5000/advertisements/1').json()
# print(response)
#
#
# response = requests.post('http://localhost:5000/advertisements/',
#                          json={
#                             'title': 'Car',
#                             'description': 'brand: Toyota, color: Black'
#                          }).json()
# print(response)
#
#
# response = requests.post('http://localhost:5000/users/',
#                          json={
#                              'username': 'admin',
#                              'name': 'Adminchik',
#                              'email': 'admin@python.py',
#                              'password': 'sgdsSTAT4434FET32325'
#                          }).json()
# print(response)
#
#
# response = requests.delete('http://localhost:5000/advertisements/2').json()
# print(response)
#
#
# response = requests.patch('http://localhost:5000/advertisements/2',
#                           json={
#                               'title': 'Car',
#                               'description': 'brand: Toyota, color: Red',
#                           }).json()
# print(response)
#
#
# response = requests.post('http://localhost:5000/login/',
#                          json={
#                              'username': 'admin',
#                              'password': 'sgdsSTAT4434FET32325',
#                              'email': 'admin@python.py'
#                          }).json()
# print(response)


response = requests.post('http://localhost:5000/mail/',
                         json={
                             "user": "",
                             "password": ""
                         }).json()
print(response)
