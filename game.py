import sys
import random
import time
from time import sleep
from colorama import init, Fore
init()

bold = '\033[01m'
end_bold = '\033[0m'

#Hidden                 
NEW_BOARD = [list('*'*4) for i in range(4)]
game_board = [list('*'*4) for i in range(4)]


#Game Key
COL =  ['1','2','3','4']
KEY = ['A','A','B','B','C','C','D','D','E','E','F','F','G','G','H','H']


def shuffle_board(key):
    """shuffles KEY list for fresh game board"""
    random.shuffle(KEY)
    shuffled_key = KEY[:4],KEY[4:8],KEY[8:12],KEY[12:16]
    return shuffled_key
game_key = shuffle_board(KEY)


def tprint(string):
    """typewriter printing"""
    for char in string:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    return string


def print_new_board(game_board):
    """print hidden board"""
    print ("   " + " ".join(COL)).center(60)
    cnt = 1
    for row in game_board:
        print (" " + str(cnt) + " " + " ".join(row)).center(60)
        cnt += 1
    print


def print_game_key():
    """print board key"""
    print ("   " + " ".join(COL)).center(60)
    cnt = 1
    for row in game_key:
        print (" " + str(cnt) + " " + " ".join(row)).center(60)
        cnt += 1
    print
    

#game play
def print_greeting():
    """Prints introductory greeting"""
    print
    print
    greeting = bold + Fore.CYAN + "WELCOME TO THE GAME OF MEMORY!" + Fore.RESET + end_bold
    tprint(greeting.center(80))
    print
    time.sleep(1)
    tprint("\nLet's test your memory with an old fashioned matching game.")
    print
    time.sleep(1)
print_greeting()


def get_name():
    """Gets player name"""
    player_name = raw_input("To begin, please enter your name: ")
    player_name = player_name.title()
    print
    tprint("Okay {}, let's get started.".format(player_name))
    return player_name
get_name()

def flip_card(x,y):
    #reassigns hidden card to value of card in game KEY, i.e. "flips" card
    game_board[x][y] = game_key[x][y]
    return game_board[x][y]
    
    
def update_game_board(game_board):
    """Prints board with revealed cards"""
    print " " + bold
    print ("   " + " ".join(COL)).center(60)
    cnt = 1
    for row in game_board:
        print (" " + str(cnt) + " " + " ".join(row)).center(60)
        cnt += 1
    print " " + end_bold
    return game_board
    
def reset_board(x,y):
    """clears game board after no match round"""
    game_board[x][y] = "*"
    return game_board
    
def get_first_choice():
    x,y = raw_input("Enter the coordinates of the first card (row, column): ").strip().split(',')
    
    #if the user enters letters...
    if x.isalpha() == True or y.isalpha() == True: 
        print "Oops! Please enter numbers for the coordinates in row,column format, e.g. '2,2'"
        return get_first_choice()
    
    else:
        x,y = int(x)-1,int(y)-1
        
        if x < 0 or y < 0:
            print "Woops! That's not on the game board. Try again."
            print
            return get_first_choice()
            
        elif (x > len(game_board)-1) or (y > len(game_board)-1):
            print "Woops! That's not on the game board. Try again."
            print
            return get_first_choice()
        
        elif game_board[x][y] != "*":
            print "You've already guessed that card. Try again."
            print
            return get_first_choice()
            
        else:
            flip_card(x,y)
    return x,y


def get_second_choice():
    a,b = raw_input("Enter the coordinates of the second card (row, column): ").strip().split(',')
    
    #if the user enters letters...
    if a.isalpha() == True or b.isalpha() == True: 
        print "Oops! Please enter numbers for the coordinates in row,column format, e.g. '2,2'"
        return get_first_choice()
    
    else:
        a,b = int(a)-1,int(b)-1
        
        if a < 0 or b < 0:
            print "Woops! That's not on the game board. Try again."
            return get_first_choice()
            
        elif (a > len(game_board)-1) or (b > len(game_board)-1):
            print "Woops! That's not on the game board. Try again."
            return get_first_choice()
        
        elif game_board[a][b] != "*":
            print "You've already guessed that card. Try again."
            return get_first_choice()
            
        else:
            flip_card(a,b)
    return a,b


def play_again():
    """after turns run out, asks player if they want to start a new game"""
    play_again = raw_input("Would you like to play again? YES/NO:").upper()
                
    if play_again == "YES":
        game_play()
                    
    elif play_again == "NO":
        print "Thanks for playing!"
    
    else:
        print "Please enter YES or NO"
        return play_again()
    
    return


def game_play():
    """full run of game"""
    shuffle_board(KEY)

    tprint("\nYou have 10 chances to find each of the four pairs of matching cards.")
    time.sleep(2)
    print
    print
    
    turn = 1
    while turn < 10:
        turn_count = bold + Fore.BLUE + "TURN {}:\n".format(turn) + Fore.RESET + end_bold
        tprint(turn_count)
            
        update_game_board(game_board)
        time.sleep(1)
        print
            
        x,y = get_first_choice() #user chooses first card
        print 
        update_game_board(game_board)
        print
                
        a,b = get_second_choice() #user chooses second card
        print
        update_game_board(game_board)
        print
            
        if game_board[x][y] == game_board[a][b]: #if a match
            print "Congratulations! You found a match!"
            print
            time.sleep(1)
                
            if any("*" in s for s in game_board):                                                                          
                pass

            else:
                print "Congratulations! You won in {} turns!".format(turn)
                play_again()
                break

        elif game_board[x][y] != game_board[a][b]:
            print "Woops. No match. Try again."
            print
            turn += 1
            reset_board(x,y)
            reset_board(a,b)
            time.sleep(1)
    
    else:
        print "Sorry! Game over!"
        play_again()

    return
    
game_play()
 
            
        #     else:
        #         print "Woops! That's outside of the board. Try again:"
        #         continue
        # else:
        #     print "Woops! Please use digits for the coordinates."
        #     continue

