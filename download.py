from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys


key = '16c49025c7114359c5daff81a39d1e9b'
secret = 'bb7b7e37d31fbb59'
wait_time = 1

#argv[1]はターミナル でpython download.py animalnameとするときの２番目の引数のこと
nationalname = sys.argv[1]
savedir = "./" + nationalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = nationalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

#ダウンロードpython download.py の後の引数のファイル名は、空欄入れられない
photos = result['photos']
# pprint(photos)

for i, photo in enumerate(photos['photo']):
     url_q = photo['url_q']
     filepath = savedir + '/' + photo['id'] + '.jpg'
     if os.path.exists(filepath):continue
     urlretrieve(url_q, filepath)
     time.sleep(wait_time)
