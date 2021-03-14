#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#    ______              _      _          
#   |  ____|            (_)    | |        
#   | |__ ___  ___   ___ _  ___| |_ _   _ 
#   |  __/ __|/ _ \ / __| |/ _ \ __| | | |
#   | |  \__ \ (_) | (__| |  __/ |_| |_| |
#   |_|  |___/\___/ \___|_|\___|\__|\__, |
#                                    __/ |
#                                   |___/
#
#

# imports lib
import sys
import argparse
import os
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
import ConfigParser
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep


# Конфиг
rootDir = path = os.path.abspath(os.path.dirname(__file__))
installDir = rootDir + '/tools/'
logDir = rootDir + '/logs/'
proxyes = ['172.106.11.102', 
           '152.179.12.86',
           '114.34.234.201', 
           '45.33.59.15', 
           '209.45.53.53' ]
port = '3128'
method = 'https'
proxy = random.choice(proxyes)
red   = '\033[91m'
blue  = '\033[34m'
green = '\033[92m'
fsocietyPrompt = red + "fsociety ~# " + blue 
continuePrompt = "\nClick [Return] to continue"
fsocietyLogo = blue + '''
        d88888b .d8888.  .d88b.   .o88b. d888888b d88888b d888888b db    db
        88'     88'  YP .8P  Y8. d8P  Y8   `88'   88         88    `8b  d8'
        88ooo   `8bo.   88    88 8P         88    88ooooo    88     `8bd8'
        88        `Y8b. 88    88 8b         88    88         88       88
        88      db   8D `8b  d8' Y8b  d8   .88.   88.        88       88
        YP      `8888Y'  `Y88P'   `Y88P' Y888888P Y88888P    YP       YP
        '''
# Точка входа
class fsociety:
    def __init__(self):
        os.system('clear')
        print(fsocietyLogo + '\033[91m' +'''
        }---------------------{+} Coded By Ermak {+}----------------------{
        }--------------{+} GitHub.com/Ermak4ok/fsociety {+}---------------{
    ''' + green +'''
        {1}--Information Gathering 
        {2}--Wireless Attacks
        {3}--Password Attacks
        {4}--Exploitation Tools
        {5}--Sniffing & Spoofing
        {6}--Web Hacking
        {7}--Private Web Hacking
        {8}--Post Exploitation
        {0}--INSTALL & UPDATE
        {11}-CONTRIBUTORS
        {99}-EXIT\n
     ''')
        choice = raw_input(fsocietyPrompt)
        os.system('clear')
        if choice == "1":
            informationGatheringMenu()
        elif choice == "99":
            sys.exit()
        elif choice == "\r" or choice == "\n" or choice == "" or choice == " ":
            self.__init__()
        else:
            try:
                print(os.system(choice))
            except:
                pass
        raw_input("Completed, click return to go back")
        self.__init__()

# Сбор информации по хосту
class informationGatheringMenu:
    menuLogo = '''
    88 88b 88 888888 dP"Yb
    88 88Yb88 88__  dP   Yb
    88 88 Y88 88""  Yb   dP
    88 88  Y8 88     YbodP
    '''

    def __init__(self):
        os.system('clear')
        print(self.menuLogo)
        print("   {1}--Whois")
        print("   {2}--Host To IP - All web-site on ip")
        print("   {3}--Nmap - Network Mapper")
        print("   {4}--CMSmap - Search CMS site")
        print("   {5}--Shell and Directory Finder")
        print("   {99}-Back To Main Menu \n")
        choiceinfo = raw_input(fsocietyPrompt)
        os.system('clear')
        if choiceinfo == "1":
            whois()
        elif choiceinfo == "2":
            hosttoip() 
        elif choiceinfo == "99":
            fsociety()
        else:
            self.__init__()
        raw_input("Completed, click return to go back")
        self.__init__()

# Получение информации о хосте: Номер, Почта, Улица, Город и т.д
class whois:
    whoisLogo = '''
    Yb        dP 88  88  dP"Yb  88 .dP"Y8        
     Yb  db  dP  88__88 dP   Yb 88 `Ybo."         
      YbdPYbdP   888888 Yb   dp 88    Y8b     
       YP  YP    88  88  YbodP  88  bodP'  
    '''

    def __init__(self):
        if not self.installed():
            self.install()
        os.system('clear')
        print(self.whoisLogo)
        address = raw_input("Enter Target IP/Subnet/Range/Host: ")
        self.menu(address)
    def installed(self):
        return (os.path.isfile("/usr/bin/whois") or os.path.isfile("/usr/local/bin/whois"))

    def install(self):
        os.system('apt-get install whois')

    def menu(self, address):
        os.system('clear')
        print(self.whoisLogo)
        print("   Whois scan for: %s\n" % address)
        print("   {1}--Full Scan \n")
        print("   {99}--Return to information gathering menu \n")
        response = raw_input("whois ~# ")
        os.system('clear')
        try:
            if response == "1":
                os.system("whois %s" % (address))
                response = raw_input(continuePrompt)
            elif response == "99":
                fsociety()
                pass
            else:
                self.menu(address)
        except KeyboardInterrupt:
            self.menu(address)















if __name__ == "__main__":
    try:
        fsociety()
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.25)