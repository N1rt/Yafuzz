import requests
import sys 
import time

title =  """
_____              _____        _             _   _ _     _____ 
|  ___|   _ _______|___ / _ __  | |__  _   _  | \ | / |_ _|___  |
| |_ | | | |_  /_  / |_ \| '__| | '_ \| | | | |  \| | | '__| / / 
|  _|| |_| |/ / / / ___) | |    | |_) | |_| | | |\  | | |   / /  
|_|   \__,_/___/___|____/|_|    |_.__/ \__, | |_| \_|_|_|  /_|   
                                       |___/                   
"""

print(title,sep='')

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

    #testando se o site esta funcionando
    r_test = requests.get(Site)
    print(f'testando se a conexão com o site está funcionando...\n[SiteRequest]:{Site}\n[StatusCode]:{r_test.status_code}')
    time.sleep(5)
    print("iniciando fuzzer...")
    for line in wordlist_lines:
        r = requests.get(f"{Site}{line}")
        print(f"PATH:{Site}{line}\nStatus Code:{r.status_code}")
    print("The program has ended.")

