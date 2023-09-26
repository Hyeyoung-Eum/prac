import requests
import time

url='https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'

def sync_fetch():
    res = [requests.get(url.format(code='005930', page=i)) for i in range(1, 50)]
    return res

if __name__ =='__main__':

    start = time.time()
    sync_fetch()
    end = time.time()
    print(f'elapsed time = {end-start}s')