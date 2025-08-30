#here we use a library which will take words from us and convert those words into the text format
# this is helpful when we are not able to communicate with any other person which is deaf
from gtts import gTTS # goggle text to speech module
import os
import platform # to check which system is running on
import time

mytext = "sout out to abhishek pokhriyal from GBPIET pauri garhwal"
language = "en" #english language is selected
myfile = gTTS(text=mytext, lang =language,slow =False)

myfile.save("language-file.mp3")

system_name = platform.system()
time.sleep(3)
print(system_name)
if system_name == "windows":
    os.system("start language-file.mp3")
elif system_name =="Linux":
    os.system("xdg-open language-file.mp3")
else:
    os.system("open language-file.mp3")

#os.system("xdg-open language-file.mp3")
