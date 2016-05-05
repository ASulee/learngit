from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://gz.ganji.com/wu/'
urlhost = 'http://gz.ganji.com'


def ganji_index_url(url):
    wd_data = requests.get(url)
    suop = BeautifulSoup(wd_data.text, 'lxml')
    link = suop.select('dl dt a')
    for links in link:
        page_url = urlhost + links.get('href')
        print(page_url)


ganji_index_url(url)

url_list = '''
        http://gz.ganji.com/shouji/

        http://gz.ganji.com/shoujipeijian/
        http://gz.ganji.com/bijibendiannao/
        http://gz.ganji.com/taishidiannaozhengji/
        http://gz.ganji.com/diannaoyingjian/
        http://gz.ganji.com/wangluoshebei/
        http://gz.ganji.com/shumaxiangji/
        http://gz.ganji.com/youxiji/
        http://gz.ganji.com/xuniwupin/
        http://gz.ganji.com/jiaju/
        http://gz.ganji.com/jiadian/
        http://gz.ganji.com/zixingchemaimai/
        http://gz.ganji.com/rirongbaihuo/
        http://gz.ganji.com/yingyouyunfu/
        http://gz.ganji.com/fushixiaobaxuemao/
        http://gz.ganji.com/meironghuazhuang/
        http://gz.ganji.com/yundongqicai/
        http://gz.ganji.com/yueqi/
        http://gz.ganji.com/tushu/
        http://gz.ganji.com/bangongjiaju/
        http://gz.ganji.com/wujingongju/
        http://gz.ganji.com/nongyongpin/
        http://gz.ganji.com/xianzhilipin/
        http://gz.ganji.com/shoucangpin/
        http://gz.ganji.com/baojianpin/
        http://gz.ganji.com/laonianyongpin/
        http://gz.ganji.com/gou/
        http://gz.ganji.com/qitaxiaochong/
        http://gz.ganji.com/xiaofeika/
        http://gz.ganji.com/menpiao/

        http://gz.ganji.com/jiaju/
        http://gz.ganji.com/rirongbaihuo/
        http://gz.ganji.com/shouji/
        http://gz.ganji.com/shoujihaoma/
        http://gz.ganji.com/bangong/
        http://gz.ganji.com/nongyongpin/
        http://gz.ganji.com/jiadian/
        http://gz.ganji.com/ershoubijibendiannao/
        http://gz.ganji.com/ruanjiantushu/
        http://gz.ganji.com/yingyouyunfu/
        http://gz.ganji.com/diannao/
        http://gz.ganji.com/xianzhilipin/
        http://gz.ganji.com/fushixiaobaxuemao/
        http://gz.ganji.com/meironghuazhuang/
        http://gz.ganji.com/shuma/
        http://gz.ganji.com/laonianyongpin/
        http://gz.ganji.com/xuniwupin/
        http://gz.ganji.com/qitawupin/
        http://gz.ganji.com/ershoufree/
        http://gz.ganji.com/wupinjiaohuan/

'''
