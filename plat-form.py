import platform
# platfrom module help us to know our system
# using mainly for working in cross platform compatibility and diagnose
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

     # pushing the code in repo   
    os.system("git status")
    os.system("git add . ")
    comment = input("please enter comment for repository :  ")
    os.system(f"git commit -m'{comment}'  ")
    os.system("git push origin main")
except Exception as e:
    print('some error occured', e)