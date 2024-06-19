import requests
import time
import multiprocessing
import random
from multiprocessing import Pool
from bs4 import BeautifulSoup
import selenium
from random import choice


proxy_pool = ['113.241.138.164','171.41.148.230', '171.41.129.231']
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
MAX_WORKER_NUM = multiprocessing.cpu_count()
proxy = choice(proxy_pool)
proxies = {proxy}

def fetch():
    r = requests.get('https://www.4.cn/buynow/detail/bid/136172555/DomainName/sl1599.com',headers=headers,proxies=proxies)
    print(r)

if __name__ == '__main__':
    t1 = time.time()
    p = Pool(MAX_WORKER_NUM)
    for i in range(1000):
        p.apply_async(fetch, args=())
    p.close()
    p.join()


    print('多进程爬虫耗时：', time.time() - t1)