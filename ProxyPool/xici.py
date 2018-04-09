import requests
####
#会话 准备
s = requests.session()
s.headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZiNGQ1ZTU3YjMwZTA2ZGYxMzVhY2M3YjZkNDkxNGQ5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWhVR1VKdk5hZWdKcitEQW5sSm1sanBJY3htbVZmU0JUMWQ3OFdhck44clk9BjsARg%3D%3D--60da3d0d1ed32e7e62ae84aab7ca86e678536a51; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1521345442,1522929663; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1522929663',
    'Host':'www.xicidaili.com',
    'If-None-Match': 'W/"81a4a5c3279ec77139d18a237910610a"',
    'Referer': 'https://www.baidu.com/link?url=QdQlW7k_y7eJ6YggypAR1U6c-DT7cad3U2BzGygm0aSurUjgEYAeedNnvu5QfjUS&wd=&eqid=a954efc500072df6000000035ac60ff9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
}

#访问
response = s.get(url='http://www.xicidaili.com/')

#返回码
print(response.status_code)
#返回结果
html_text = response.content.decode(encoding='utf-8')
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
#再重构：我们直接使用@装饰 看看是否可以在parse中避免首尾两行代码。
def parse(SOME_source_html_string):
    etree_html = lxml_demo('loadbystring', SOME_source_html_string)
    target_elements = etree_html.xpath('//tr[@class="odd"]/td')
    target_element0 = target_elements[0]
    WANTED_string = lxml_demo('get', target_element0, 'attr', 'id')
    #WANTED_string_list = lxml_tool('get all', target_elements, 'attr', 'id')
    return WANTED_string

e_text = parse(html_text)
print(e_text)

