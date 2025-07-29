import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

def login_to_amazon(username, password):
    try:
        driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26tag%3Dgooghydrabk1-21%26ref%3Dnav_ya_signin%26adgrpid%3D155259813593%26hvpone%3D%26hvptwo%3D%26hvadid%3D713930225169%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D8610212928063929876%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D1007824%26hvtargid%3Dkwd-64107830%26hydadcr%3D14452_2402225%26gad_source%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        ).send_keys(username)
        driver.find_element(By.ID, "continue").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        ).send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()
        time.sleep(2)
    except Exception as e:
        print(f"Login failed: {e}")

def scrape_amazon(driver):
    extracted_data = []
    category_links = [
        "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0",
        "https://www.amazon.in/gp/bestsellers/mobile-apps/ref=zg_bs_nav_mobile-apps_0",
        "https://www.amazon.in/gp/bestsellers/luggage/ref=zg_bs_nav_luggage_0",
        "https://www.amazon.in/gp/bestsellers/beauty/ref=zg_bs_nav_beauty_0",
        "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_books_0",
        "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
        "https://www.amazon.in/gp/bestsellers/apparel/ref=zg_bs_nav_apparel_0",
        "https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0",
        "https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0",
        "https://www.amazon.in/gp/bestsellers/garden/ref=zg_bs_nav_garden_0"
    ]
    
    for category_url in category_links:
        try:
            driver.get(category_url)
            time.sleep(5)
            
            products = driver.find_elements(By.XPATH, '//div[contains(@class, "_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")]')
            prices = driver.find_elements(By.XPATH, '//span[contains(@class, "_cDEzb_p13n-sc-price_3mJ9Z")]')
            for product, price in zip(products, prices):
                title = product.text if product else "N/A"
                price_text = price.text if price else "N/A"
                extracted_data.append({
                    'Title': title,
                    'Price': price_text
                })
        except Exception as e:
            print(f"Error scraping {category_url}: {e}")
    return extracted_data

def save_to_csv(data, filename):
    try:
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error saving CSV file: {e}")

try:
    username = "your username"#replace
    password = "your password"#replace
    login_to_amazon(username, password)
    data = scrape_amazon(driver)
    save_to_csv(data, "best_sellers.csv")
finally:
    driver.quit()