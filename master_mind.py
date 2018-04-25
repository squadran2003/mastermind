import random


no_of_tries = 0

def guess():
    player_num = input("guess the number >> ")
    return player_num

print("You get 4 tries to guess a number between 1 and 10")
while no_of_tries < 4:
    player_num = guess()
    random_num = random.randint(1,10)
    if player_num == random_num:
        print("Yayy you guessed right, the number was {}".format(random_num))
        break
    elif no_of_tries==3:
        print("You lost haha, the number was {}".format(random_num))
    else:
        print("try again!")
    no_of_tries+=1
    
        
        
    
    
