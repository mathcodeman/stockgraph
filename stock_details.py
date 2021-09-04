import requests
from bs4 import BeautifulSoup

class stock_detail:
    def __init__(self,stock_symbol):
        r=requests.get(f"https://www.gurufocus.com/stock/FB/summary?search=fb")
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all=soup.find_all("div",{"class":"stock-summary-table fc-regular"})
        self.a=all[0].find_all(attrs={"data-v-5d68188a":""})

    def get_Volume(self):
        try:
            Volume=self.a[1].text.strip(" ")
            return print(Volume)
        except:
            return None

    def get_Avg_Vol(self):
        try:
            Avg_Vol=self.a[3].text.strip(" ")
            return print(Avg_Vol)
        except:
            return None

    def get_PE(self):
        try:
            PE=self.a[9].text.strip(" ")
            return print(PE)
        except:
            return None

    def get_PB(self):
        try:
            PB=self.a[11].text.strip(" ")
            return print(PB)
        except:
            return None
    
    def get_Market_Cap(self):
        try:
            Market_Cap=a[5].text.strip(" ")
            return print(Market_Cap)
        except:
            return None

