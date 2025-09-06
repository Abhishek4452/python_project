# write an code which fetch the data from the server of news api and show us the headline of the today nws
# they uses the request module to done all this things
# use command line or some sort of creativity to get the particular news of the particular source
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import platform
import os
 
url ='https://realpython.com/beautiful-soup-web-scraper-python/'
response = requests.get(url)


soup = BeautifulSoup(response.text,'html.parser')#scraping data
headlines = soup.find('body').find_all('h3')#selected headlines
texts = headlines #text save
language = 'en'#language set

mytext = gTTS(text = texts,lang = language,slow = False)#call the function
mytext.save("language-file.mp3")#save the file

system_name = platform.system()#knowing the system
if system_name == "windows":
    os.system("start language-file.mp3")
elif system_name =="Linux":
    os.system("xdg-open language-file.mp3")
else:
    os.system("open language-file.mp3")


# for x in headlines:
#     print(x.text.strip())


