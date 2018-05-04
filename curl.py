# -*-coding:utf-8-*-
"""
@author:Mark
@file: curl.py 
@time: 2018/04/04
"""
import requests

cookies = {
    'UM_distinctid': '1627490da11932-0f8efeb08d069a-b34356b-1fa400-1627490da121085',
    'CNZZDATA1254615503': '666271230-1522373905-http%253A%252F%252Fzhanzhang.sm.cn%252F%7C1522373905',
    '5bc8c4afcfc56a5f84b2d2c89d52f215': '43ef6dc50553aa6207ab56e28b73c81389e779e1a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2247698%22%3Bi%3A1%3Bs%3A19%3A%22john.jin%40qingbao.cn%22%3Bi%3A2%3Bi%3A86400%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D',
    'sm_diu': 'c13dc00752e5c3650f76db90131bf457%7C%7C11eef1ee4bd55b0d62%7C1522813468',
    'cna': '8GQ6E7J0ByQCATrSjgbAttB7',
    'sm_sid': 'a39a82692eb7616f249cade52a45e3a6',
    'isg': 'BLm5VGT5x2xNopv4AYXqVUFkyCVTbqxlpfb5rtvuNeBfYtn0Iha9SCez4GCUWkWw',
    'zhanzhang_access': 'nkd0gg1fba303gcfrpm1u235k1',
}

headers = {
    'Origin': 'http://zhanzhang.sm.cn',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'http://zhanzhang.sm.cn/open/sitemap/id/246540/page/1',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = [
  ('domain_id', '246540'),
  ('type', '0'),
  ('url', 'https://alpha-x.oss-cn-hangzhou.aliyuncs.com/seo/shenma/20180403.xml'),
]

response = requests.post('http://zhanzhang.sm.cn/open/addSitemapUrl', headers=headers, cookies=cookies, data=data)