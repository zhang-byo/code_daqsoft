# coding=utf8

import os

os.chdir(os.path.split(os.path.realpath(__file__))[0])

BLANK = '\u0001'
ENCODE = 'utf-8'
TIME_DELAY = 3
HDFS = '/user/spider/linkip_yq/%s'

# INFO

USER_INFO = {
    'name': 'gujing8835',
    'password': 'gugugu110',
    'type': 1,
}

PROXIES = {
    "http": "http://HY3JE71Z6CDS782P:CE68530DAD880F3B@proxy.abuyun.com:9010",
    "https": "http://HY3JE71Z6CDS782P:CE68530DAD880F3B@proxy.abuyun.com:9010",
}
REQUEST_DATA = {
    'rangeId': 1,
    'currPage': 1,
    'themeId': 0,
    'topicId': 0,
    'sentiment': 1,
    'type': 0,
    'startDay': '2017-12-05 00:00',
    'endDay': '2017-12-11 23:59',
    'page': 100,
    'allKeywords': '',
    'orKeywords': '',
    'noKeywords': '',
    'tuKeywords': '',
    'keyWordLocation': 5
}

# headers

HEADERS = {
    'Host': 'yq.linkip.cn',
    'oginin': 'http://yq.linkip.ccn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',

}

HEADERS_XML = {
    'Host': 'yq.linkip.cn',
    'Origin': 'http://yq.linkip.cn',
    'Referer': 'http://yq.linkip.cn/user/qwyq.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# url

URL_HOME = 'http://yq.linkip.cn/user/login.do'
URL_LOGIN = 'http://yq.linkip.cn/user/index.do'
URL_DATA = 'http://yq.linkip.cn/user/getdata.do'
URL_YQ = 'http://yq.linkip.cn/user/snapshot.do?id=%s'

# 请求结果

REQUESTS_RESULT = {
    'response': 'bad_requests',
    'cookies': '',
    'url': '',
    'data': '',
    'status_code': '',
    'error': ''
}

COOKIE_TEXT = ' userName=gujing8835; userPass=gugugu110; JSESSIONID=%s'
COOKIE_DICT = {
    'Cookies': ''
}

NEWS_LIST = {
    'list': [],
    'page': 1,
    'json_error': False,
    'error': ''
}

NEWS_INFO_CONTENT = {
    'content': '',
    'source': '',
    'author': '',
    'time': '',
}

# xpath

INFO_PARSE = {
    'content': '//div[@id="content"]',
    'source': '//span[@id="media"]/text()',
    'author': '//span[@id="author"]/text()',
    'time': '//span[@id="source"]/text()',
}

LIST_ELEMENTS = ['id', 'title', 'createtime', 'url', 'type', 'xss', 'source', 'score', 'sentiment', 'content']

# path

NEWS_LIST_FILE = os.path.abspath('news_list.txt')
NEWS_LIST_HISTORY_FILE = os.path.abspath('news_list_history.txt')
NEWS_LIST_IDS_FILE = os.path.abspath('news_list_id.txt')
NEWS_LIST_IDS_HISTORY_FILE = os.path.abspath('news_list_ids_history.txt')
NEWS_INFO_FILE = os.path.abspath('news_info.txt')
NEWS_INFO_HISTORY_FILE = os.path.abspath('news_info_history.txt')

for each in [NEWS_LIST_FILE,
             NEWS_LIST_HISTORY_FILE,
             NEWS_LIST_IDS_FILE,
             NEWS_INFO_FILE,
             NEWS_INFO_HISTORY_FILE,
             NEWS_LIST_IDS_HISTORY_FILE
             ]:
    if not os.path.exists(each):
        f = open(each, 'w')
        f.close()

# 关键词

KEYWORDS = [
    ('西安旅游', '48810'),
    ('旅游', '52682'),
    ('陕西旅游', '52683'),
    ('保定', '52684'),
    ('大理', '52685'),
    ('云南石林', '48964'),
    # ('云南世博园', '48965'),
    # ('云南腾冲火山', '48966'),
    # ('丽江古城', '48967'),
    # ('玉龙雪山', '48968'),
    # ('西双版纳热带植物园 ', '48969'),
    # ('崇圣寺三塔文化 ', '48970'),
    ('普达措国家公园 ', '48971'),
    ('天山大峡谷 ', '48972'),
    ('雅安', '48973'),
    ('绵阳罗浮山', '48974'),
    ('乌鲁木齐', '48975'),
    ('吐鲁番', '48976'),
    ('和田', '48977'),
    ('丽江', '48978'),
    ('克拉玛依', '48979'),
    ('克孜勒苏柯尔克孜', '48980'),
    ('博尔塔拉', '48981'),
    ('哈密地区', '48982'),
    ('阿勒泰', '48983'),
    ('昌吉', '48984'),
    ('塔城', '48985'),
    ('喀什', '48986'),
    ('新疆伊犁', '48987'),
    ('新疆巴音', '48988'),
    ('新疆阿克苏', '48989'),
    ('玉溪', '48990'),
    ('德宏', '48991'),
    ('昆明', '48993'),
    ('河北承德', '54038'),
    ('承德', '54040'),
]