#num1=34
#num2=36
#total=num1+num2
#print(total)


import random

def choose_Animal():
    Animals =['Dog','cat','bird','fish','rabbit','mouse','horse','cow','pig','sheep','goat','chicken','duck','goose','deer','bear','elephant','tiger','lion','giraffe','monkey','gorilla','panda','koala','kangaroo','wolf','fox','squirrel','raccoon','otter','seal','dolphin','whale','shark','turtle','frog','lizard','snake','crocodile','hippo','rhino','zebra','camel','ostrich','penguin','eagle','owl','bat','bee','butterfly','ant','spider','snail','octopus','jellyfish']
    chosen_word=random.choice(Animals)
    Animals.remove(chosen_word)
    return chosen_word

def Answer(Animal,Guessed_alphabets):
    display=''
    for letter in Animal:
        if letter in Guessed_alphabets:
            display+= letter
        else:
            display='_'
    return display

def Hangman_Game():
    Animal=choose_Animal()
    Guessed_alphabets=[]
    attempts= 5

    print("Welcome to Hangman Game!")
    print("The word has {} letters".format(len(Animal)))

    while attempts>0:
        print('\nAttempts left:', attempts)
        print("Guessed Alphabets:",Guessed_alphabets)
        print(Answer(Animal,Guessed_alphabets))

        guess =input("Guess a letter:").lower()
        
        if guess in Guessed_alphabets:
            print("You've already done it.")
        elif guess in Animal:
            Guessed_alphabets.append(guess)
            print("Bravo!")
        else:
            attempts-= 1
            print("Wrong Guess!")
        if '_' not in Answer(Animal,Guessed_alphabets):
            print("\nCongratulation! You've guessed the Animal:",Animal)
            break
    if attempts == 0:
        print("\nOh! you've failed to guess animal. The Animal was:",Animal)
if __name__=='__main__':
         Hangman_Game()        