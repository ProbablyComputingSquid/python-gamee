from colorama import init, Fore, Back, Style
from keyboard import is_pressed
from time import sleep
import random
import os as yupOS
init()
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
  for i in range(num):
    print("")

#le clear screen function
def clear():
    # for windows 
    if yupOS.name == 'nt': 
      # Clears screen (Windows)
      _ = yupOS.system('cls') 
    else: 
      # Clears screen (Linux or mac)
      _ = yupOS.system('clear') 
