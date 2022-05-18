import time

from selenium import webdriver

chrome_driver_path = "C:/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
print(timeout)
five_min = time.time() + 60
items=driver.find_elements_by_css_selector("#store div")
item_ids=[item.get_attribute("id") for item in items]

while True:
    cookie.click()
    if time.time() > timeout:
        item_prices=[]
        all_prices=driver.find_elements_by_css_selector("#store b")
        for price in all_prices:
            element_text=price.text
            if element_text !="":
                item_price=int(element_text.strip().split("-")[1].strip().replace(",",""))
                item_prices.append(item_price)
        cookie_upgrades={}
        # create a dictionary to store item and prices
        print(item_ids)
        print(item_prices)
        print(len(item_ids),len(item_prices)) # len item_ids=9,item_prices=8
        for i in range(len(item_prices)):
            cookie_upgrades[item_ids[i]]=item_prices[i]

        total_cookies=driver.find_element_by_css_selector("#money").text
        print(total_cookies)
        affordable_prices=[price for price in item_prices if price <= int(total_cookies)]
        max_price=max(affordable_prices)
        print(affordable_prices)
        print(max_price)
        max_buyable_cookie_id=list(cookie_upgrades.keys())[list(cookie_upgrades.values()).index(max_price)]
        print(max_buyable_cookie_id)
        driver.find_element_by_id(max_buyable_cookie_id).click()

        timeout=time.time()+5
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

