import random,time

Fruits = ['apple','banana','grapes']
Colors = ['blue','green','red']

category = ""
secret_word_list = []
GuessLetter = ""
GuessLetter_list = []
secret_word = ""


#welcome page 
name = input("Enter your name : ")
time.sleep(0.2)
print(f"Welcome {name} to the game!")
time.sleep(0.2)

print("This is a word guessing game")
time.sleep(0.2)

print("You are allowed to guess only one alphabet at a time")
time.sleep(0.2)

print("lets begin")
time.sleep(0.2)

category =int(input("Please select the category:\n1. Fruits\n2. Colours\n"))
if category == 1:
    secret_word = random.choice(Fruits)
elif category == 2:
    secret_word = random.choice(Colors)   
else:
    print("Please select the appropriate category")

if category==1 or category ==2:

    for word in secret_word:
        print("*",end="")
    print('\n')

    secret_word_list = list(secret_word)
    attempts = (len(secret_word)+2)

    while len(secret_word_list)!=0 and attempts>0:

        GuessLetter = input("Enter the letter you want to try : ").lower()
        attempts -= 1
        if GuessLetter in secret_word_list:
            secret_word_list.remove(GuessLetter)
            print("Nice Guess!")
            if  attempts>1:
                print("You have ", attempts, ' guess left!')
        
        elif GuessLetter not in secret_word_list and attempts>0:
            print("Oops! Try again.")
            print("You have ", attempts, 'guess left!')
                
        if len(secret_word_list)==0:
           print('The word is {}'.format(secret_word))
           print("You won!")
        else:
           print("Try agian next time")











