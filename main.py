# Core libraries
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
    found_button = True

    driver = webdriver.Chrome(options=options, service=service)
    driver.get("https://pursuit.codetrack.dev/")
    wait = WebDriverWait(driver, 10)  # Increase the wait time to ensure the page fully loads
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='playerCardCollection__container']"))) 

# Find all the li elements within the ul element
    li_elements = wait.unit(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class='MuiPagination-ul css-nhb8h9']")))

    # Extract the text from each li element
    for li in li_elements:
        try:
            url_int = int(li.text)
            page_links.append(url_int)
        except:
            pass
    while found_button:
        try:
            container_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='playerCardCollection__container']")))
            print(container_div)
            player_divs = container_div.find_elements(By.CSS_SELECTOR, '.playerCard__notGraph')
            for player_div in player_divs:
                player_name = player_div.find_elements(By.CSS_SELECTOR, '.playerCard__name')
                player_score = player_div.find_elements(By.CSS_SELECTOR, '.playerCard__totalScore .playerCard__points')
                with open('player_scores.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    for name, score in zip(player_name, player_score):
                        writer.writerow([name.text, score.text])
            nextp_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Go to next page']")))
            if nextp_icon:
                nextp_icon.click()
        except:
            found_button = False
def main():
   # call your functions and print results to signal the user here and remove the 'pass' word below
    with open('player_scores.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['player_name', 'score']) 
    getCards()

if __name__ == "__main__":
    main()