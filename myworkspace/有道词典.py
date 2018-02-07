#
import  json #拿来主义，简答
import  sys
from  urllib2 import  urlopen #打开一个  url
from urllib import  urlencode #url & fother
def fetch(query_str):
    a_dict = { 'name':'ben','age':22}
    b_json = json.dumps()
    print(type(b_json))
    print(b_json)
