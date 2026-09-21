import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By

url = "LINK TOKOPEDIA"  # Ganti dengan URL Tokopedia yang ingin diambil reviewnya
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)
data = []

for i in range(0, 10):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs={'class': 'css-1pr2lii'})

    for container in containers:
        review_element = container.find(
            'span',
            attrs={'data-testid': 'MASUKAN ELEMEN HTML REVIEWS'})
        if review_element is None:
            continue
        review = review_element.get_text(strip=True)

        rating_element = container.find('div', attrs={'data-testid': 'MASUKAN ELEMEN HTML RATING'})
        if rating_element is not None:
            rating = rating_element.get('aria-label')
            rating_parent = rating_element.find_parent('div')
            date_element = rating_parent.find('p', attrs={'data-unify': 'Typography'}) if rating_parent else None
            tanggal = date_element.get_text(strip=True) if date_element else None
        else:
            rating = None
            tanggal = None

        print(review)
        print(rating)
        print(tanggal)
        data.append((review, rating, tanggal))

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='MASUKAN LABEL CLICK HALAMAN BERIKUTNYA']").click()
    time.sleep(3)
    print(data)

df = pd.DataFrame(data, columns=['Review', 'Rating', 'Tanggal'])
df.to_csv("data/tokped_reviews.csv", index=False)
driver.close()