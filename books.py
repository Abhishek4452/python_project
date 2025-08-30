#books = {take the list of book data from user and save her here}
# book_number == len(books)
books = []
iota=0
def insert():
     while True :
         a = input("enter the data : ")
         if a == "c":
             
             break
         else:
             global books
             books.append(a) 
             global iota
             iota+=1    


#books = {take the list of book data from user and save her here}
# book_number == len(books)
books = []
iota=0
def insert():
     while True :
         a = input("enter the data : ")
         if a == "":
             
             break
         else:
             global books
             books.append(a) 
             global iota
             iota+=1    



insert()
print('-----   items in the books list are :  ------------ ')
for i in books:
    print(i)

#match case 
if(len(books)== iota):
    print("number of books are match iota+=1  d you are done with it")
    print(len(books), end = " ")

    print('=', end = " ")
    print(iota)
    

insert()
print('-----   items in the books list are :  ------------ ')
for i in books:
    print(i)

#match case 
if(len(books)== iota):
    print("number of books are match iota+=1  d you are done with it")
    print(len(books), end = " ")

    print('=', end = " ")
    print(iota)
    
