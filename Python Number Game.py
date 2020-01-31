import random
a = random.randint(1,10)
userClaim = 3

def numberGame():
    ops = int(input("ENTER 1-10 NUMBER:"))
    if ops == a:
       print("YOU WON")
    elif ops < a:
       print("----ENTER HIGH NUMBER") 
    elif ops > a:
       print("----ENTER LOW NUMBER")
    else:
       print("ENTER NUMBER...")
    return ops


while True:
    if userClaim > 0:
      if numberGame() == a:
         break
      userClaim -= 1
      print("YOUR CLAİM",userClaim)
    else:
      print("GAME OVER")
      print("NUMBER=",a)
      break
       


