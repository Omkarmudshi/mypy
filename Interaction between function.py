#three ball game

from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input('Enter yr guess between 0 to 2 ')
        print(f"ur choise is {guess}")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("currect")
        print(mylist)
    else:
        print("wrong guess")
        print(mylist)


game=['x','0','x']
mixedup_list=shuffle_list(game)
guess = player_guess()

print(check_guess(mixedup_list,guess))

    


