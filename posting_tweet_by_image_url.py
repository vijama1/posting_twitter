#importing the necessary modules
from TwitterAPI import TwitterAPI
import urllib

#account authentication
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

#opening the image url
content=urllib.request.urlopen("image_url")

#generating the API
api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret)

#reading the image data
data = content.read()

#uploading the image
r = api.request('media/upload', None, {'media': data})
if r.status_code==200:
    print("Media uploaded")
else:
    print("Failure in uploading")


#posting tweet with reference to uploaded image
if r.status_code == 200:
        media_id = r.json()['media_id']
        r = api.request('statuses/update', {'status':'your_status', 'media_ids':media_id})
        if r.status_code==200:
            print("Status uploaded")
        else:
            print("Failure in uploading status")
