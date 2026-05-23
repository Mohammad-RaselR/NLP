from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd 
driver= webdriver.Chrome()
driver.get('https://www.daraz.com.bd/men-eyeglasses/')

# text= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text
# link= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')
# //*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/a
# //*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a
# print("This is link", link)

# print("This is text", text)
# for image
# //*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img

# //*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/a/div/img
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

text_list = []
image_link=[]
link_list=[]

for i in range (1, 41):
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]/a').text
    image= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[1]/div/a/div/img').get_attribute('src')
    link= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]/a').get_attribute('href')
    text_list.append(text)
    image_link.append(image)
    link_list.append(link)





time.sleep(5)
driver.quit()

data={
    'Text': text_list,
    'Image Link': image_link,
    'Link': link_list
}
df= pd.DataFrame(data)

df.to_csv('daraz.csv', index=False)
print(len(text_list))
print(len(image_link))
print(len(link_list))