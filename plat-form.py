import platform
# platfrom module help us to know our system
import os

print(platform.system())# in which system we are working on

print(platform.release())# which 6.12.41+deb13-amd64

print(platform.machine())# x-86_64

print(platform.processor())

print(platform.python_version())# python version will print out

print(platform.platform())# give platform data

try:
    if platform.system() =="Window":
        print("hey you are working in window")

    elif platform.system()=="Linux":
        print("hey you are working in linux")
    else:
        print("please mention your system in code")
    os.system("git status")
    if os.system("git status")== 0:
        os.system("git add . ")
        comment = input("please enter comment for repository :  ")
        os.system(f"git commit -m'{comment}'  ")
        os.system("git push origin main")
    else: 
        print('updated all')
except:
    print('some error occured')