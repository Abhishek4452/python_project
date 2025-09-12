#enumerate function
marks = [12,23,3,4,56,67,78,8,9,9,7]
for index,mark in enumerate(marks,start = 1):
    print(index,mark)
    if(index == 5):
        print("number available")
        
    