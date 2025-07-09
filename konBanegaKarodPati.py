print("  SWAGAT HAI AAP KA KNO BANEGA KAROD PATI SHOW MAI ")
name =input("Enter your name : ")

print(f" To pehla sawal apki screen paar {name} ji")
sum = 0
# output match
def output(x):
    list = [4,3,4,2,3]
    return list[x-1]
# winning
def winning(c):
    list = ["1,000","5,000","10,000","20,000","50,000"]
    return list[c-1]

#FUNCTION TO ASK THE QUESTION
def fun(num):
    print("")
    match num:
        case 1:
             print("Who was the first Prime Minister of India?")
             print("1) Mahatma Gandhi")
             print("2) Sardar Vallabhbhai Patel")
             print("3) Dr. B.R. Ambedkar")
             print("4) Jawaharlal Nehru")
        case 2:
             print("What is the national animal of India?")
             print("A) Lion")
             print("B) Elephant")
             print("C) Bengal Tiger")
             print("D) Leopard")
        case 3:
             print("Which is the longest river in India?")
             print("A) Yamuna")
             print("B) Brahmaputra")
             print("C) Godavari")
             print("D) Ganga")
        case 4:
             print("who wrote the Indian national anthem Jana Gana Mana?")
             print("A) Bankim Chandra Chatterjee")
             print("B) Rabindranath Tagore")
             print("C) Sarojini Naidu")
             print("4) Jawaharlal Nehru")
        case 5:
             print(" In which year did India gain independence from British rule?")
             print("A) 1950")
             print("2) 1930")
             print("3) 1947")
             print("4) 1919")                    
        case _ :
             print("GAME OVER")     
for i in range(1,6):
    print(fun(i))
    #input from user
    a = int(input("chosse your option : "))
    print(output(i))
    if a == output(i):
        print("good job you have give the right answer,you have earn: ",winning(i))
        sum = winning(i)
    else :
        print("you lost , your bad!")
        break


print("")
print(f"THANK YOU FOR JOINING US {name}")
print(f"game end! you have earned {sum} try again late ")
print("What will you this with this money")

        