from decouple import config

API_KEY=config('API_KEY')
API_SECRET_KEY=config('API_SECRET_KEY')
ACCESS_TOKEN=config('ACCESS_TOKEN', default=None)
ACCESS_TOKEN_SECRET=config('ACCESS_TOKEN_SECRET', default=None)
BEARER_TOKEN=config('BEARER_TOKEN', default=None)