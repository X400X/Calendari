import re
import time

date = []
selected_event = []


def load_dates():
    with open("date.txt") as file:
        for row in file:
            sdata = row.strip().split("|")
            d = (sdata[0], sdata[1], sdata[2], sdata[3], int(sdata[4]))
            date.append(d)


def save_dates():
    with open("date.txt", "w") as t:
        for ii in range(len(date)):
            t.write(
                date[ii][0] + "|" + date[ii][1] + "|" + date[ii][2] + "|" + date[ii][3] + "|" + str(date[ii][4]) + "\n")


def check_time(s: str):
    a = False
    reg = "^([01][0-9]|2[0-3]):([0-5][0-9])$"
    if ":" not in s:
        if len(s) == 4:
            s1 = s[0] + s[1] + ":" + s[2] + s[3]
            if re.compile(reg).search(s1) is not None:
                a = True
            else:
                print("The time entered is incorrect. The time format must be XX:XX or XXXX")
        else:
            print("The time entered is incorrect. The time format must be XX:XX or XXXX")
    else:
        if len(s) == 5:
            s1 = s
            if re.compile(reg).search(s1) is not None:
                a = True
            else:
                print("The time entered is incorrect. The time format must be XX:XX or XXXX")
        else:
            print("The time entered is incorrect. The time format must be XX:XX or XXXX")
    return a


def check_date(s: str):
    a = False
    s1 = ""
    if "." not in s:
        if len(s) == 8:
            s1 = s[0] + s[1] + "." + s[2] + s[3] + "." + s[4] + s[5] + s[6] + s[7]
        else:
            print("The date was entered incorrectly. The date format should be: DDMMYYYY")
    else:
        if len(s) == 10:
            s1 = s
        else:
            print("The date was entered incorrectly. The date format should be: DD.MM.YYYY")
    try:
        if s1 != "":
            time.strptime(s1, "%d.%m.%Y")
            a = True
    except ValueError:
        print("The date was entered incorrectly. The date format should be: DDMMYYYY or DD.MM.YYYY")
    return a


def get_date(s: str):
    s1 = ""
    if "." not in s:
        if len(s) == 8:
            s1 = s[0] + s[1] + "." + s[2] + s[3] + "." + s[4] + s[5] + s[6] + s[7]
    else:
        if len(s) == 10:
            s1 = s
    return s1


def get_time(s: str):
    s1 = ""
    if ":" not in s:
        if len(s) == 4:
            s1 = s[0] + s[1] + ":" + s[2] + s[3]
    else:
        if len(s) == 5:
            s1 = s
    return s1


def check_imp(i: int):
    a = False
    if 0 < i < 6:
        a = True
    else:
        print("The importance entered is incorrect. The importance should be from 1 to 5")
    return a


def search_date(s: str):
    a = True
    for i in range(len(date)):
        if date[i][0] == s:
            print(date[i][0] + " " + date[i][1] + " " + date[i][2] + " " + date[i][3] + " " + str(date[i][4]))
            a = False
    if a:
        print("Not found.")


def search_eve(s: str):
    a = True
    for i in range(len(date)):
        if date[i][2] == s:
            print(date[i][0] + " " + date[i][1] + " " + date[i][2] + " " + date[i][3] + " " + str(date[i][4]))
            a = False
    if a:
        print("Not found.")


def search_imp(x: int):
    a = True
    for i in range(len(date)):
        if date[i][4] == x:
            print(date[i][0] + " " + date[i][1] + " " + date[i][2] + " " + date[i][3] + " " + str(date[i][4]))
            a = False
    if a:
        print("Not found.")


load_dates()

while True:
    s = int(input(f"Choose:\n1 - Add new event\n2 - Show all events\n3 - Search\n0 - Exit\nOption: "))
    if not isinstance(s, int):
        print("The Choose entered is incorrect. The Choose should be from 0 to 5")
    if not -1 < s < 5:
        print("The Choose entered is incorrect. The Choose should be from 0 to 5")
    if s == 0:
        save_dates()
        break
    if s == 1:
        dat = input("Date: ")
        dat1 = get_date(dat)
        if check_date(dat):
            tim = input("Time: ")
            tim1 = get_time(tim)
            if check_time(tim):
                event = input("Event: ")
                descr = input("Description: ")
                imp = int(input("Importance: "))
                if check_imp(imp):
                    dd = (dat1, tim1, event, descr, imp)
                    date.append(dd)
    if s == 2:
        for i in range(len(date)):
            print(date[i][0] + " " + date[i][1] + " " + date[i][2] + " " + date[i][3] + " " + str(date[i][4]))
    if s == 3:
        how = int(input(f"Choose:\n1 - Date\n2 - Event\n3 - Importance\nOption: "))
        if not isinstance(how, int):
            print("The Choose entered is incorrect. The Choose should be from 1 to 3")
        if not 0 < how < 4:
            print("The Choose entered is incorrect. The Choose should be from 1 to 3")
        if how == 1:
            date_t = input("Date: ")
            date_t1 = get_date(date_t)
            if check_date(date_t):
                search_date(date_t1)
        if how == 2:
            eve_t = input("Event: ")
            search_eve(eve_t)
        if how == 3:
            imp_t = input("Importance: ")
            if check_imp(int(imp_t)):
                search_imp(int(imp_t))
