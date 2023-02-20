import requests
import concurrent.futures
import time
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()

counter = 0
url = "https://api.mojang.com/users/profiles/minecraft/"

def check(name):
    global counter
    while True:
        #if name.len < 3 or name.len > 16:
         #   print(Fore.YELLOW + name + " is an invalid username.")
          #  with open("invalid.txt", "a") as f:
           #     f.write(name + "\n")
            #    counter += 1
             #   os.system(counter + " names checked.")
            #break
        r = requests.get(url + name)
        if r.status_code == 200:
            print(Fore.RED + name + " is a valid username.")
            with open("valid.txt", "a") as f:
                f.write(name + "\n")
                counter += 1
                os.system(counter + " names checked.")
            break
        elif r.status_code == 204:
            print(Fore.GREEN + name + " is not taken.")
            with open("not taken.txt", "a") as f:
                f.write(name + "\n")
                counter += 1
                os.system(counter + " names checked.")
            break
        elif r.status_code == 400:
            print(Fore.YELLOW + name + " is an invalid username.")
            with open("invalid.txt", "a") as f:
                f.write(name + "\n")
                counter += 1
                os.system(counter + " names checked.")
            break
        elif r.status_code == 429:
            time.sleep(5)
            continue
        else:
            print("An error occurred. Please try again. Code: " + str(r.status_code))
            break

while True:
    multiThread = input(Fore.RED + "Do you want to use multi-threading? (y/n): ")
    if multiThread == "y":
        multiThread = True
        while True:
            os.system("cls")
            threads = input(Fore.RED + "How many threads do you want to use? (1-100): ")
            if threads.isdigit() and int(threads) > 0 and int(threads) <= 100:
                threads = int(threads)
                break
            else:
                os.system("cls")
                print(Fore.RED + "Please enter a number between 1 and 100.")
        break
    elif multiThread == "n":
        multiThread = False
        threads = 1
        break
    else:
        os.system("cls")
        print(Fore.RED + "Please enter y or n.")
        

while True:
    try:
        os.system("cls")
        file = input(Fore.RED + "Enter the file name: ")
        with open(file, "r") as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            os.system("cls")
        break
    except FileNotFoundError:
        os.system("cls")
        print(Fore.RED + "File not found. Please enter a valid file name including the extension. (Example: names.txt)")

if __name__ == "__main__":
    if multiThread:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(check, lines)
    else:
        for line in lines:
            check(line)