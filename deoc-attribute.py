#doc attribute use in python
# doc attribute help user to understand the behaviour of the doucment in the python
# rasing custom error

def square(n):
    ''' take a number and return its square'''
    if (n>5):
        print(n*n)
    else:
        raise ValueError("need to enter value greater than 5 ")


square(int(input("enter a number : ")))
print(square.__doc__)#help us to understand what is the comment written inside the function square
