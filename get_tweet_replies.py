from TwitterAPI import TwitterAPI, TwitterRequestError, TwitterConnectionError
import credentials

TWEET_ID = '1397528226256334850'

try:
    api = TwitterAPI(
        consumer_key=credentials.API_KEY, 
        consumer_secret=credentials.API_SECRET_KEY, 
        auth_type='oAuth2', 
        api_version='2')


    r = api.request('tweets/search/all', {
	    'query':f'conversation_id:{TWEET_ID}', 
	    'tweet.fields':'author_id,in_reply_to_user_id',
	    'expansions':'author_id'})

    for item in r:
	    print(item)

    print(r.get_quota())
    
except TwitterRequestError as e:
    print(e.status_code)
    for msg in iter(e):
        print(msg)

except TwitterConnectionError as e:
    print(e)

except Exception as e:
    print(e)