from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
import lxml

clint = pymongo.MongoClient('localhost', 27017)
ganji = clint['ganji']
ganji_url_list = ganji['url_list']
ganji_item_info = ganji['item_info']

channel1 = 'http://gz.ganji.com/fushixiaobaxuemao/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Connection': 'keep-alive'
}
proxy_list = [
    'http://14.18.236.99:80',
    'http://14.18.236.100:80',
    'http://14.18.236.99:80'


]
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}
url22 = 'http://gz.ganji.com/bijibendiannao/'


def get_links_from(channel, pages, who_sell=1):
    list_view = '{}a{}o{}'.format(channel, str(who_sell), str(pages), )
    print(list_view)
    wb_data = requests.get(list_view, headers=headers)

    time.sleep(1)
    suop = BeautifulSoup(wb_data.text, 'lxml')

    if suop.find('ul', 'pageLink'):
        for link in suop.select('li.js-item a.ft-tit'):
            item_link = link.get('href')
            ganji_url_list.insert_one({'url': item_link})
            print(item_link)
    else:
        pass


url = 'http://gz.ganji.com/fushixiaobaxuemao/2024435985x.htm'


def get_ganji_info(url, data=None):
    time.sleep(2)
    wd_data = requests.get(url, headers=headers)
    if wd_data.status_code == 404:
        pass
    else:
        try:
            suop = BeautifulSoup(wd_data.text, 'lxml')

            data = {
                'title': suop.title.text,
                'date': suop.select('i.pr-5')[0].text.strip().split(' ')[0],
                'types': suop.select('li span a')[5].text,
                'prices': int(suop.select('i.f22')[0].text),
                'aers': list(suop.select('ul.det-infor li')[2].stripped_strings),
                'url': url
            }
            ganji_item_info.insert_one(data)


        except AttributeError:
            pass
        except IndexError:
            pass



'''

'''
