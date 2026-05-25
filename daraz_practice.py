from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://www.daraz.com.bd/products/tranparent-frame-clear-glass-for-men-i209430532-s1159686217.html"
)

time.sleep(5)

# scroll to review section
height = driver.execute_script(
    "return document.body.scrollHeight"
)

for i in range(0, height, 70):

    driver.execute_script(
        f"window.scrollTo(0, {i});"
    )

    time.sleep(0.03)

all_comments = []

visited_pages = set()

total_pages = 145

# scrape first page
comments = driver.find_elements(
    By.CLASS_NAME,
    'content'
)

for c in comments:

    txt = c.text.strip()

    if txt != "":

        all_comments.append(txt)

visited_pages.add(1)

current_page = 2

while current_page <= total_pages:

    try:
# //*[@id="module_product_review"]/div/div/div[3]/div[2]/div
# //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div
# //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[1]
        buttons = driver.find_elements(
            By.XPATH,
            '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button'
        )

        numeric_buttons = []

        for btn in buttons:

            txt = btn.text.strip()

            if txt.isdigit():

                numeric_buttons.append((int(txt), btn))

        # sort buttons
        numeric_buttons.sort(key=lambda x: x[0])

        # find current page button
        target_btn = None

        for num, btn in numeric_buttons:

            if num == current_page:

                target_btn = btn
                break

        if target_btn is None:
            print("Page button not found:", current_page)
            break

        driver.execute_script(
            "arguments[0].click();",
            target_btn
        )

        print("Clicked Page:", current_page)

        time.sleep(3)

        comments = driver.find_elements(
            By.CLASS_NAME,
            'content'
        )

        print("Comments:", len(comments))

        for c in comments:

            txt = c.text.strip()

            if txt != "":

                all_comments.append(txt)

                print(txt)

                print("----------------")

        visited_pages.add(current_page)

        current_page += 1

    except Exception as e:

        print("Error:", e)

        break

# save CSV
df = pd.DataFrame({
    "Comments": all_comments
})

df.to_csv("daraz_comments.csv", index=False)

print("CSV Saved Successfully")

print("Total Comments:", len(all_comments))

driver.quit()