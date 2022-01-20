##########################
# Made by ComputingSquid #
##########################
from colorama import init
from colorama import Fore, Back, Style
from time import sleep
import random
import os as yupOS

randomMoneyAmount = random.randint(100,500000)
# written text???
### credit to EmojiGame for initial writing and question functions
def write(txt, newline = True, speed = 0.05,color = 'WHITE'):
  for i in txt:
    sleep(speed)
    if color == 'WHITE':      
      print(Fore.WHITE + i, end = "", flush = True)
    elif color == 'RED':
      print(Fore.RED + i, end = "", flush = True)
    elif color == 'BLUE':
      print(Fore.BLUE + i, end = "", flush = True)
    elif color == 'GREEN':
      print(Fore.GREEN + i, end = "", flush = True)
    elif color == 'MAGENTA':
      print(Fore.MAGENTA + i, end = "", flush = True)
    elif color == 'YELLOW':
      print(Fore.YELLOW + i, end = "", flush = True)
    elif color == 'CYAN':
      print(Fore.CYAN + i, end = "", flush = True)
    else:
      print(Fore.WHITE + i, end = "", flush = True)
  if newline:
    print("")

# idk
def ask(txt):
  write(txt, False)
  ans = input(" ")
  return ans

# newline because why now
def newline(num):
  while num != 0:
    print("")
    num -= 1

#le clear screen function
def clear():  
    # for windows 
    if yupOS.name == 'nt': 
      # Clears screen (Windows)
      _ = yupOS.system('cls') 
    else: 
      # Clears screen (Linux or mac)
      _ = yupOS.system('clear') 

#variables
randomMoneyAmount = random.randint(100,500000)
money = 300000
finished = 0
homeless = False
init()
selfEsteem = 1
while finished == 0:
  clear()
  days_survived = 0
  print(Fore.RED + "_________________________________________")
  print("|                                       |")
  print("|          Text adventure game          |")
  print("|           By: ComputingSquid          |")
  print("|_______________________________________|")
  sleep(2)
  write('You have woken up, deciding to start a new life.\n',color='WHITE')
  sleep(1.5)
  write("A new year means a new life. \n", color='GREEN')
  sleep(1.5)
  write("So you have decided to be a better person.\n", color='WHITE')
  sleep(1.5)
  write("Different from the RUTHLESS CRIME LORD that you had used to be.\n")
  sleep(1.5)
  write("(In reality you were the proud owner of a daycare franchise.)\n")
  sleep(1.5)
  write("But let bygones be bygones.\n")
  sleep(1.5)
  write("Anyways...")
  sleep(1.5)
  write("Lets get around to the real stuff\n")
  clear()
  write("DAY 1 of your new life \n")
  sleep(1)
  write("So in order to start your new life, you need to make some money. \nYou already have $" + str(money) +
" in your bank account from your day care buisness.")
  write("So in order to make some money, what will you do?\n")
  write("[1]: Sell your day care franchise")
  write("[2]: Sell all your stocks")
  write("[3]: Stock trading")
  write("[4]: Crypto Mining")
  write("[5]: Go to McDonalds, get a burger, and do nothing else except binge-watch The Simpsons")
  choice = ask("Pick either 1,2,3,4 or 5:")
  tried = 'not yet'
  while tried == 'not yet':
    clear()
    if choice == '1':
      clear()
      write("You put up an ad on AdManiac.\n")
      write("'Day care franchise for sale! only 500 grand!'")
      write("1 hour later...")
      sleep(1)
      write("Someone replied to your ad!")
      sleep(1)
      write("The person said 'Ok why not'")
      sleep(1)
      write("So the person bought your daycare franchise.")
      sleep(1)
      write("+500 grand minus tax ($472500)")
      money += 472500
      sleep(1)
      write("-1 daycare franchise")
      daycarefranchises = 0
      sleep(1)
      write("+1 Self-Esteem")
      selfEsteem +=1
      sleep(1)
      write("+1 AdManiac Reputation Points")
      sleep(2)
      adManiacReputationPoints = 1
      days_survived += 1
      tried = 'yes'
    elif choice == '2':
      clear()
      stockValue = randomMoneyAmount
      write("But then you realized you only had " + str(stockValue) + " dollars worth in stocks ")
      sleep(1)
      write("So you sold your stocks for $" + str(stockValue) + ".")
      sleep(1)
      write("+" + str(stockValue) + " Dollars", color = 'RED')
      money += stockValue
      sleep(1)
      days_survived += 1
      tried = 'yes'
    elif choice == '3':
      write("Ok time for stock trading...")
      write("What do you want to invest in?")
      stockinvested = ask("[1]: Microsoft\n or:\n[2]:Amazon\n")
      if stockinvested == '1':
        clear()
        write("Ok...")
        write("Microsoft it is then.")
        write("You bought 5000 dollars worth of Microsoft Stocks...")
        write("You will recive 1000 dollars every 2 days")
      elif stockinvested == '2':
        clear()
        write("You decide to invest in AMAZON")
        write("You then see in the news....")
        sleep(1)
        write("AMAZON CANCELS FREE SHIPPING!!!!", color = 'RED')
        write("You die of shock because you would never imagine that amazon would ever, ever, EVER cancel free shipping.")
        write("+1000000 Amazon hate")
        sleep(1)
        sadness = 100000
        tried = 'yes'
      else:
        write("You didn't invest in anything...")
        days_survived += 1
        tried = 'yes'
      days_survived += 1
      tried = 'yes'
    elif choice == '4':
      clear()
      write("Hmm Crypto mining?")
      write("What crypto to mine....")
      crypto_mined = ask("[1]: Bitcoin, Time: 1 week, Expected gains: Good\n[2]: Ethereum, Time: 6 months, Expected gains: Good\n[3]: LiteCoin, Time: 10 minuted, Expected gains: Poor, but easy to mine\n ")
      clear()
      if crypto_mined == '1':
        write("Bitcoin?")
        write("Ok then.")
        write("You open up your laptop and open up XMrig.")
        sleep(10)
        write("1 week and 10 McBurgers later...")
        write("You got one bitcoin.")
        write("+1 Bitcoin")
        write("-1 bitcoin")
        write("+42968 dollars")
        money += 42968
        days_survived += 7
      elif crypto_mined == '2':
        write("Etherium...")
        write("Time to get mining then...")
        days_survived += 182
        sleep(10)
        write("182 days and 400 Starbucks coffees later...")
        write("You got 1 ethereum")
        write("Congrats")
        write("+1 Ethereum")
        write("-1 Ethereum")
        write("+3267 dollars")
        write("+400 Coffees")
        write("-400 Coffees")
        days_survived +=1
        tried = 'yes'
      elif crypto_mined == '3':
        write("1 hour and 6 LiteCoin later")
        write("You mined some LiteCoin")
        write("+6 LiteCoin\n")
        write("You sold your LiteCoin to JohnXina55")
        sleep(1)
        write("-6 LiteCoin")
        write("+850 Dollars")
        sleep(1)
        days_survived +=1
        money+= 850
      else:
        write("You went to freebitco.in")
        write("And gambled your money away.")
        write("You lost all your money and sold all your property and became homeless.")
        write("You then got hit by a car, and had no health insurance and couldn't afford health care and died of injuries.")
        sleep(2)
        write("- All of your money")
        write("- All of your belongings")
        sleep(1)
        money = 0
        homeless = True
        finished=0
        tried = 'yes'
        
      tried = 'yes'
    elif choice == '5':
      clear()
      write("You hop in your car and drive off to McDonalds.")
      sleep(1)
      write("Now the most important descision...")
      sleep(1)
      write("What burger to get?")
      sleep(2)
      burger = ask("[1]: A BaconBurger\n[2]: A delicious McBurger\n[3]: A Chicken McBurger\n[4] An ImposibleMcBurger\n")
      if burger == '1':
        clear()
        write("A delicious BaconBurger...")
        sleep(1)
        write("A good choice.")
        write("")
      elif burger == '2':
        clear()
        write("A delicious McBurger...")
        write("Quite generic though...")
        write("The guy says, 'You gonna pay or not?'")
        sleep(1)
        write("The McBurger costs 2 dollars")
        write("You hand over two dollars to the clerk")
        money -= 2
        burgers = 1
        write("You take the burger and drive back to your home to watch The Simpsons reruns")
        sleep(1)
        write("You plop down on the couch and turn on your TV and open Disney Minus")
        sleep(2)
        write("1 Hour later...", True, 0.08)
        write("And one ")
        write("ok")
        tried = "yes"
      elif burger == '3':
        clear()
        write("A delicious Chicken McBurger...")
        write("Well Chicken burgers???")
        write("What have we come to...")
        write("You order and pay.")
        sleep(1)
        write("When you get home and take a bite into your 'delicious' chicken McBurger")
        write("You die of food posisoning from the burger")
        sleep(1)
        write("That was dumb...")
        tried = 'yes'
      elif burger == '4':
        clear()
        write("What, are you a vegitarian...")
        write("I don't got anything against vegitarians though...")
        write("Impossible burgers are good though.")
        write("So you order an impossible burger")
        write("You hand over 6 dollars to the cashier")
        write("You take the burger and drive home looking forwards to a TV dinner.")
        write("You chomp down your burger in front of the TV.")
        write("That was good...")
        sleep(1)
        write("But you didn't earn any money though...")
        write("Too bad.")
        write("Stop getting off-track.")
        newline(3)
        selfEsteem -= 1
        write("Self Esteem - 1")
        write("Burgers +1")
        write("Burgers -1")
        burgers = 0
        days_survived += 1
        tried = "yes"
      else:
        write("The guy gives you a standard McBurger")
        money -= 2
        write("You go home and watch the simpsons.")
        write("You didn't earn any money.")
        write("Too bad for you")
    else:
      write("Invalid input...")
      write("Try again")
      write("Actually never mind because you had an invalid input, YOU DIEDDDDD")
      sleep(10)
      write("JK")
      write("Now you have to try again")
      write("So let this be a lesson to you")
      write("www.tinyurl.com/4r8vaa6p")
      tried = 'not yet'    
    
  finished = 1

clear()
write("You survived " + str(days_survived) + " days,")
write("And had " + str(money) + " Dollars")
if homeless:
  write("And... Died homeless")
  write("Seriously....")
  write("Acheived Ending: Died Homeless from a car crash.")
else:
  write("")
if days_survived <= 3:
  write(str(days_survived) + " day(s) wasn't that long...")
  write("could have done better")
elif days_survived > 3:
  write("Good job")
elif days_survived > 10:
  write("Nice... You did a great job. Worthy of appriciation..")
else:
  write("Good job, you survived pretty long...")
write("")