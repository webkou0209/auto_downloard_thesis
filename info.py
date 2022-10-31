from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import datetime


def get_search_results_df(keyword,number):
    columns = ["rank", "title", "writer", "year", "citations", "url"]
    df = pd.DataFrame(columns=columns) #表の作成
    html_doc = requests.get("https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&num=" + str(number) + "&q=" + keyword).text
    soup = BeautifulSoup(html_doc, "html.parser") # BeautifulSoupの初期化
    tags1 = soup.find_all("h3", {"class": "gs_rt"})  # title&url
    tags2 = soup.find_all("div", {"class": "gs_a"})  # writer&year
    tags3 = soup.find_all(text=re.compile("引用元"))  # citation

    rank = 1
    for tag1, tag2, tag3 in zip(tags1, tags2, tags3):
        title = tag1.text.replace("[HTML]","")
        url = tag1.select("a")[0].get("href")
        writer = tag2.text
        writer = re.sub(r'\d', '', writer)
        year = tag2.text
        year = re.sub(r'\D', '', year)
        citations = tag3.replace("引用元","")
        se = pd.Series([rank, title, writer, year, citations, url], columns)
        df = df.append(se, columns)
        rank += 1
    return df



keyword = "教育工学" #ここに調べたいキーワードを入力
number = 10 #数を入力
search_results_df = get_search_results_df(keyword,number)
d_today = datetime.date.today()
filename = "./result/"+ str(d_today) + "_"+keyword + ".csv"
search_results_df.to_csv(filename, encoding="shift-jis")
