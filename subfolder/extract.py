from bs4 import BeautifulSoup
from datetime import datetime

import pandas as pd
import numpy as np
import requests
import re

try:
	from scode.selenium import *
except:
	os.system("pip install --upgrade scode")
	from scode.selenium import *
from scode.util import *

# ===============================================================================
#                               Definitions
# ===============================================================================

with load_driver() as driver:
    
    result = {"p_id":[],
            "price":[],
            "delivery":[],
            "category":[],
            "extra_explain":[],
            "event":[],
            "review":[],
            "total":[],
            "date":[],
            "cart":[],
            "rank":[]
            }

    for i in range(1,26):
        
        url = f'https://search.shopping.naver.com/search/all?query=곱창&frm=NVSHATC&pagingIndex={i}&pagingSize=40'
        

        driver.get(url)
        
        scrollDownUntilPageEnd(driver)

        text = driver.page_source

        soup = BeautifulSoup(text, 'html.parser')

        top_div_list = soup.select('[class="basicList_item__0T9JD"] div[class="basicList_info_area__TWvzp"]')

            
        for div_idx, top_div in enumerate(top_div_list, start=1):
            
            
            rank = div_idx + (i-1)*40
            
            result["rank"].append(rank)
            
            print(f'{i}페이지 // {rank}번쨰 데이터 추출 중..')
            
            product_id = rank - 1
            result["p_id"].append(product_id)
            
            title = top_div.select_one('a[class="basicList_link__JLQJf"]').text
            
            price1 = top_div.select_one('span[class="price_num__S2p_v"]').text
            price1 = re.sub('[가-힣,]', '', price1)
            result["price"].append(int(price1))
            
            delivery = top_div.select_one('span[class="deliveryInfo_info_delivery__3DAnV"]')
            price2 = delivery.text if delivery != None else None
            price2 = re.sub('[가-힣,]', '', price2) if price2 != None else np.nan
            result["delivery"].append(price2)
            
            categories_div = top_div.select_one('div[class="basicList_depth__SbZWF"]')
            categories = 1 if categories_div != None and categories_div != '' else 0
            
            result["category"].append(categories)
            
            explain = top_div.select_one('div[class="basicList_detail_box__OoXKt"]')
            extra_explain = explain.text if explain != None and explain.text != '' else 0
            result["extra_explain"].append(len(extra_explain)) if isinstance(extra_explain,str) else result["extra_explain"].append(extra_explain)

            event = top_div.select_one('div[class="basicList_product_event__5pRAq"]')
            event_msg = 1 if event != None and event.text != '' else 0
            result["event"].append(event_msg)
            
            review_buy_a = top_div.select_one('div[class="basicList_etc_box__5lkgg"]').select('a[class="basicList_etc__LSkN_"]')
            review = None
            buy = None
            for review_buy in review_buy_a:
                if '리뷰' in review_buy.text:
                    review = review_buy.text
                    review = re.sub('리뷰별점 \d\.\d', '', review).replace(',','').strip()
                    review = re.sub('별점 \d', '', review).replace(',','').strip()
                    review = re.sub('리뷰', '', review)
                elif '구매건수' in review_buy.text:
                    buy = review_buy.text
                    buy = re.sub('[가-힣,]', '', buy)
            if review is None:review = np.nan
            else:review = int(review)
            if buy is None:buy = np.nan
            else:buy = int(buy)
            
            result["review"].append(review)
            result["total"].append(buy)
            
            date_jjim_span = top_div.select_one('div[class="basicList_etc_box__5lkgg"]').select('span[class="basicList_etc__LSkN_"]')
            date = None
            jjim = None
            for date_jjim in date_jjim_span:
                if '등록일' in date_jjim.text:
                    date = date_jjim.text[:-1].replace('등록일','').strip()
                    date = datetime.strptime(date, '%Y.%m')
                elif '찜하기' in date_jjim.text:
                    jjim = date_jjim.text.replace('찜하기','').strip()
            if date is None : date = np.nan
            if jjim is None : jjim = np.nan
            else: jjim = int(jjim)
            
            result["date"].append(date)
            result["cart"].append(jjim)

pd.DataFrame(result).to_csv('./곱창.csv', index=False)


# ===============================================================================
#                            Program information
# ===============================================================================

__author__ = '임성현'
__registration_date__ = '221223'
__latest_update_date__ = '221223'
__version__ = 'v1.00'
__title__ = 'extract_data'
__desc__ = '네이버 쇼핑에서 곱창에 대한 1000위까지의 데이터를 추출하는 프로그램'

