import time
from selenium import webdriver
from selenium.webdriver.common.by import By

STORE_CAP = 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.implicitly_wait(2)

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
get_cookie = driver.find_element(By.ID, "cookie")


def get_cps():
    return float(driver.find_element(By.ID, "cps").text.split(":")[-1])


def buy(i):
    items_data["level"][i] += 1
    driver.find_element(by=By.ID, value=items_data["item_id"][i]).click()
    update_data(i)


def update_data(i):
    if i == 1:
        for level, power, index in zip(items_data["level"][2:5], range(1, 6), range(2, 5)):
            if level == 0:
                items_data["power"][index] += power
                items_data["price/power"][index] = round(items_data["price"][index] / items_data["power"][index], 2)

    items_data["power"][i] -= (i - 1) * items_data['level'][1] if i >= 2 and items_data["level"][i] == 1 else 0
    items_data["power"][1] += (i-1) if items_data["level"][i] == 1 and i >= 2 else 0
    items_data["price"][i] = get_price(items_data["item_id"][i])
    items_data["price/power"][i] = round(items_data["price"][i] / items_data["power"][i], 2)

    if i == 5:
        for value in items_data.values():
            value[i].remove()


def bank():
    return int(driver.find_element(By.ID, "money").text.replace(",", ""))


def get_price(id):
    time.sleep(0.03)
    return int(driver.find_element(By.ID, id).text.split("\n")[0].replace(",", "").split(' - ')[1])


items_data = {"item_id": [], "level": [0, 0, 0, 0, 0], "price": [], "power": [1, 4, 20, 50, 100], "price/power": []}
for item, index in zip(items, range(STORE_CAP)):
    item_id = item.get_attribute("id")
    price = get_price(item_id)

    items_data["item_id"].append(item_id)
    items_data["price"].append(price)
    items_data["price/power"].append(price/items_data["power"][index])


game = time.time() + (60 * 5)
shop_time = time.time()
shop_time += 1

while True:
    get_cookie.click()
    game_time = game - time.time()

    if shop_time < time.time():
        shop_time += 1

        best_price = min(items_data["price/power"])
        item_index = items_data["price/power"].index(best_price)
        price = items_data["price"][item_index]

        if price < bank() and game_time > 10:
            buy(item_index)

    if game_time < 3:
        for i in range(2, -1, -1):
            time.sleep(0.05)
            driver.find_element(by=By.ID, value=items_data["item_id"][i]).click()

    if game_time < 0:
        break

print(f"Your score is {get_cps()}cps.")