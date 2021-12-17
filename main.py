# pip install chromedriver_binary=="使用しているchromeのバージョン"(適合するものがなければ近いものを)

import chromedriver_binary  # noqa: F401
from selenium import webdriver
import csv

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)


def access_url(url):
    driver.get(url)
    print(driver.current_url)
    x = driver.find_elements_by_css_selector('div#tab-data-qa-reviews-0 div.Iwpns div.bPhtn span.NejBf')
    texts = [i.text for i in x]
    print(texts)
    # 手動で空のtext.csvを作成してください
    with open('text.csv', 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(texts)
    return texts


# レビュー数に応じてrangeの値を手動で変更（レビュー数/10）
for urlnum in range(92):
    urlnum = urlnum*10
    # "~.com"なら英語レビュー、"~.jp"なら日本語レビューを取得できます
    url_1 = "https://www.tripadvisor.com/Attraction_Review-g298153-d1675920-Reviews-"
    url_2 = "or"+str(urlnum)
    url_3 = "-Otaru_Canal-Otaru_Hokkaido.html"
    url = url_1+url_2+url_3
    access_url(url)
