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
print("Welcome {} to the game!".format(name))
time.sleep(1)
print("This is a word guessing game")
time.sleep(1)
print("You are allowed to guess only one alphabet at a time")
time.sleep(1)
print("lets begin")
time.sleep(1)
category =input("Please select the category(Fruits/Colors) :")
if category == 'Fruits':
    secret_word = random.choice(Fruits)
elif category == 'Colors':
    secret_word = random.choice(Colors)
else:
    print("Please select the appropriate category")

for word in secret_word:
    print("*",end="")
print('\n')
print(secret_word)
    
        
        

secret_word_list = list(secret_word)
attempts = (len(secret_word)+2)

while attempts>0:

    GuessLetter = input("Enter the letter you want to try : ").lower()
    if GuessLetter in GuessLetter_list:
        print("Alphabet is already guessed earlier! please try any other letter")
    else:
        attempts -= 1
        GuessLetter_list.append(GuessLetter)
        if GuessLetter in secret_word_list:
            print("Nice Guess!")
            
            if attempts>0:
                print("Number of attempts left is {}".format(attempts))
            for i in range(len(secret_word_list)):
                if GuessLetter == secret_word_list[i]:
                   LetterIndex = i
                   GuessLetter_list[LetterIndex] = GuessLetter
        else:
            print("Oops! Try again.")
            print("You have ", attempts, 'guess left!')
                

    
WordJoined = [''.join(GuessLetter_list)]
if secret_word == WordJoined:
    print("You won!")
else:
    print("Too many failed attempts, please try again!")







        
















