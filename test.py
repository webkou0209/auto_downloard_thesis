from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
CHROMEDRIVER = "C:/Users/Koichi Ito/Downloads/chromedriver_win32/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    'download.default_directory' :'~/Download',
    "plugins.always_open_pdf_externally": True
})

print("検索したい用語を入力してください")
search_word=input()

# ドライバー指定でChromeブラウザを開く
browser = webdriver.Chrome(CHROMEDRIVER,options=options)


# Googleアクセス
browser.get('https://scholar.google.co.jp/schhp?hl=ja&as_sdt=0,5')
# 検索ボックスを特定
elem = browser.find_element(By.NAME, 'q')
# 「Selenium」と入力して、「Enter」を押す
elem.send_keys(search_word + Keys.RETURN)

time.sleep(1)
for element in browser.find_elements(By.CLASS_NAME, "gs_ctg2"):
    if element.text == "[PDF]":
        element.click()
        time.sleep(1)

next__content = browser.find_elements(By.CLASS_NAME, "gs_btnPR gs_in_ib gs_btn_lrge gs_btn_half gs_btn_lsu")
next__content.click()

print("pdfのダウンロードが終了しました。")
time.sleep(10)

# ブラウザを閉じる
browser.quit()

#<span class="gs_ctg2">[PDF]</span>
#PARTIAL LINK TEXT