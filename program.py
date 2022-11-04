from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
CHROMEDRIVER = "./chromedriver.exe"

#C:/Users/Koichi Ito/Downloads/chromedriver_win32/chromedriver.exe

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    'download.default_directory' :'./downlord',
    "plugins.always_open_pdf_externally": True
})

print("検索したい用語を入力してください")
search_word=input()

print("何件ダウンロードしますか？（半角数字で入力してください）")
search_number=input()

# ドライバー指定でChromeブラウザを開く
browser = webdriver.Chrome(CHROMEDRIVER,options=options)


# Googleアクセス
browser.get('https://scholar.google.co.jp/schhp?hl=ja&as_sdt=0,5')
# 検索ボックスを特定
elem = browser.find_element(By.NAME, 'q')
# 「Selenium」と入力して、「Enter」を押す
elem.send_keys(search_word + Keys.RETURN)

time.sleep(1)

count = 0

while count <= int(search_number):
   
    if count !=0:
        next_element = browser.find_element(By.XPATH, '//*[@id="gs_nm"]/button[2]')
        next_element.click()

    for element in browser.find_elements(By.CLASS_NAME, "gs_ctg2"):
        if element.text == "[PDF]":
            element.click()
            count = count + 1
            #time.sleep(0.5)
            

print("pdfのダウンロードが終了しました。")


# ブラウザを閉じる
time.sleep(1)
browser.quit()
