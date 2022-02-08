import cloudscraper
from bs4 import BeautifulSoup
import re

def ethpullacc():
    accounts = []
    balance = []
    for i  in range(1, 5):
        scraper = cloudscraper.create_scraper()  
        site = scraper.get("https://etherscan.io/accounts/" + str(i)).text
        soup = BeautifulSoup(site, 'html.parser')
        sa = soup.findAll("a")
        #sa2 = soup.findAll('td', text = re.compile" Ether")
        for word in sa:
            if word.text.startswith("0x"):
                accounts.append(word.text)
    return accounts
def ethpullbal():
    accounts = []
    balance = []
    for i  in range(1, 5):
        scraper = cloudscraper.create_scraper()  
        site = scraper.get("https://etherscan.io/accounts/" + str(i)).text
        soup = BeautifulSoup(site, 'html.parser')
        sa2 = soup.findAll('td')
        for wo in sa2:
            if wo.find('span') and wo.text.startswith("0x")!=1:
                res = wo.text.rpartition("Ether")[0]
                resu = res.replace(',', '')
                lo = float(resu)
                balance.append(lo)
            elif any(c.isdigit() for c in wo.text) and wo.find(text = re.compile("Ether")):
                res = wo.text.rpartition("Ether")[0]
                resu = res.replace(',', '')
                lo = float(resu)
                balance.append(lo)
    return balance
    print(len(accounts))
    print(balance)