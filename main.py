import httpx
import requests
import time
import asyncio
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def main():
    urls = get_urls()
    start = time.time()
    [scrape_by_requests_bs4(url) for url in urls]
    print(f'requests processing time: {time.time() - start} second(s)')

    start = time.time()
    executor = ThreadPoolExecutor()
    executor.map(scrape_by_requests_bs4(),urls)
    print(f'concurrent requests processing time: {time.time() - start} second(s)')

def get_urls():
    urls = []
    [urls.append(f'https://www.entrepreneur.com/franchises/category/personal-care-businesses/{str(page)}') for page in range(1,6)]
    return urls

def scrape_by_requests_bs4(url):
    s = requests.Session()
    response = s.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    names = soup.select("p.text-base.font-medium.text-gray-700.w-1\/2")
    for i,name in enumerate(names):
        name = name.text.split('\n')[1].replace('\t','')
        print(f"{i}. {name}")

def scrape_by_httpx_selectolax(url):
    client = httpx.AsyncClient
    response = client()


if __name__ == '__main__':
    main()