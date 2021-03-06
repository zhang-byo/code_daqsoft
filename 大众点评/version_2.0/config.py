import os
import logging
from config_area import CITY_LIST

os.chdir(os.path.split(os.path.abspath(__file__))[0])

# CHOICE = sys.argv[1:][0]
"""
# 测试用
CHOICE = 'food'
PROVS = '河北'
"""
PROVS = '河北'
CHOICE = 'shopping'
CITY_LIST = CITY_LIST

# 设置
BLANK = '\u0001'
ENCODEING = 'utf8'
HDFS = '/user/spider/dianping/%s'
REQUESTS_LOG = 'requests_%s.log'
# 请求回应 response

REQUESTS_RESULT = {
    'response': 'bad_requests',
    'url': '',
    'params': '',
    'status_code': '',
    'error': ''
}

CATEGORY_LIST = {
    'data': [],
}

SHOP_LIST = {
    'data': [],
}

SHOP_INFO = {
    'data': [],
    'error': ''
}

SHOP_CMT = {
    'data': [],
}

# logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='requests_%s.log' % PROVS,
    filemode='w+'
)
# 分类

TYPES = {
    'entertainment': '30',
    'food': '10',
    'shopping': '50'
}

# url

CATEGORY_URL = 'http://www.dianping.com/search/category/%s/%s/'
# 四个参数，依旧是cityid， 菜品分类， 行政区
SHOP_URL = 'http://www.dianping.com/search/category/%s/%s/%s%sp'

INFO_URL = 'http://www.dianping.com/ajax/json/shopfood/wizard/BasicHideInfoAjaxFP'

# CMT_URL = 'http://www.dianping.com/shop/%s/review_more_latest?pageno=%s'
CMT_URL = 'http://www.dianping.com/shop/%s/review_all/p%s?queryType=sortType&queryVal=latest'

# xpath

CATEGORY_LIST_PARSE = {
    'list': '//div[@class="nc-contain"]/div[@class="con"]/div[@id="classfy"]/a',
    'id': '@href',
    'type': 'span/text()'
}

SHOP_LIST_PARSE = {
    'list': '//div[@id="shop-all-list"]/ul/li',
    'url': 'div[@class="txt"]/div[@class="tit"]/a/@href',
    'name': 'div[@class="txt"]/div[@class="tit"]/a/h4/text()',
}

SHOP_CMT_PARSE = {
    'data': '//div[@class="reviews-items"]/ul/li',
    'user1': 'div[@class="main-review"]/div[@class="dper-info"]/a/text()',
    'user2': 'div[@class="main-review"]/div[@class="dper-info"]/span/text()',
    # 贡献值被取消
    'contribution': 'div[@class="no_data"]/text()',
    'attitute': 'div[@class="main-review"]/div[@class="review-rank"]/span/@class',
    # 分数也没有了
    'score': 'div[@class="main-review"]/div[@class="review-rank"]/span[@class="score"]/span/text()',
    'content': 'div[@class="main-review"]/div[@class="review-words"]/text()',
    'date': 'div[@class="main-review"]/div[@class="misc-info clearfix"]/span[@class="time"]/text()',
    'fav': 'div[@class="main-review"]/div[@class="review-recommend"]/a/text()',
    'imgs': 'div[@class="main-review"]/div[@class="review-pictures"]/ul/li/a/img/@data-big',
}

# cookies

COOKIES1 = {
    "Cookie": (
        # "cy=8;"
        # " cye=chengdu;"
        # " _lxsdk_cuid=1614591ca5dc8-077d8fce01b563-32667403-13c680-1614591ca5dc8;"
        # " _lxsdk=1614591ca5dc8-077d8fce01b563-32667403-13c680-1614591ca5dc8;"
        # " _hc.v=368d1395-fa0e-d541-e0f6-8690a26bb529.1517290638;"
        # " dper=9b5ba8ba8fb7338106d7db259d132cf9e4a4b9ff6044c42201fcf8347bf59323;"
        " ll=7fd06e815b796be3df069dec7836c3df;"  ## !!!
         " lgtoken=025cadcec-73bf-4809-a971-4e7bdebdd442;"
        # " ua=18582389107;"
        " ctu=06936018815a622639a414e01836cb5348b97dd37cfa87092eb83d7be0c80ad4;"  # !!!
        # " s_ViewType=10;"
        " _lxsdk_s=1614591ca60-041-da1-f01%7C%7C44"  # !!!
    )
}
COOKIES = {
    "Cookie": (
        "cy=8;"
        " cye=chengdu;"
        " _lxsdk_cuid=162422c252dc8-0fcacc5ef594bc-33627805-13c680-162422c252ec8;"
        " _lxsdk=162422c252dc8-0fcacc5ef594bc-33627805-13c680-162422c252ec8;"
        " _hc.v=d5577e34-76fc-368f-4031-71cdbdcfe638.1521528612;"
        " lgtoken=059f0fd5a-1baf-4927-9e20-2c4933bdf245;"
        " thirdtoken=481037F8F2674FD1871F3898C6905637;"
        " JSESSIONID=A1925DDA6858B3170FC3FBC4BDA69F2F;"
        " dper=668d1f13c70683432c25a44d18614673879dea2f3c2c030adc1c685ac6298b8e;"
        " ll=7fd06e815b796be3df069dec7836c3df;"
        " ua=_%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E4%B8%AD%E5%80%BC%E5%AE%9A%E7%90%86;"
        " ctu=a91d9076090ffb8fe11e3982711567ed049a427fb68f247a21e59c84a4ed9fac;"
        " s_ViewType=10;"
        " wed_user_path=2814|0;"
        " aburl=1;"
        "__mta=189209876.1521528632529.1521528632529.1521528632534.2;"
        " _lxsdk_s=162422c2531-361-e20-a4f%7C%7C33"
   )
}

# PARAMS
PARAMS = {
    "_nr_force": "1508318702379",
    "shopId": "66037477",
}
# 代理

PROXIES = {
    "http": "http://HY3JE71Z6CDS782P:CE68530DAD880F3B@proxy.abuyun.com:9010",
    "https": "http://HY3JE71Z6CDS782P:CE68530DAD880F3B@proxy.abuyun.com:9010",
}

# headers

HEADERS = {
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/shop/3998371',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
}

HEADERS_XML = {
    'X-Request': 'JSON',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.dianping.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
}

# 文件夹系列

CATEGORY_FILE = {
    'food': os.path.join(os.path.abspath(PROVS), 'food_category_list.txt'),
    'entertainment': os.path.join(os.path.abspath(PROVS), 'entertainment_category_list.txt'),
    'shopping': os.path.join(os.path.abspath(PROVS), 'shopping_category_list.txt'),
}

SHOP_LIST_FILE = {
    'food': os.path.join(os.path.abspath(PROVS), '%s_food_shop_list.txt' % PROVS),
    'entertainment': os.path.join(os.path.abspath(PROVS), '%s_entertainment_shop_list.txt' % PROVS),
    'shopping': os.path.join(os.path.abspath(PROVS), '%s_shopping_shop_list.txt' % PROVS),
}

SHOP_INFO_FILE = {
    'food': os.path.join(os.path.abspath(PROVS), '%s_food_shop_info.txt' % PROVS),
    'entertainment': os.path.join(os.path.abspath(PROVS), '%s_entertainment_shop_info.txt' % PROVS),
    'shopping': os.path.join(os.path.abspath(PROVS), '%s_shopping_shop_info.txt' % PROVS),
}

SHOP_ALREADY_EXISTS = {
    'food': os.path.join(os.path.abspath(PROVS), '%s_food_shop_exists.txt' % PROVS),
    'entertainment': os.path.join(os.path.abspath(PROVS), '%s_entertainment_exists.txt' % PROVS),
    'shopping': os.path.join(os.path.abspath(PROVS), '%s_shopping_exists.txt' % PROVS),
}

SHOP_CMT_FILE = {
    'food': os.path.join(os.path.abspath(PROVS), '%s_food_cmt.txt' % PROVS),
    'entertainment': os.path.join(os.path.abspath(PROVS), '%s_entertainment_cmt.txt' % PROVS),
    'shopping': os.path.join(os.path.abspath(PROVS), '%s_shopping_cmt.txt' % PROVS)
}

SHOP_CMT_HISTORY_FILE = {
    'food': os.path.join(os.path.abspath(PROVS), '%s_food_history_cmt.txt' % PROVS),
    'entertainment': os.path.join(os.path.abspath(PROVS), '%s_entertainment_history_cmt.txt' % PROVS),
    'shopping': os.path.join(os.path.abspath(PROVS), '%s_shopping_history_cmt.txt' % PROVS)
}

START_DATE_FILE = {
    'food': os.path.join(os.path.abspath(PROVS), 'food_start.txt'),
    'entertainment': os.path.join(os.path.abspath(PROVS), 'entertainment_start.txt'),
    'shopping': os.path.join(os.path.abspath(PROVS), 'shopping_start.txt'),
}
#
DATA_STYLE = {
    "food": {
        "中文全称": "&",
        "中文简称": "&",
        "所属地区": "&",
        "地址": "&",
        "地理位置": "&",
        "类型": "&",
        "等级": "&",
        "营业时间": "&",
        "人均消费": "&",
        "特色菜品": "&",
        "咨询电话": "&",
        "传真": "&",
        "邮政编码": "&",
        "投诉电话": "&",
        "交通信息": "&",
        "周边信息": "&",
        "简介": "&",
        "国别": "&",
        "省自治区全称": "&",
        "省自治区简称": "&",
        "市州全称": "&",
        "市州简称": "&",
        "区县全称": "&",
        "区县简称": "&",
        "地区编码": "&",
        "url": "&",
    },
    "entertainment": {
        "中文全称": "&",
        "中文简称": "&",
        "所属地区": "&",
        "地址": "&",
        "地理位置": "&",
        "类型": "&",
        "营业时间": "&",
        "咨询电话": "&",
        "传真": "&",
        "邮政编码": "&",
        "投诉电话": "&",
        "交通信息": "&",
        "周边信息": "&",
        "简介": "&",
        "国别": "&",
        "省自治区全称": "&",
        "省自治区简称": "&",
        "市州全称": "&",
        "市州简称": "&",
        "区县全称": "&",
        "区县简称": "&",
        "地区编码": "&",
        "url": "&",
    },
    "shopping": {
        "中文全称": "&",
        "中文简称": "&",
        "所属地区": "&",
        "地址": "&",
        "地理位置": "&",
        "类型": "&",
        "营业时间": "&",
        "特色商品": "&",
        "传真": "&",
        "邮政编码": "&",
        "投诉电话": "&",
        "交通信息": "&",
        "周边信息": "&",
        "简介": "&",
        "国别": "&",
        "省自治区全称": "&",
        "省自治区简称": "&",
        "市州全称": "&",
        "市州简称": "&",
        "区县全称": "&",
        "区县简称": "&",
        "地区编码": "&",
        "url": "&",
    }
}

DATA_STYLE_L = {
    "food": [
    "中文全称", "中文简称", "所属地区", "地址", "地理位置", "类型", "等级", "营业时间", "人均消费", "特色菜品", "咨询电话",
    "传真", "邮政编码", "投诉电话", "交通信息", "周边信息", "简介", "国别", "省自治区全称", "省自治区简称", "市州全称",
    "市州简称", "区县全称", "区县简称", "地区编码", "url",
    ],
    "entertainment": [
    "中文全称", "中文简称", "所属地区", "地址", "地理位置", "类型", "营业时间", "咨询电话", "传真", "邮政编码",
    "投诉电话", "交通信息", "周边信息", "简介", "国别", "省自治区全称", "省自治区简称", "市州全称", "市州简称", "区县全称",
    "区县简称", "地区编码", "url"
    ],
    "shopping": [
    "中文全称", "中文简称", "所属地区", "地址", "地理位置", "类型", "营业时间", "特色商品", "传真",
    "邮政编码", "投诉电话", "交通信息", "周边信息", "简介", "国别", "省自治区全称", "省自治区简称", "市州全称",
    "市州简称", "区县全称", "区县简称", "地区编码", "url"
    ]
}

# 创建分类list
if not os.path.exists(PROVS):
    os.mkdir(os.path.abspath(PROVS))

for each in ['food', 'entertainment', 'shopping']:
    for i in [CATEGORY_FILE, SHOP_LIST_FILE, SHOP_INFO_FILE, SHOP_ALREADY_EXISTS, SHOP_CMT_FILE, SHOP_CMT_HISTORY_FILE]:
        if not os.path.exists(i[each]):
            f = open(i[each], 'w+')
            f.close()

    if not os.path.exists(START_DATE_FILE[each]):
        f = open(START_DATE_FILE[each], 'w+')
        f.write('2017-11-01')
        f.close()
