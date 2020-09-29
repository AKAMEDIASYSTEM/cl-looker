"""Check craigslist every day for lathes near you."""

from craigslist import CraigslistForSale as CFS
import tweepy
import time
import json

'''
>> CFS.show_filters()
Base filters:
* query = ...
* search_titles = True/False
* has_image = True/False
* posted_today = True/False
* bundle_duplicates = True/False
* search_distance = ...
* zip_code = ...
Section specific filters:
* min_price = ...
* max_price = ...
* make = ...
* model = ...
* min_year = ...
* max_year = ...
* min_miles = ...
* max_miles = ...
* min_engine_displacement = ...
* max_engine_displacement = ...
* language = 'af', 'ca', 'da', 'de', 'en', 'es', 'fi', 'fr', 'it', 'nl', 'no', 'pt', 'sv', 'tl', 'tr', 'zh', 'ar', 'ja', 'ko', 'ru', 'vi'
* condition = 'new', 'like new', 'excellent', 'good', 'fair', 'salvage'

'''

#  params built into the craigslist library
script_site = 'nh'
script_area = None
script_zipcode = '03301'
script_radius = 75
script_today_only = True


twitter_consumer_key = 'YOUR_OWN_CREDENTIALS'
twitter_consumer_secret = 'YOUR_OWN_CREDENTIALS'
twitter_access_token = 'YOUR_OWN_CREDENTIALS'
twitter_access_token_secret = 'YOUR_OWN_CREDENTIALS'
twitter_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
twitter_auth.set_access_token(twitter_access_token, twitter_access_token_secret)

api = tweepy.API(twitter_auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

with open('terms.json') as f:
    data = json.load(f)
    for item in data:
        print(item['name'])
        lathes = CFS(site=script_site, filters={'has_image': True, 'search_distance': script_radius, 'search_titles': True, 'bundle_duplicates': True, 'posted_today': script_today_only, 'zip_code': script_zipcode, 'query': item['name'], 'max_price': item['limit']})
        print('starting cl-lathe looker')
        for i in lathes.get_results(sort_by='newest', geotagged=True):
            if i['deleted'] is False and i['repost_of'] is None:
                tweet_text = "{}: {}\n{}".format(i['price'], i['name'], i['url'])
                print(tweet_text)
                try:
                    api.update_status(tweet_text)
                except Exception as e:
                    print(str(e))
                    pass
                time.sleep(17)
