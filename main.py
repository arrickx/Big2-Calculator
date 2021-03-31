from os import system
from time import sleep

def bigD():
    # Let user input scores. Also provide samples for clarification
    while True:
      try:
        # if any number is decimal, notice the user and restart program
        score = [ int(x) for x in input("Please input the score for all players.(split by space) \ni.e., 1 2 3 4\n").split()]
      except ValueError:
        system('clear')
        print("Decimal not allowed. \nPlease try again. \n")
        sleep(3)
        system('clear')
      else:
        # if any number is negative, notice the user and restart program
        for i in score:
              if i < 0:
                system('clear')
                print("Negative number not alllowed. \nPlease try again. \n")
                sleep(3)
                system('clear')
                break
              else:
                  if any(score.count(element) > 1 for element in score) == True:
                    system('clear')
                    print("Two or more player got the same scores. \nPlease play one more rount then try again. \n")
                    sleep(5)
                    system('clear')
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
                    if price < 0:
                      system('clear')
                      print("Negative number not alllowed. \nPlease try again. \n")
                      sleep(3)
                      system('clear')
                      break
                    else:
                      print("\nTop player win $%s" %(first*price))
                      print("Second player win $%s" %(second*price))
                      print("Third player lose $%s" %(third*price))
                      print("Fourth player lose $%s\n" %(fourth*price) )

while True:
  bigD()