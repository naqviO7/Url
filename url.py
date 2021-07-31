# => URL Shortner

# => importing required modules
import random
import string
import os
import time
import sys
from os import system

# => setting window title 
system("title " + "Url Shortener")

# => function contains menu of program
def menu():
    time.sleep(3)
    
    print("="*25,"M E N U","="*25)
    print(" -> Press 1 to Shorten URL!")
    print(" -> Press 0 to Exit!")
    print("="*59,"\n")
    
    time.sleep(3) 
    
# => function to generate random shorted url
def shorted_urls():
    # => taking input from user
    long_url = input("Enter URl to Shorten: ")
    
    # => generating random url
    short_url = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
    
    # => concatinating it with wwww. and .com
    short_url = "www." + short_url + ".com"
    
    # => displaying short generated url
    print("Shortened URL: ",short_url)
    
    #creating and opening file in append mode
    f = open("URLs.txt", "a+")
    
    # => saving long urls in file
    f.write("Long Url: ")
    f.write(long_url)

    # => saving long urls in file
    f.write("\tShorted Urls: ")
    f.write(short_url)
    f.write("\n\n")
    
    time.sleep(1.5)
    print("Long and Short Url is Saved in",f.name)
    time.sleep(1.5)
    
    
# => self made main function    
# => from where code execution will start    
def main_function():
    # => clearing screen of previous output
    os.system('cls')
    
    # => displaying menu 
    menu()
    
    # => taking input from user
    # => for the action to perform
    key=int(input("Enter Key to Perform Option: "))
    
    if key==1:
        time.sleep(1.5)
        shorted_urls()
        print("="*22, "E X I T I N G", "="*22,"\n")
        sys.exit()
    
    elif key==0:
        print("="*22, "E X I T I N G", "="*22,"\n")
        sys.exit()
    
    else:
        print("-> Invalid Option!\n")
        print("="*22, "E X I T I N G", "="*22,"\n")
        sys.exit()
        
# => calling main function
main_function()

# => calling input function 
# => to let user see the output

input()
