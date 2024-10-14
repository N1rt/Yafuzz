#!/bin/python3

import requests
import sys 
import os

os.system("figlet Fuzz3r by N1r7")

if(len(sys.argv) < 3 and len(sys.argv) > 1):
    print("ParameterError:fuzzer takes 2 arguments")
    exit()
if(len(sys.argv) > 3):
    print("ParameterError:fuzzer takes only 2 arguments,not more")
    exit()
if(len(sys.argv) == 1):
    print("Fuzzer Usage: fuzzer.sh [SITE] [WORDLIST]")
if(len(sys.argv) == 3):
    Site = sys.argv[1];
    WordList = sys.argv[2];
    try:    
        with open(WordList,'r') as w:
            wordlist_lines = w.readlines();
            for line in range(len(wordlist_lines)):
                wordlist_lines[line] = wordlist_lines[line].replace("\n","")
    except:
        print("FileNotFounded:Error,WordList not founded,do you put the right path?")
    for line in wordlist_lines:
        r = requests.get(f"{Site}{line}")
        print(f"PATH:{Site}{line}\nStatus Code:{r.status_code}")
    print("The program has ended.")


