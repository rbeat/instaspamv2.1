# coding=utf-8
#!/usr/bin/env python3

""" 
Before changing the program and posting it somewhere, please
Please note that this program is under the GPLv3 license.
More information:
https://www.gnu.org/licenses/quick-guide-gplv3.html
"""

__author__ = "Hichigo TurkHackTeam"
__license__ = "GPLv3"
__version__ = "2.1.0"
__status__ = "WIP"



from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Logging in . . .")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Logging in w/o proxy . . .")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging in . . .")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging in w/o proxy . . .")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Users are being loaded . . .")
    USERS = LoadUsers("./kullanicilar.txt")
    PrintStatus("Proxies are being loaded . . .")
    PROXIES = LoadProxies("./proxyler.txt")
    print("")

    username = GetInput("Username of the account you want to report:")
    userid = GetInput("Account number you want to report:")
    useproxy = GetInput("Do you want to use a proxy? [y/n]:")
    if (useproxy == "y" || useproxy == "Y"):
        useproxy = True
    elif (useproxy == "n" || useproxy == "N"):
        useproxy = False
    else:
        PrintFatalError("Please just enter 'y' or 'n'!")
        exit(0)
    usemultithread = GetInput("Do you want to use multithreading? [y/n] (Don't use this feature if you have a lot of users or your computer is slow!):")
    
    if (usemultithread == "y" || usemultithread == "Y"):
        usemultithread = True
    elif (usemultithread == "n" || usemultithread == "N"):
        usemultithread = False
    else:
        PrintFatalError("Please just enter 'y' or 'n'!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Please select one of the above complaint reasons (ex: 1 for spam):")

    
    
    
    print("")
    PrintStatus("Starting!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
    

    
