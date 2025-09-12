#here i will learn the basic os module and its working
import os
if not os.path.exists("data"):
    os.mkdir("data")

for i in range(1,100):
    #os.rmdir(f"data\day{i}")       # for removing the directory 
    os.mkdir(f"data/day{i}")       #for making the file
    