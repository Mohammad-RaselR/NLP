from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScm69vuwbZIUQ1Zg3gVbKwbgRSU3z0L9BPrbGkJ8Iu3l8fqMQ/viewform?usp=dialog")
driver.maximize_window()
test_data=[
    ('Raselhosen229@gmail.com','Mohammad Rasel', '01789777317' ),
    ('mrhrasel229@gmail.com',' Rasel', '01516594220' ),
]

for i, (email, name, phone) in enumerate(test_data):
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').clear()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').clear()
    # driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').clear()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').clear()


    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)
    # driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(date)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(phone)
    # click submit button 
    
    driver.find_element(By.TAG_NAME, "form").submit()
    # if submit button hit then print successfully submitted
    print(f"Test case {i+1} submitted successfully.")

    # driver.find_element(By.XPATH, 'form').submit()

    # time.sleep(5)

    # email_input.send_keys(email)
    # name_input.send_keys(name)
    # date_input.send_keys(date)
    # phone_input.send_keys(phone)

time.sleep(5)