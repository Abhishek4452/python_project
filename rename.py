#write an function which will take the file file your computer and rename her into an sequence of name
# ex--
# abhi.png --> 1.png
# aman.png --> 2.png
#deepak.png -->3.png

import os
#check folder exit or not
if not os.path.exists("photo"):
    print("folder does not exits")
    exit()
else:
    print("folder exists")
print("      older name of the files are : ------- ")
listsss = os.listdir("photo")
#print(listsss)#for printing sequence of the files
for files in listsss:
    print(f"{files}")
i=1
print(" ----   new name was give to list    --------")
for q in listsss:
    os.rename(f"photo/{q}",f"photo/{i}.png")
    print(f"photo/{i}.png")
    i+=1