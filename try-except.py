a = input("enter the number : ")

# exception handling in by using the try and except statment

try:
    print(f"multiplication table of {int(a)} is : ")#error occur if the variable a is not of integer type
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except ValueError:# when value error occur then print this other wise something else
    print("please enter some value not the character : ")
    
except Exception as e:
    print(e)
    print(" ------ error occur ----- ")
    print("keep trying with other number")

print("have a nice day bro ")