import random
import time
import os
import sys
import colorama
from colorama import Fore 
from colorama import init

os.system("title PrntScLinkGen")

chars = "1234567890abcdefghijklmnoprstuvwxyz"
start_link = "https://prnt.sc/"
file = open ("links.txt", "w", encoding="utf-8")

time.sleep(2)

print(Fore.BLUE)

print("""
  _____            _    _____      _      _       _     _____            
 |  __ \          | |  / ____|    | |    (_)     | |   / ____|           
 | |__) | __ _ __ | |_| (___   ___| |     _ _ __ | | _| |  __  ___ _ __  
 |  ___/ '__| '_ \| __|\___ \ / __| |    | | '_ \| |/ / | |_ |/ _ \ '_ \ 
 | |   | |  | | | | |_ ____) | (__| |____| | | | |   <| |__| |  __/ | | |
 |_|   |_|  |_| |_|\__|_____/ \___|______|_|_| |_|_|\_\\_____|\___|_| |_|

""")

print("хотите ли вы сохранять ссылки в .txt [y/n]")

path_to_script = os.path.abspath(os.curdir)

answer = "n"
answer = input()

print("введите колиество ссылок для генерации")

amount = int(input())

try:
  os.system("cls")
except:
  os.system("clear")


for i in range(amount):
  a = random.choice(chars)
  b = random.choice(chars)
  c = random.choice(chars)
  d = random.choice(chars)
  e = random.choice(chars)
  f = random.choice(chars)

  ready_link = start_link+a+b+c+d+e+f
  print(Fore.GREEN)
  
  print(ready_link)

  if(answer == "y"):
    file.write(ready_link + '\n')

file.close()
print("\n ссылок сгенерировано: ", amount,"\n")

if(answer == "y"):
  print("все ссылки сохранены в файл ", path_to_script, "\links.txt")

#to preduce closing of console
input()
