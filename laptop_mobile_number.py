from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
driver = webdriver.Chrome()

driver.get("https://www.google.com/maps")

time.sleep(5)

search_box = driver.find_element(By.XPATH, '//input[@name="q"]')

search_box.send_keys("laptop shop dhaka")

search_box.send_keys(Keys.ENTER)

time.sleep(5)

# left sidebar scrollable div
scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')

previous_count = 0

while True:

    results = driver.find_elements(
        By.XPATH,
        '//a[contains(@href,"/place")]'
    )

    current_count = len(results)

    print("Loaded Results:", current_count)

    # stop if no new result appears
    if current_count == previous_count:
        break

    previous_count = current_count

    # scroll down
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollHeight',
        scrollable_div
    )

    time.sleep(3)

print("\nFinal Total Results:", len(results))

names_list=[]
phone_number_list=[]

for i in range(1, len(results)+1):

    index = (2 * i) + 1

    try:

        name = driver.find_element(
            By.XPATH,
            f'/html/body/div[1]/div[2]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{index}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]'
        ).text

    except:
        name = "Not Found"

    try:

        phone = driver.find_element(
            By.XPATH,
            f'/html/body/div[1]/div[2]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{index}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]'
        ).text

    except:
        phone = "Not Found"

    print(name, phone)

    names_list.append(name)
    phone_number_list.append(phone)

# //*[@id="89__uuXHif62"]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]
# //*[@id="89__uuXHif62"]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]


# name =//*[@id="89__uuXHif62"]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]
# name =//*[@id="89__uuXHif62"]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]
# //*[@id="89__uuXHif0"]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]
# /html/body/div[1]/div[2]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]

# /html/body/div[1]/div[2]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]
# /html/body/div[1]/div[2]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[5]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]

# name=/html/body/div[1]/div[2]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]
df=pd.DataFrame({
    'Name': names_list,
    'Phone Number': phone_number_list
})
df.to_csv('google_maps.csv', index=False)

driver.quit()