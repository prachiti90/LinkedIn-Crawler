#!/usr/bin/env python
import oauth2 as oauth
import httplib2
import time, os, simplejson
import json
 
# Fill the keys and secrets you retrieved after registering your app

consumer_key  = '78n346jkxj5sub'
consumer_secret = 'FUpuqff4O6qucIyN'
user_token = '0ddc05c7-1fc4-4bc1-98f5-fc62f8d2683e'
user_secret = 'b57425ab-6b06-44d8-82fd-1b6a9984c7ec'

 
# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)
 
# Use the consumer object to initialize the client object
client = oauth.Client(consumer)
 
# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)
 
client = oauth.Client(consumer, access_token)
 
# Make call to LinkedIn to retrieve your data

connections = []
for no in xrange(0, 1601):
    if no%10 == 0:
        x = client.request("https://api.linkedin.com/v1/company-search:(companies:(id,name,universal-name,website-url,company-type,industries,blog-rss-url,twitter-id,employee-count-range,locations),num-results)?hq-only=true&facet=location,in&facet=industry,104&start=" + str(no) + "&count=10&format=json", "GET", "")


# Remove the Header 
connections.append(x[1])

# Write fetched data in json format
f = open('linkedin2_data1.json','a')

f.write(json.dumps(connections, indent=2))

f.close()

