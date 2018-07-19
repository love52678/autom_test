import requests


ip = 'http://118.31.19.120:3000/api/v1'
url = '/topics?'
def get_topics(page,tab,limit,mdrender):
    value = ip+url+'&page'+str(page)+'&tab'+str(tab)+'&limit'+str(limit)+'&mdrender'+str(mdrender)
    res = requests.get(value)
    print res.text

if __name__=='__main__':
    page = 1
    tab = 'ask'
    limit = 10
    mdrender = 'false'
    get_topics(page,tab,limit,mdrender)