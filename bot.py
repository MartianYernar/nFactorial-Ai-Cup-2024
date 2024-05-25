import requests
from bs4 import BeautifulSoup

cookies = {
    'GUCS': 'AXMVXg2o',
    'GUC': 'AQEBCAFmU1pmgkIfIwSk&s=AQAAALtJc_9x&g=ZlIS0g',
    'A1': 'd=AQABBN4n-WUCEDYTlwy0e-JNR0vtMDlVNsAFEgEBCAFaU2aCZmNnb2UB_eMBAAcI3if5ZTlVNsA&S=AQAAArkyRxllD20uXtkfLjWxzxg',
    'A3': 'd=AQABBN4n-WUCEDYTlwy0e-JNR0vtMDlVNsAFEgEBCAFaU2aCZmNnb2UB_eMBAAcI3if5ZTlVNsA&S=AQAAArkyRxllD20uXtkfLjWxzxg',
    'A1S': 'd=AQABBN4n-WUCEDYTlwy0e-JNR0vtMDlVNsAFEgEBCAFaU2aCZmNnb2UB_eMBAAcI3if5ZTlVNsA&S=AQAAArkyRxllD20uXtkfLjWxzxg',
    'cmp': 't=1716654795&j=0&u=1---',
    'gpp': 'DBAA',
    'gpp_sid': '-1',
    'axids': 'gam=y-8e65bwJE2uLyreJ4dQFMHHC1G_eR80NX~A&dv360=eS15QWtNS2JCRTJ1RnA1bUI4RzRRUFFaTDRvNlRIMnBsWH5B&ydsp=y-ItWmhT5E2uLb_vvvmzJifZhrjs2B1JcK~A&tbla=y-4cIXkR5E2uICzbDrvbv8WJbcB_pxoYZM~A',
    'tbla_id': '5276aaab-a051-49ca-be81-7a63cb266943-tuctcf3e92d',
    'trc_cookie_storage': 'taboola%2520global%253Auser-id%3D5276aaab-a051-49ca-be81-7a63cb266943-tuctcf3e92d',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'GUCS=AXMVXg2o; GUC=AQEBCAFmU1pmgkIfIwSk&s=AQAAALtJc_9x&g=ZlIS0g; A1=d=AQABBN4n-WUCEDYTlwy0e-JNR0vtMDlVNsAFEgEBCAFaU2aCZmNnb2UB_eMBAAcI3if5ZTlVNsA&S=AQAAArkyRxllD20uXtkfLjWxzxg; A3=d=AQABBN4n-WUCEDYTlwy0e-JNR0vtMDlVNsAFEgEBCAFaU2aCZmNnb2UB_eMBAAcI3if5ZTlVNsA&S=AQAAArkyRxllD20uXtkfLjWxzxg; A1S=d=AQABBN4n-WUCEDYTlwy0e-JNR0vtMDlVNsAFEgEBCAFaU2aCZmNnb2UB_eMBAAcI3if5ZTlVNsA&S=AQAAArkyRxllD20uXtkfLjWxzxg; cmp=t=1716654795&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=gam=y-8e65bwJE2uLyreJ4dQFMHHC1G_eR80NX~A&dv360=eS15QWtNS2JCRTJ1RnA1bUI4RzRRUFFaTDRvNlRIMnBsWH5B&ydsp=y-ItWmhT5E2uLb_vvvmzJifZhrjs2B1JcK~A&tbla=y-4cIXkR5E2uICzbDrvbv8WJbcB_pxoYZM~A; tbla_id=5276aaab-a051-49ca-be81-7a63cb266943-tuctcf3e92d; trc_cookie_storage=taboola%2520global%253Auser-id%3D5276aaab-a051-49ca-be81-7a63cb266943-tuctcf3e92d',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'guccounter': '1',
    'guce_referrer': 'aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8',
    'guce_referrer_sig': 'AQAAAMJ99NLPOyKWsSqE1HKMy5at7RwVB8hork3rk-CCGC_iN4Iw4SJ3gCwBzZDYl5AibYf2rnJIPuQouIVqAFG3JiLW5M2yRz6TQYhfzVr15eFMkP02zMfwKu-ap3KiYnIHqR3B_7xUkzvuWQZiLjTBiCSk3bGZOJ8iRIs-ucXHMMSC',
}
def get_news():
    response = requests.get('https://finance.yahoo.com/', params=params, cookies=cookies, headers=headers)

    src = response.text
    soup = BeautifulSoup(src, 'html.parser')

    news = soup.find_all('h3', class_='clamp tw-line-clamp-none tw-leading-5 svelte-1v1zaak')
    
    # print(len(news))
    return news

def get_links():
    response = requests.get('https://finance.yahoo.com/', params=params, cookies=cookies, headers=headers)
    src = response.text
    soup = BeautifulSoup(src, 'html.parser')
    links = soup.find_all('a', class_='subtle-link fin-size-small titles basis-without-img noUnderline svelte-wdkn18', href=True)
    # print(len(links))
    
    return links

def get_cryp():
    response = requests.get('https://finance.yahoo.com/', params=params, cookies=cookies, headers=headers)
    src = response.text
    soup = BeautifulSoup(src, 'html.parser')
    cryp = soup.find_all('span', class_='symbol svelte-86injt valid')
    
    return cryp
# get_news()
# get_links()

