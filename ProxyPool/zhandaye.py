import requests
##
#会话 准备
s = requests.session()
s.headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'acw_tc=AQAAAMgkBm5yig4AxaHzdJ8ES8UguQSn; ASPSESSIONIDCQBTCTRB=OKHHPOJBELJOBPNJKHLPMELH; __51cke__=; ASPSESSIONIDAQAQDQTB=EEDHANKBHOEJIKENMMPLNACB; ASPSESSIONIDAQDSARSA=CDAEBELBOALMKPJJIDEJHPDN; acw_sc__=5acb6c95550452cbcfcf69a9413a07e22879276d; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1523279241,1523279255,1523281047,1523281054; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1523281054; __tins__16949115=%7B%22sid%22%3A%201523281379946%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201523283276184%7D; __51laig__=25',
    'Host':'ip.zdaye.com',
    'Referer': 'http://ip.zdaye.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
}

#访问
response = s.get(url='http://ip.zdaye.com/')

#返回码
print(response.status_code)
#返回结果
html_text = response.content.decode(encoding='gbk')
#print(html_text)


# xpath 入门
# https://cuiqingcai.com/2621.html
# 进阶
# https://blog.csdn.net/winterto1990/article/details/47903653
# 接口说明：text:html string
#   mode
#  从语言的本质上来说。这样的接口的本质：
#   mode代表动词， object代表宾语， about代表宾语补足语
#   use_lxml(do, it , about, which)
def lxml_demo(mode, object, about=None, attrname=None):
    from lxml import etree
    # 01 加载类库, 输入html
    if mode == 'loadhtmlbystring':
        # 从html string中读取
        etree_html = etree.HTML(object)
        return etree_html
    if mode == 'loadhtmlbyfile':
        # 从html文件中读取
        etree_html = etree.parse(object)
        return etree_html
    # 02 找到目标节点
    # 由外部操作，示例：
    # etree_html = lxml_tool('loadbystring', SOME_source_html_string)
    # target_elements = etree_html.xpath('//tr[@class="odd"]/td')
    # target_element0 = target_elements[0]
    # WANTED_string = lxml_tool('get', target_element0, 'attr', 'id')
    # WANTED_string_list = lxml_tool('get all', target_elements, 'attr', 'id')

    # 03 获取结果
    if mode == 'get':
        result = None
        if about == 'tag':
            # 获取节点标签名
            result = object.tag
        if about == 'attr':
            # 获取节点属性
            result = object.xpath('/@'+attrname)
        if about == 'text':
            # 获取节点内容
            result = object.text

        return result

def parse(func):
    def inner(SOME_source_html_string):
        etree = lxml_demo('loadhtmlbystring', SOME_source_html_string)
        targets = func(etree)
        #results = []
        #for target in targets:
        #    results.append(lxml_demo('get', target['element'], target['about'], target['which']))
        #results = lxml_demo('get', target_elements, 'text')
        #WANTED_string_list = lxml_tool('get all', target_elements, 'attr', 'id')
        return targets
    return inner
#再重构：我们直接使用@装饰 看看是否可以在parse中避免首尾两行代码。
@parse
def find_elements(etree):
    Tbodys = etree.xpath('//tbody')
    TRs = Tbodys[0].xpath('tr')
    for i, tr in enumerate(TRs):
        TDs = tr.xpath('td')
        https = TDs[6].xpath('div')
        if len(https):
            if '高匿' == TDs[3].text:
                yield {'ip':TDs[0].text, 'port':TDs[2].xpath('img/@src')}
def down_pic(url='https://up.enterdesk.com/edpic_source/ca/6b/5f/ca6b5f366b3ea52aab975235096594e8.jpg'):
    res = requests.get(url)
    f = open('test.jpg', 'wb')
    f.write(res.content)
    f.close()
ProxyGenerater = find_elements(html_text)
for i, proxy in enumerate(ProxyGenerater):
    print(proxy['ip'])
    PicUrl = 'http://ip.zdaye.com'+proxy['port'][0]
    #PicUrl = 'https://up.enterdesk.com/edpic_source/ca/6b/5f/ca6b5f366b3ea52aab975235096594e8.jpg'
    #print(proxy['port'][0])
    s.headers['referer'] = 'http://ip.zdaye.com/'
    r = s.get(url=PicUrl)
    down_pic(PicUrl)
    #print(r.content.decode(encoding='utf-8',errors='ignore'))
    f = open('N'+'1'*i+'.jpg', 'wb')
    f.write(r.content)
    f.close()


