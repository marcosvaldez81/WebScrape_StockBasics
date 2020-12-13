import requests
from bs4 import BeautifulSoup
import time # for wait time
import csv
from datetime import date # for date
import send_mail

urls = ["https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch", "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch", "https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch", "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]

headers = {}
today = str(date.today()) + ".csv"
with open(today, "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'DayRange', '52 Week Range', 'Volume', 'Avg. Volume', 'Market Cap', 'Beta(5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est'])



    for url in urls:
        stock = []
        html_page = requests.get(url,headers = headers)
        soup = BeautifulSoup(html_page.content, 'lxml')

        #title = soup.find("title").get_text() #for getting rid of <title>
        header_info = soup.find_all("div", id = "quote-header-info")[0]
        stock_title = header_info.find("h1").get_text();
        current_price = header_info.find("div", class_= "My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text();
        stock.append(stock_title)
        stock.append(current_price)
        table_info = soup.find_all("div", id = 'quote-summary')[0]
        stock_info = table_info.find_all("div", class_ = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")
        stock_info2 = table_info.find_all("div", class_ = "D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)")[0].find_all("tr")

        for i in range(0,8):
            heading = stock_info[i].find_all("td")[0].get_text()
            value = stock_info[i].find_all("td")[1].get_text()
            stock.append(value)


        print(" ")
        for i in range(0,8):
            heading2 = stock_info2[i].find_all("td")[0].get_text()
            value2 = stock_info2[i].find_all("td")[1].get_text()
            stock.append(value2)
        writer.writerow(stock)
    time.sleep(10) # wait time of 10 seconds for each stock

file.close()
send_mail.send(filename = today)
