from os import system, name
from time import sleep

# define our clear function
def clear():
    # for windows use 'cls' else use 'clear'
    system('cls') if name == 'nt' else system('clear')

# define the reset function that can show up the message then restart this app
def reset(sec,text):
    clear()
    print(text)
    sleep(sec)
    clear()

# define the bigD function to calculate the amount
def bigD():
    # let user input scores. Also provide samples for clarification
    while True:
      try:
        # if any number is decimal, notice the user and restart program
        score = [ int(x) for x in input("Please input the score for all players.(split by space) \ni.e., 1 2 3 4\n").split()]
      except ValueError:
        reset(3,"Decimal not allowed. \nPlease try again. \n")
      else:
        # if the number of scores are not equal to 4. Notice user and restart the program
        if len(score) != 4:
          reset(3,"Please input 4 numbers in score. \nPlease try again. \n")
        else:
          # if any number is negative, notice the user and restart program
          for i in score:
                if i < 0:
                  reset(3,"Negative number not alllowed. \nPlease try again. \n")
                  break
                else:
                  # Find the min number
                  m = min(score)
                  # Deduct all the number by the min number
                  score = [x  - m for x in score]
                  # Sort the number into ascending  order
                  score.sort()
                  a,b,c,d = score
                  # Calculate the win/loss amounts for the players. Update the staus of second and third ranking player based on their score
                  first = sum(score)
                  second = -3*b+c+d
                  secondOutcome = "lose" if second<0 else "win"
                  second = -second if second<0 else second
                  third = -b+3*c-d
                  thirdOutcome = "win" if third<0 else "lose"
                  third = -third if third<0 else third
                  fourth = -b-c+3*d
                  # Find out the amount they play
                  price = float(input("\nHow much do you guys play?\ni.e., 0.25\n"))
                  # if any price is negative, notice the user and restart program
                  if price <= 0:
                    reset(3,"Negative number or zero not alllowed. \nPlease try again. \n")
                    break
                  else:
                    print("\nTop player win $%s" %(str(round(first*price, 2))))
                    print("Second player %s $%s" %(secondOutcome, str(round(second*price, 2))))
                    print("Third player %s $%s" %(thirdOutcome, str(round(third*price, 2))))
                    print("Fourth player lose $%s\n" %(str(round(fourth*price, 2))))
                    break
while True:
  bigD()