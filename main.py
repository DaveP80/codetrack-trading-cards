# Core libraries
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from open_gen import get_completion

CHROMEDRIVER_PATH = '/usr/bin/chromedriver'

def getCards():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    page_links = []
    unique_rows = set()
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
    driver.quit()
    for n in range(page_links[-1]):
        try:
            chrome_driver = webdriver.Chrome(service=service, options=chrome_options)
            wait = WebDriverWait(chrome_driver, 10)
            chrome_driver.get(f"https://pursuit.codetrack.dev/?page={n+1}")
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
            chrome_driver.quit()
        except NoSuchElementException as e:
            logging.error(e)
    if page_links:
        make_json(page_links)
    
            
def main():
   # call your functions and print results to signal the user here and remove the 'pass' word below
    with open('player_scores.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['player_name', 'score']) 
    getCards()

def make_json(page_links):
    if page_links:
        get_completion("player_scores.csv")

def container():
    while True:
        pass

if __name__ == "__main__":
    main()
    container()
