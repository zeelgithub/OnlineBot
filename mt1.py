import selenium
from selenium import webdriver
import time
import timetable as tt
import datetime
from datetime import date

#driver = webdriver.Chrome()
#driver.get('https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid')
#driver = webdriver.Chrome()
#driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')
driver = webdriver.Chrome(executable_path="C:\\Users\\baps\\AppData\\Local\\Temp\\Rar$EXa8620.29737\\chromedriver.exe")
driver.get("http://teams.microsoft.com")
time.sleep(5)

print("LOGING PROCESSING.......")

def login():
    print("ENTERING THE EMAIL ID......")
    driver.find_element_by_id("i0116").send_keys('19IT003@edu.charusat.org')
    time.sleep(2)

    print("Clicking next button........")
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(2)

    print("ENTERING THE PASSWOARD......")

    driver.find_element_by_id("i0118").send_keys('zeel1234@')
    time.sleep(2)

    print("Clicking sing in button.......")

    driver.find_element_by_id("idSIButton9").click()
    time.sleep(2)

    driver.find_element_by_id("KmsiCheckboxField").click()
    time.sleep(2)

    driver.find_element_by_id("idSIButton9").click()
    time.sleep(2)
    print("LOGIN IS SUCCESSFULL")




# THIS IS MAIN AREA

login()
time.sleep(10)
if date.today().weekday() == 0:
    print("PRASOON BOT is checking MONDAY Timetable")
    tt.Monday()

if date.today().weekday() == 1:
    print("PRASOON BOT is checking TUESDAY Timetable")
    tt.Tuesday()

if date.today().weekday() == 2:
    print("PRASOON BOT is checking WEDNESDAY Timetable")
    tt.Weadnesday()

if date.today().weekday() == 3:
    print("PRASOON BOT is checking THRUSDAY Timetable")
    tt.Thursday()

if date.today().weekday() == 4:
    print("PRASOON BOT is checking FRIDAY Timetable")
    tt.Friday()

if date.today().weekday() == 5:
    print("PRASOON BOT is checking SATURDAY Timetable")
    tt.Saturday()

