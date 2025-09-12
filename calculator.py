

def calc(a,b):
   
    print("enter - 1 to perform addtion ")
    print("enter - 2 to perform subtraction ")
    print("enter - 3 to perform divison ")
    print("enter - 4 to perform multiplication ")
    print("enter - 5 to perform reminder ")

    num = int(input("enter the input value \n"))
    
    if(num == 1):
        print(a+b)
    elif(num == 2):
        print(a-b)
    elif(num == 3):
        print(a/b) 
    elif(num == 4):
        print(a*b)
    elif(num == 5):
        print(a%b)
    else :
        exit

if __name__ == "__main__":
    print("hello welcome to my calculator")
    print("hello we have enter the main function : ")

    for i in range(5):
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))
        calc(num1,num2)


    print("I AM EXIT NOW")