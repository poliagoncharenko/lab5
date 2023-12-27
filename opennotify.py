import requests
import json

req_iss = "http://api.open-notify.org/iss-now.json"
response_iss = requests.get(req_iss).json()

position_E = response_iss['iss_position']['longitude']
position_N = response_iss['iss_position']['latitude']

print(f'''
        Текущее местоположение Международной космической станции:
        {position_N}° N {position_E}° E
        ''')

req_in_space = "http://api.open-notify.org/astros.json"
response_in_space = requests.get(req_in_space).json()

people_in_space = response_in_space['number']
peoples = response_in_space['people']

print(f'''На данный момент в космосе {people_in_space} человек''')

for person in peoples:
        print('    ' + person['name'])

