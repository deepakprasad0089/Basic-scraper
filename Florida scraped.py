from pandas import DataFrame
from bs4 import BeautifulSoup
#import requests
from urllib.request import Request,urlopen

name=[]
email=[]
address=[]
def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)

    return de 

u=="https://www.floridabar.org/directories/find-mbr/?lName=&sdx=N&fName=Hugh&eligible=N&deceased=N&firm=&locValue=&locType=C&pracAreas=&lawSchool=&services=&langs=&certValue=&pageNumber=1&pageSize=50"
requests.get 
s=BeautifulSoup (

url=f"https://www.floridabar.org/directories/find-mbr/?lName=&sdx=N&fName=Hugh&eligible=N&deceased=N&firm=&locValue=&locType=C&pracAreas=&lawSchool=&services=&langs=&certValue=&pageNumber={i}&pageSize=50"
headers = {"User-Agent":"Mozilla/5.0"}

page_req=Request(url,headers=headers)
page=urlopen(page_req)

soup=BeautifulSoup(page,'html.parser')
#print(soup.prettify())

link=soup.find_all('div',attrs={'class':'profile-contact'})
l=soup.find_all('p',attrs={'class':'profile-name'})


for i,j in zip(link,l):
    e=i.find('a',attrs={"class":"icon-email"}).get('href')
    name.append(j.text)
   # print(j.text)
    address.append(i.find('p').text)
    #print(i.find('p').text)
    #print(i)
  
    #print(e)
    #print(e[28:])
    p=decodeEmail(e[28:]) 
    email.append(p)
   # print(p)
    #print("\n")

for i in range(0,len(email)):
    print(name[i])
    print(email[i])
    print(address [i])
    print("\n")


#zipped=list(zip(name,address,email))
#dfObj = pd.DataFrame(zippedList, columns = ['Name' , 'Age', 'City'])
people=[name,email,address]
df=DataFrame(people).transpose()
df.columns=['Name','Email','Address']
df.style.set_properties(**{'text-align': 'right'})
print (df)
