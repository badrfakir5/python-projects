import random
guess = int(input("guess a number: "))
number = random.randint(1,10)
count = 0

while guess != number :
    if guess < number :
        print("your guess is too low")
        guess = int(input("try again: "))
        count += 1
    elif guess > number :
        print("your guess is too high")
        guess = int(input("try again: "))
        count += 1
        
print(f"you are right you took {count + 1} guesses to guess the right number")
        
    
    

