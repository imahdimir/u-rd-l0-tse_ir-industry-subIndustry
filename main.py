"""

  """

##


import json
from ast import literal_eval

import requests


def main() :

  pass

  ##
  url = 'https://tse.ir/json/Listing/ListingByGroup1.json'
  ##
  r = requests.get(url , verify = False)
  t1 = r.text
  ##
  t1 = '{' + t1.split('{' , 1)[1]
  ##
  dc = literal_eval(t1)
  ##
  with open('sc.json' , 'w' , encoding = 'utf8') as fi :
    json.dump(dc , fi)

  ##
  with open('sc.json' , 'r') as fi :
    dc1 = json.load(fi)

  ##

##
if __name__ == '__main__' :
  main()

##

##