import requests, json
from pprint import pp
from datetime import datetime

def print_pretty(response):
    pp(f'Response URL: {response.url}')
    pp(f'Response Status Code: {response.status_code}')
    pp(f'Response Reason: {response.reason}')
    pp(f'Response Text:')
    pp(response.text)
    pp(f'Response Json Object:')
    pp(response.json())


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'

#GET
pet_id = 9223372036854597073
# response = requests.get(f'{BASE_URL_PETSTORE}/pet/{pet_id}')
# #response = requests.get(f'{BASE_URL_PETSTORE}/pet/9223372036854596000')
#
# pp('Get example')
# print_pretty(response)


new_pet_data = {
    'name': 'Barbos',
    'status': 'available'
}
new_pet_data['name'] = f'Barbos {str(datetime.now())}'

pet_response_before_change = requests.get(f'{BASE_URL_PETSTORE}/pet/{pet_id}')

# change pet via POST request
response = requests.post(f'{BASE_URL_PETSTORE}/pet/{pet_id}', data=new_pet_data)


# get changed pet_id from response
changed_pet_id = json.loads(response.text)['message']

# get pet again for verification purposes
pet_response_after_change = requests.get(f'{BASE_URL_PETSTORE}/pet/{changed_pet_id}')
#print_pretty(response)

pet_response_after_change = requests.get(f'{BASE_URL_PETSTORE}/pet/{pet_id}')

assert new_pet_data['name'] == pet_response_after_change.json()['name']
#response = requests.get(f'{BASE_URL_PETSTORE}/pet/findByStatus?status=available')
#print_pretty(response)

