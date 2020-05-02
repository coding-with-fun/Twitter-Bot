import tweepy, time

print("This is my twitter bot")

CONSUMER_KEY = '(API key)'
CONSUMER_SECRET = '(API secret key)'

ACCESS_KEY = '(Access token)'
ACCESS_SECRET = '(Access token secret)'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    # The example is already added in the last_seen_id.txt file.

    # Get last seen ID
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id

        # Overwrite last seen ID in txt file
        store_last_seen_id(last_seen_id, FILE_NAME)

        if 'hello' in mention.full_text.lower():
            print('found hello!', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hello @' + mention.user.screen_name
                               , mention.id)

        elif '#hello' in mention.full_text.lower():
            print('found #hello!', flush=True)
            print('responding back...', flush=True)
            api.update_status('#Hello @' + mention.user.screen_name
                               , mention.id)

        elif 'hey' in mention.full_text.lower():
            print('found hey!', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hey @' + mention.user.screen_name
                               , mention.id)

        elif '#hey' in mention.full_text.lower():
            print('found #hey!', flush=True)
            print('responding back...', flush=True)
            api.update_status('#hey @' + mention.user.screen_name
                               , mention.id)    

        elif 'hi' in mention.full_text.lower():
            print('found hi!', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hi @' + mention.user.screen_name
                               , mention.id)

        elif '#hi' in mention.full_text.lower():
            print('found #hi!', flush=True)
            print('responding back...', flush=True)
            api.update_status('#hi @' + mention.user.screen_name
                               , mention.id)                               


while True:
    reply_to_tweets()
    time.sleep(5)
