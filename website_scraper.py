from bs4 import BeautifulSoup
import requests
import csv

r=requests.get("https://www.gadgetsnow.com/?utm_source=toiweb&utm_medium=referral&utm_campaign=toiweb_hptopnav").text

soup=BeautifulSoup(r,"lxml")

csv_file=open("gadgets_now_tech_latest.csv",'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Title','Link'])

for item in soup.find_all("span",class_="w_tle"):
    title=item.text.replace("\n","")
    print(title)
    link=item.a['href']
    st="https://www.gadgetsnow.com"
    if st in link:
        link=link.replace(st,"")
    link=st+link
    print(link)
    csv_writer.writerow([title,link])
    print()
csv_file.close()


