import random

print("""\nWelcome to the hangman game. The objective of the game is to find the correct word by inputing the 
correct individual letters (one letter at a time) into the program.You only have 7 attempts to guess the word, and the 
letters should be between A-Z, all lowercase, no symbols, and no numbers. If you are to input more than one letter into the program
or anything but lowercase letters you will lose an attempt. Good luck!\n""")

print("""------------
|          |
|           
|        
|        
|          
|_____________\n        
""")


allWords = ["basketball", "actually", "gaming", "student", "teacher", "school", "impossible", 
        "cryptic", "classes", "hyper", "airport", "beyond", "infinity", "enormous", 
        "reverberate", "intelligent", "alarm", "phantom", "calculator", "cosmic"]

randomWordNumber = random.randint(0,19)
word = allWords[randomWordNumber]
word_list = list(word)

def solver(word, word_list):
    attempts = 8
    dash_word = ""
    dash_list = []
    input_list = []
    attempts = 8
    for i in word:
        dash_list.append("-")

    for z in dash_list:
            dash_word += z
    
    print(dash_word, "\n")
    print("You have", attempts - 1, "attempts left!\n")

    while True:
        user_input = str(input("Please enter any lowercase letter between A-Z: "))
        count = -1
        while True:
            if user_input in dash_list or user_input in input_list:
                user_input = str(input("You have already used this letter, select a new one: "))
            else:
                break
        input_list.append(user_input)
        for i in word_list:
            count += 1
            if user_input in word:
                for x in dash_list:
                    if user_input == i:
                        dash_list[count] = user_input

        if user_input not in word:
            attempts = attempts - 1

        gallow(attempts)

        dash_word = ""
        for z in dash_list:
            dash_word += z

        print(dash_word, "\n")
        print("You have", attempts - 1, "attempts left!\n")

        if word_list == dash_list:
            print("You won! Good job!\n")
            print("The word was:", word,"\n")
            break

        if attempts == 1:
            print("Nice try, but you lost.\n")
            print("The word was:", word,"\n")
            break

def gallow(attempts):
    if attempts == 8:
        print("""\n------------
|          |
|           
|        
|        
|          
|_____________\n        
""")
    elif attempts == 7:
        print("""\n------------
|          |
|          o 
|        
|        
|          
|_____________\n        
""")
    elif  attempts == 6:
        print("""\n------------
|          |
|          o 
|        - O -
|         
|          
|_____________\n        
""")
    elif  attempts == 5:
        print("""\n------------
|          |
|          o 
|       /- O - 
|       
|         
|_____________\n        
""")
    elif  attempts == 4:
        print("""\n------------
|          |
|          o 
|       /- O -\ 
|          
|          
|_____________\n        
""")
    elif  attempts == 3:
        print("""\n------------
|          |
|          o 
|       /- O -\ 
|          | 
|           
|_____________        
""")
    elif  attempts == 2:
        print("""\n------------
|          |
|          o 
|       /- O -\ 
|          | 
|         /   
|_____________\n        
""")
    elif  attempts == 1:
        print("""\n------------
|          |
|          o 
|       /- O -\ 
|          | 
|         / \  
|_____________\n        
""")

solver(word, word_list)

while True:
    ask = input("Do you want to play again (Y/N): ")
    
    if ask == "Y" or ask == "y":
        
        print("""\n------------
|          |
|           
|        
|        
|          
|_____________\n        
""")

        allWords = ["hello", "actually", "friends", "student", "teacher", "school", "animal", 
        "bird", "classes", "toast", "airport", "beyond", "infinity", "enormous", 
        "family", "beautiful", "alarm", "water", "calculator", "pencil"]

        randomWordNumber = random.randint(0,19)
        word = allWords[randomWordNumber]
        word_list = list(word)

        solver(word, word_list)

    else:
        print("\nThanks for playing hangman!\n")
        break