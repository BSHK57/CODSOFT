import random
#Global variablea to store scores
user_score=0
computer_score=0
Tied=0
def RockPaperScissorsGame(user_choice):
    #generating random choice as computer choice
    computer_choice=random.choice(['Rock','Paper','Scissors'])
    #printing the Computer choice
    print(f"Computer choice  : {computer_choice}")
    #condition who won the game and return values
    #if match Tied Tie will be returned
    if user_choice == computer_choice:
        return 'Tie'
    #if match won by computer Computer will be returned
    elif user_choice == 'Rock'and computer_choice=='Paper':
        return 'Computer'
    elif user_choice == 'Scissors'and computer_choice=='Rock':
        return 'Computer'
    elif user_choice == 'Paper'and computer_choice=='Scissors':
        return 'Computer'
    #Other wise User will be returned
    else:
        return 'User'
def main():
    global user_score,computer_score,Tied
    #printing various choice to select
    print("\n1.Rock\n2.Paper\n3.Scissors\n")
    while True:
        #prompting user to get the choice from the user
        choice=int(input("Choose your Choice(1-3):"))
        #Prints User choice and the game will start
        if choice == 1:
            print("Your choice      : Rock")
            game=RockPaperScissorsGame('Rock')
            break
        elif choice == 2:
            print("Your choice      : Paper")
            game=RockPaperScissorsGame('Paper')
            break
        elif choice == 3 :
            print("Your choice      : Scissors")
            game=RockPaperScissorsGame('Scissors')
            break
        else:
            print("..Invalid Choice Try again..")
    #User won Score increased
    if game == 'User':
        print(f'..Congratulations!..\nYou win')
        user_score+=10
    #Computer won Score increased
    elif game == 'Computer':
        print(f"..Better Luck next time..\nYou lost")
        computer_score+=10
    #match Tied No Increase in score
    else:
        Tied+=1
        print(f"..Match Tied..")
if __name__=="__main__":
    print("Welcome to Rock-Paper-Scissors Game")
    while True:
        #Choices to exit or Continue
        print("\nTo Continue game Press 1")
        print("To Exit          Press 0")
        choice=int(input("Your Choice:"))
        if choice == 1:
            main()
        #Printing both the Scores
        elif choice == 0:
            print(f"\nUSER SCORE    :{user_score}")
            print(f"COMPUTER SCORE:{computer_score}")
            print(f"No of Matches Tied={Tied}")
            print("\n......Thank You......")
            break
        else :
            print("..Invalid Selection Try again..")
