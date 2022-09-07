"""

  """

import json
from ast import literal_eval

import requests
from githubdata import GithubData


class GDUrl :
    trg = 'https://github.com/imahdimir/rd-tse_ir-industry-subIndustry'
    cur = 'https://github.com/imahdimir/u-rd-tse_ir-industry-subIndustry'

gdu = GDUrl()

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

    gd_trg = GithubData(gdu.trg)
    gd_trg.overwriting_clone()
    ##
    jsp = gd_trg.local_path / 'data.json'
    ##
    with open(jsp , 'w' , encoding = 'utf8') as fi :
        json.dump(dc , fi)
    ##
    msg = 'update data.json by: '
    msg += gdu.cur
    ##
    gd_trg.commit_and_push(msg)
    ##


    gd_trg.rmdir()


    ##

##
if __name__ == '__main__' :
    main()

##

##
