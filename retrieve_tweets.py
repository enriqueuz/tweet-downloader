import credentials
import tweepy

def retrieve_tweets(query, tweets_number):
    auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    query = query.strip().lower()
    filename = query.replace(" ", "_") + '.txt'

    id = None
    count = 0
    while count <= tweets_number:
        tweets = api.search(q=query, lang='es', tweet_mode='extended', max_id=id)

        for tweet in tweets:
            if tweet.full_text.startswith('RT'):
                count += 1
                continue
            
            f = open(filename, 'a', encoding='utf-8')
            f.write(tweet.full_text + '\n')
            count += 1
            f.close
        
        id = tweet.id
        print(count)

if __name__ == '__main__':
    query = input("Type a hashtag, word or phrase you would like like to "
    "retrieve tweets from: ")
    tweets_number = int(input("Enter the quantity of tweets you want to download "
    "(max 3000): "))
    retrieve_tweets(query, tweets_number)