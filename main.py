# encoding=utf8
#!/usr/bin/python3
import argparse
import os
import smtplib
import sys

from getpass import *
from typing import Type
from src.Colors import *
from time import *


def banner():
    banner = f'''
    {Color.ALERT}
    
______                          _  _  _                        _     
| ___ \  {Color.BLUE}@theycallmecharlie{Color.ALERT}    (_)| || |                      | |    
| |_/ /_   _  _ __ ___    __ _  _ | || |__    ___   _ __ ___  | |__  
|  __/| | | || '_ ` _ \  / _` || || || '_ \  / _ \ | '_ ` _ \ | '_ \ 
| |   | |_| || | | | | || (_| || || || |_) || (_) || | | | | || |_) |
\_|    \__, ||_| |_| |_| \__,_||_||_||_.__/  \___/ |_| |_| |_||_.__/ 
        __/ |                                                        
       |___/  {Color.DANGER} 4 EDUCATIONAL PURPOSE {Color.WHITE}                                                        
    {Color.WHITE}'''
    return banner


# def main():
#     parser = argparse.ArgumentParser(description="Pymail bombing")
#     parser.add_argument('-n', '--name', help='A name to sent mail as', action='store_true')
#     parser.add_argument('-m', '--mail', help='Attacker mail', action='store_true')
#     parser.add_argument('-p', '--passw', help='Password app set', action='store_true')
#     parser.add_argument('-l', '--list', help='Mailist', action='store_true')
#     parser.add_argument('-t', '--target', help='Target mail', action='store_true')
#     parser.add_argument('-q', '--quantity', help='Quantity of emails that\'ll be sent to the target', action='store_true')
#     parser.add_argument('-body', '--body', help='Message', action='store_true')
#     parser.add_argument('-smtp', '--smtpserver', action='store_true', default = 'smtp.gmail.com')
#     parser.add_argument('-port', '--smtport', action='store_true', default = 587)
#     args = parser.parse_args()
#     menu()
def main():
    try:
        name, mail, passw = input("Anon name: "), input("Attacker mail: "), input("Attacker passw: ")
        #removed # emails
        target, subject, body = input("Target mail: "), input("Subject :"), input("Message: ")
        print(f'{Color.HEADER}Leave the info bellow in blank to use [smtp.gmail.com:587]{Color.WHITE}')
        smtpserver = input(f"[{Color.ALERT}Default{Color.WHITE}] smtp.gmail.com - SMTP SERVER: ")
        smtpport = input(f"[{Color.ALERT}Default{Color.WHITE}] 587 - SMTP PORT: ")
        if smtpserver == '':smtpserver = 'smtp.gmail.com'
        if smtpport == '':smtpport = '587'
        extension = target[-4:]
        body = f"Subject:{subject}\n\n {body} \n\n {name}"
        if extension == '.txt':
            with open(target, 'r', encoding='UTF-8') as f:
                list = f.readlines()
                maillist = []
                for i in list:
                    maillist.append(i.strip())
                f.close()
            print(f"{Color.ALERT}Connecting..", end='\r')
            connection = smtplib.SMTP(smtpserver, smtpport)
            connection.ehlo(), connection.starttls(), connection.login(mail, passw)
            sleep(0.75), print(f"[{Color.GREEN}Yep! Connected{Color.WHITE}]", end='\r')
            for target in maillist:
                print(f'[{Color.GREEN}+{Color.WHITE}] sending mail to {Color.BLUE}{i}{Color.WHITE}', end='\r')
                sleep(1), connection.sendmail(mail, target, body)
                print(f'[{Color.GREEN}+{Color.WHITE}] mailto {Color.BLUE}{i}{Color.WHITE} has been sent. ', end='\n')
                sleep(0.75), sys.stdout.flush()
        else:
            print(f"{Color.ALERT}Connecting..", end='\r')
            connection = smtplib.SMTP(smtpserver, smtpport)
            connection.ehlo(), connection.starttls(), connection.login(mail, passw)
            sleep(0.75), print(f"[{Color.GREEN}Yep! Connected{Color.WHITE}]", end='\r')
            print(f"{Color.ALERT}Sending email{Color.WHITE}", end='\r')
            connection.sendmail(mail, target, body)
            print(f'[{Color.GREEN}+{Color.WHITE}] mailto {target} has been sent. ', end='\r')
            sleep(1), sys.stdout.flush()
        print('', end='\n'), connection.quit
        print(f'[{Color.HEADER}Finished{Color.WHITE}]')
        sys.exit(1)
    except smtplib.SMTPAuthenticationError: print(f'[{Color.DANGER}Error{Color.WHITE}] Woops! Email or password entered is incorrect'), sys.exit(1)
    except smtplib.SMTPConnectError: print(f'{Color.DANGER}Error{Color.WHITE} Could not connect to {mail}'), sys.exit(1)
    except FileNotFoundError: print(f'[{Color.DANGER}Error{Color.WHITE}] Can not find the specified file'), sys.exit(1)
    except KeyboardInterrupt: print(f'{Color.WHITE} pymailbomb has been stopped'), sys.exit(1)
    except Exception as error: print(f'[{Color.DANGER}Error{Color.WHITE}] {error}'), sys.exit(1)


if __name__ == '__main__':
    print(banner())
    main()
