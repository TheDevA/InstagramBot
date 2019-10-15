# source code for InstgramBot By TheDevA
# github: https://github.com/TheDevA/InstgramBot.git
from selenium import webdriver
from time import sleep
import datetime
from random import randint
from sys import exit
print("""

 _           _                                             _           _
(_)         | |                                           | |         | |
 _ _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___    ______  | |__   ___ | |_
| | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |______| | '_ \ / _ \| __|
| | | | \__ \ || (_| | (_| | | | (_| | | | | | |          | |_) | (_) | |_
|_|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|          |_.__/ \___/ \__|
                       __/ |
                      |___/
                      By:TheDevA
                    github: https://github.com/TheDevA/InstgramBot.git

PS:It's better if you use a new instagram account for the bot
""")
print("""
--What type of browsers you use
-Google chrome
1-use google chrome version 76.x
2-use google chrome version 77.x
3-use google chrome version 78.x
99-exit
ps: more browsers is coming soon
""")
try:
    chrome76 = "driver/chromedriver76.exe"
    chrome77 = "driver/chromedriver77.exe"
    chrome78 = "driver/chromedriver78.exe"
    f = "Errors.txt"
    webd = ""
    goOrNot = False
    while goOrNot == False:
        choose = input(">>>")
        if choose == "1":
            print("useing chrome v76.x")
            webd = chrome76
            goOrNot = True
        elif choose == "2":
            print("useing chrome v77.x")
            webd = chrome77
            goOrNot = True
        elif choose == "3":
            print("useing chrome v78.x")
            webd = chrome78
            goOrNot = True
        elif choose == "99":
            exit()
            goOrNot = True
        else:
            print("ERROR:Use One Of The Top Choices")
    inputusernam = input("Put your instagram username >>> ")
    inputpassword = input("Put your instagram password >>> ")

    driver = webdriver.Chrome(webd)
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(5)
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    conne = driver.find_element_by_class_name("L3NKy")
    password.clear()
    username.clear()
    username.send_keys(inputusernam)
    password.send_keys(inputpassword)
    conne.click()
    sleep(5)
    driver.get("https://www.instagram.com/explore/")
    sleep(5)
    el = driver.find_elements_by_class_name("_9AhH0")
    el[0].click()
    while True:
        skp = randint(1, 5)
        sleepTime = randint(5, 10)
        floawOrNot = randint(0, 1)
        likeOrNot = randint(0, 1)
        try:
            sleep(sleepTime)
            hart = driver.find_element_by_class_name("fr66n")
            floow = driver.find_element_by_class_name("oW_lN")
            btn = driver.find_element_by_class_name(
                "coreSpriteRightPaginationArrow")
            if likeOrNot == 1:
                hart.click()
            elif floawOrNot == 1:
                floow.click()
            else:
                pass
            for n in range(skp):
                sleep(sleepTime)
                btn.click()

        except Exception as e:
            time = datetime.datetime.now()
            file = open(f, "a")
            file.write(f"{str(time)}>>>>{str(e)}" + "\n")
            print(f"""
            ==========================
            {e}
            ==========================
            """)
            file.close()
            exit()
except Exception as ee:
    if str(ee) == "list index out of range":
        print("""
        ===============================
        There is problem in the account
        ===============================
        """)
        exit()
    else:
        pass
    time = datetime.datetime.now()
    file = open(f, "a")
    file.write(f"{str(time)}(-o)>>>>{str(ee)}" + "\n")
    print(f"""
        ==========================
        {ee}
        ==========================
        """)
    file.close()
    exit()
