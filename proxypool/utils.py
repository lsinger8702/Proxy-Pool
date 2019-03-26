import requests
from requests.exceptions import ConnectionError

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def get_page(url, options={}):
	"""
	抓取代理
	:param url:
	:param options:
	:return:
	"""
	headers = dict(base_headers, **options)
	print('正在抓取', url)
	try:
		response = requests.get(url, headers=headers)
		print('抓取成功', url, response.status_code)
		if response.status_code == 200:
			return response.text
	except ConnectionError:
		print('抓取失败', url)
		return None