from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd 
import re, math
driver= webdriver.Chrome()
driver.refresh()
driver.maximize_window()
driver.get('https://www.daraz.com.bd/products/fonex-alloy-glasses-frame-men-square-eyeglasses-frames-2022-new-male-full-ultralight-optical-korean-style-rectangle-stylish-eyewear-singapore-branded-8105-i379743945-s1905336575.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A379743945%253Bsrc%253ALazadaMainSrp%253Brn%253A1db7fdeaf7a8c2a4758f35ec9785e94b%253Bregion%253Abd%253Bsku%253A379743945_BD%253Bprice%253A1734%253Bclient%253Adesktop%253Bsupplier_id%253A700682144823%253Bsession_id%253A%253Bbiz_source%253Ah5_external%253Bslot%253A2%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7693%253Bitem_id%253A379743945%253Bsku_id%253A1905336575%253Bshop_id%253A498867%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Overseas&price=1734&priceCompare=skuId%3A1905336575%3Bsource%3Alazada-search-voucher%3Bsn%3A1db7fdeaf7a8c2a4758f35ec9785e94b%3BoriginPrice%3A173400%3BdisplayPrice%3A173400%3BsinglePromotionId%3A50000075262001%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1779508764264&ratingscore=5.0&request_id=1db7fdeaf7a8c2a4758f35ec9785e94b&review=7&sale=25&search=1&source=search&spm=a2a0e.searchlistcategory.list.2&stock=1')


height= driver.execute_script('return document.body.scrollHeight')  
print(height);
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for i in range(0, height+300, 50):
    driver.execute_script("window.scrollTo(0, "+str(i)+");")
    time.sleep(0.5)
comment= driver.find_elements(By.CLASS_NAME, 'content')
#module_product_review > div > div > div:nth-child(3) > div.mod-reviews > div:nth-child(1) > div.item-content > div.content
for c in comment:
    print(c.text)