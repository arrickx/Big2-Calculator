from os import system, name
from time import sleep

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

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
                    # if any player has the same score, notice the user and restart program
                    if any(score.count(element) > 1 for element in score) == True:
                      reset(3,"Two or more player got the same scores. \nPlease play one more rount then try again. \n")
                      break
                    else:
                      # Find the min number
                      m = min(score)
                      # Deduct all the number by the min number
                      score = [x  - m for x in score]
                      # Sort the number into ascending  order
                      score.sort()
                      a,b,c,d = score
                      # Calculate the win/loss amounts for the players
                      first = sum(score)
                      second = d-b+c-b-b
                      third = c+c-d-b+c
                      fourth = d+d-b+d-c
                      # Find out the amount they play
                      price = float(input("\nHow much do you guys play?\ni.e., 0.25\n"))
                      # if any price is negative, notice the user and restart program
                      if price <= 0:
                        reset(3,"Negative number or zero not alllowed. \nPlease try again. \n")
                        break
                      else:
                        print("\nTop player win $%s" %(str(round(first*price, 2))))
                        print("Second player win $%s" %(str(round(second*price, 2))))
                        print("Third player lose $%s" %(str(round(third*price, 2))))
                        print("Fourth player lose $%s\n" %(str(round(fourth*price, 2))))
                        break
while True:
  bigD()