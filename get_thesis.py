#! /usr/local/bin/python3
from functools import partial
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROMEDRIVER = "C:/Users/Koichi Ito/Downloads/chromedriver_win32/chromedriver.exe"

#browser = webdriver.Chrome(CHROMEDRIVER)

url = "https://pubs.acs.org/toc/jacsat/0/0" #JACS の ASAP ページ
keyword = "Education" #論文タイトルの検索キーワード
#PDF download 用の設定

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
                                "download.prompt_for_download": False,
                                "download.directory_upgrade": True,
                                "plugins.plugins_disabled": ["Chrome PDF Viewer"],
                                "plugins.always_open_pdf_externally": True
                                })
options.add_argument("--disable-extensions")
options.add_argument("--disable-print-preview")
driver = webdriver.Chrome(CHROMEDRIVER,options=options)
driver.get(url)
time.sleep(2)
PDF = []
for a in driver.find_elements(By.PARTIAL_LINK_TEXT,"PDF"):
    PDF.append(a.get_attribute("href"))
TITLE = []
for a in driver.find_elements(By.CLASS_NAME, "issue-item_title"):
    TITLE.append(a.text + ".pdf")
i = 0
for a in TITLE:
    if keyword in a:
        driver.get(PDF[i])
        time.sleep(2)
    i += 1
time.sleep(20)
driver.quit()