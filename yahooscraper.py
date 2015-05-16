#!usr/bin/env python

'''
_Script_ : YahooDataFetcher 
_Author_ : Debapriya Das

Description : this script fetches the S&P 500 Companies list from Wikipedia
and downloads their data as csv/table files from Yahoo Finance in the current directory
good for fetching data

'''



from lxml import html
import requests
import os
import time


 
 
def fetch_table():
    page = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    tree = html.fromstring(page.text)
    xpath = '//*[@id="mw-content-text"]/table[1]'
    rows = tree.xpath(xpath)[0].findall("tr")
    rows = [(row.getchildren()[0],row.getchildren()[3]) for row in rows[1:]]
    rows = [(row[0].getchildren()[0].text, row[1].text) for row in rows]
 
    from collections import defaultdict
    sectors = defaultdict(list)
    for row in rows:
        sectors[row[1]].append(row[0])
 
    for sector in sectors:
        print
        print sector
        folder = sector.replace(' ','_') 
        if not os.path.exists(folder):
            os.mkdir(folder)
        for ticker in  sectors[sector][:10]:
            print "Downloading {}...".format(ticker)
            link = "http://real-chart.finance.yahoo.com/table.csv?s={}&a=11&b=1&c=2014&d=04&e=16&f=2015&g=d&ignore=.csv".format(ticker)
            cmd = "wget {} -P /tmp/{}/".format(link, folder)
            print cmd
            os.system(cmd)
            time.sleep(3)    
            os.system("mv table.csv\?s={} /tmp/{}/{}.csv".format(ticker, folder, ticker))


            
''' 
def remove_old_stocks():
    import commands;
    files = commands.getstatusoutput("find . -name *.csv")[1]
    files = [f for f in files.split('\n') if 'csv' in f]
   
    from datetime import date
    compare_date = lambda d : date(2014,1,1) <= date(*map(int, d[0].split("-")))
 
    import csv
    for f in files:
        with open(f, 'rb') as fin:
            reader = csv.reader(fin)
            rows = [row for row in reader]
 
        header = rows[0]
        rows = rows[1:]
 
        rows = filter(compare_date, rows)
 
        with open(f, 'wb') as fout:
            writer = csv.writer(fout)
            writer.writerow(header)
            for row in rows:
                writer.writerow(row)
 '''



if __name__ == '__main__':
    fetch_table()
    
    
