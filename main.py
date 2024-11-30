# Core libraries
import logging
from dotenv import load_dotenv    # API key management
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import re
from tempfile import mkdtemp
import csv

def getCards():

    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/opt/chromedriver")

    options.binary_location = '/opt/chrome/chrome'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options, service=service)
    page_links = []
    unique_rows = set()
    found_button = True

    driver = webdriver.Chrome(options=options, service=service)
    driver.get("https://pursuit.codetrack.dev/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='playerCardCollection__container']"))) 
# Find all the li elements within the ul element
    ul_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class='MuiPagination-ul css-nhb8h9']")))
    li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
    # Extract the text from each li element
    for li in li_elements:
        try:
            url_int = int(li.text)
            page_links.append(url_int)
        except ValueError:
            pass
    for n in range(page_links[-1]):
        try:
            driver.get(f"https://pursuit.codetrack.dev/?page={n+1}")
            container_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='playerCardCollection__container']")))
            print(container_div)
            player_divs = container_div.find_elements(By.CSS_SELECTOR, '.playerCard__notGraph')
            for player_div in player_divs:
                player_name = player_div.find_elements(By.CSS_SELECTOR, '.playerCard__name')
                player_score = player_div.find_elements(By.CSS_SELECTOR, '.playerCard__totalScore .playerCard__points')
                if len(player_name[0].text) > 2:
                    with open('player_scores.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        row_tuple = tuple([player_name[0].text, player_score[0].text])
                        if row_tuple not in unique_rows:
                            writer.writerow([player_name[0].text, player_score[0].text])
                            unique_rows.add(row_tuple)
            time.sleep(1)
        except NoSuchElementException as e:
            logging.error(e)
            
def main():
   # call your functions and print results to signal the user here and remove the 'pass' word below
    with open('player_scores.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['player_name', 'score']) 
    getCards()

if __name__ == "__main__":
    main()