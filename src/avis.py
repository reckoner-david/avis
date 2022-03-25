import json
import requests

# https://developer.avis.com/getting-started
# NOTE: All of the endpoints referenced on this website are executed in our staging or pre-prod environments.  
# They do not make live, usable reservations for customers. 
# When you're ready, please send us a note so we can get your application launched.
class avis:
    base_address = 'https://stage.abgapiservices.com'

    def __init__(self, id, secret):
        self._id = id
        self._secret = secret
        self.login()

    def login(self):
        req_headers = {
            'client_id': self._id,
            'client_secret': self._secret
        }
        req = requests.get('{}/oauth/token/v1'.format(self.base_address), headers=req_headers)
        login = json.loads(req.text)
        self._auth = "{} {}".format(login['token_type'], login['access_token'])
    
    def locations(self, country_code, keyword):
        req_headers = {
            'client_id': self._id,
            'authorization': self._auth
        }
        req = requests.get('{}/cars/locations/v1?country_code={}&keyword={}'.format(self.base_address, country_code, keyword), headers=req_headers)
        print(req.text)
    
    def availability(self):
        # "The pick-up location entered is Sold Out for the dates you have entered"
        req_headers = {
            'client_id': self._id,
            'authorization': self._auth
        }
        req_params = {
            'client_id': self._id,
            'authorization': self._auth,
            'brand': 'Avis',
            'age': '28',
            'country_code': 'ES',
            'pickup_date': '...',
            'pickup_location': '...', # Fetch code from locations
            'dropoff_date': '...',
            'dropoff_location': '...',
            'rate_code': 'G3', # No info about this
            'vehicle_class_code': 'A',
        }
        req = requests.get('{}/cars/catalog/v1/vehicles'.format(self.base_address), headers=req_headers, params=req_params)
        print(req.status_code)
        print(req.text)