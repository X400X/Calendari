import calendar
from datetime import datetime
import os
import re
import time

date = []
date_del = []
selected_event = []


def load_dates():
    if os.path.exists("date.txt"):
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


def search_all(x: str, xt: int):
    if xt == 4:
        sss = int(x)
    else:
        sss = x
    a = True
    for i in range(len(date)):
        if date[i][xt] == sss:
            print(date[i][0] + " " + date[i][1] + " " + date[i][2] + " " + date[i][3] + " " + str(date[i][4]))
            a = False
            d = (date[i][0], date[i][1], date[i][2], date[i][3], int(date[i][4]))
            date_del.append(d)
    if a:
        print("Not found.")


def delete_date():
    b = 0
    while b < len(date_del):
        a = 0
        while a < len(date):
            if date_del[b] == date[a]:
                del date[a]
            else:
                a += 1
        b = b + 1
    date_del.clear()


def go_to_start():
    print("Go to start.")


def show_events_for_delete():
    b = 0
    while b < len(date_del):
        print(date_del[b][0] + " " + date_del[b][1] + " " + date_del[b][2] + " " + date_del[b][3] + " " + str(
            date_del[b][4]))
        h = int(input(f"Do you want to delete this event?\n1 - Yes\n2 - Continue\nOption: "))
        try:
            if not 0 < h < 3:
                print("The Choose entered is incorrect. The Choose should be 1 or 2")
            if h == 1:
                d = (date_del[b][0], date_del[b][1], date_del[b][2], date_del[b][3], int(date_del[b][4]))
                date_del.clear()
                date_del.append(d)
                delete_date()
                print("Selected event are deleted.")
            if h == 2:
                print("Next")
        except ValueError:
            print("The Choose entered is incorrect. The Choose should be 1 or 2")
        b += 1


def delete_step_by_step(y: int):
    s0 = f"\nDo you want to delete all events for this date?\n1 - Yes\n2 - Select event\n0 - To Start\nOption: "
    s2 = f"\nDo you want to delete all of this same names events?\n1 - Yes\n2 - Select event\n0 - To Start\nOption: "
    s4 = f"\nDo you want to delete all events for this importance?\n1 - Yes\n2 - Select event\n0 - To Start\nOption: "
    w = ""
    if y == 0:
        w = s0
    elif y == 2:
        w = s2
    else:
        w = s4
    try:
        h = int(input(w))
        if not -1 < how < 3:
            print("The Choose entered is incorrect. The Choose should be from 0 to 2")
        if h == 1:
            delete_date()
            print("All selected events are deleted.")
        if h == 2:
            show_events_for_delete()
        if h == 0:
            go_to_start()
            date_del.clear()
    except ValueError:
        print("The Choose entered is incorrect. The Choose should be from 0 to 2")


def set_str1(ss: str):
    t = ss.split(".")
    s1 = "______________________________________\n"
    s1 = s1 + "|      Month: " + t[1] + "     Year: " + t[2] + "      |\n"
    s1 = s1 + "|____________________________________|\n"
    s1 = s1 + "|  Ma   Ti   Ke   To   Pe   La   Su  |\n"
    s1 = s1 + "| "
    a = 1
    b = 1
    num_days = calendar.monthrange(int(t[2]), int(t[1]))[1]
    d = "01." + t[1] + "." + t[2]
    date2 = datetime.strptime(d, "%d.%m.%Y")
    i = date2.weekday()
    s = "    "
    while i > 0:
        s1 = s1 + s + " "
        i -= 1
        a += 1

    while a < 8:
        s1 = s1 + return_number_of_day(b, t[1], t[2]) + " "
        b += 1
        a += 1
    s1 = s1 + "|\n| "

    while a < 15:
        s1 = s1 + return_number_of_day(b, t[1], t[2]) + " "
        b += 1
        a += 1
    s1 = s1 + "|\n| "

    while a < 22:
        s1 = s1 + return_number_of_day(b, t[1], t[2]) + " "
        b += 1
        a += 1
    s1 = s1 + "|\n| "

    while a < 29:
        s1 = s1 + return_number_of_day(b, t[1], t[2]) + " "
        b += 1
        a += 1
    s1 = s1 + "|\n"

    if num_days != b:
        s1 = s1 + "| "
        while a < 36:
            if b <= num_days:
                s1 = s1 + return_number_of_day(b, t[1], t[2]) + " "
            else:
                s1 = s1 + s + " "
            b += 1
            a += 1
        s1 = s1 + "|\n"

    if b <= num_days:
        s1 = s1 + "| "
        while a < 43:
            if b <= num_days:
                s1 = s1 + return_number_of_day(b, t[1], t[2]) + " "
            else:
                s1 = s1 + s + " "
            b += 1
            a += 1
        s1 = s1 + "|\n"

    s1 = s1 + "|____________________________________|"

    return s1


def one_equal(s: str):
    a = False
    for iii in range(len(date)):
        if s == date[iii][0]:
            a = True
    return a


def return_number_of_day(i: int, a: str, b: str):
    s3 = ""
    s = ""
    if i < 10:
        s = "0" + str(i)
    else:
        s = str(i)
    s3 = s + "." + a + "." + b
    if one_equal(s3):
        s = "|" + s + "|"
    else:
        s = " " + s + " "
    return s


load_dates()
try:
    while True:
        try:
            s = int(input(
                f"Choose:\n1 - Add new event\n2 - Show all events\n3 - Search and Delete\n0 - Exit\nOption: "))
            if not -1 < s < 4:
                print("The Choose entered is incorrect. The Choose should be from 0 to 3")
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
                            print("Successfully added!")
            if s == 2:
                try:
                    how = int(input(f"Choose:\n1 - Current month and year\n2 - Any date\n3 - All events in list\n0 - To Start\nOption: "))
                    if not -1 < how < 4:
                        print("The Choose entered is incorrect. The Choose should be from 0 to 3")
                    if how == 1:
                        date123 = datetime.today()
                        str1 = date123.strftime(".%m.")
                        str2 = date123.strftime("%y")
                        s = "01" + str1 + "20" + str2
                        date_t4 = get_date(s)
                        if check_date(s):
                            print(set_str1(date_t4))
                    if how == 2:
                        date_t = input("Date: ")
                        date_t3 = get_date(date_t)
                        if check_date(date_t3):
                            print(set_str1(date_t3))
                    if how == 3:
                        for i in range(len(date)):
                            print(date[i][0] + " " + date[i][1] + " " + date[i][2] + " " + date[i][3] + " " + str(date[i][4]))
                    if how == 0:
                        go_to_start()
                except ValueError:
                    print("The Choose entered is incorrect. The Choose should be from 0 to 3")
            if s == 3:
                try:
                    how = int(input(f"Choose:\n1 - Date\n2 - Event\n3 - Importance\n0 - To Start\nOption: "))
                    if not -1 < how < 4:
                        print("The Choose entered is incorrect. The Choose should be from 0 to 3")
                    if how == 1:
                        date_t = input("Date: ")
                        date_t1 = get_date(date_t)
                        if check_date(date_t):
                            search_all(date_t1, 0)
                            delete_step_by_step(0)
                    if how == 2:
                        eve_t = input("Event: ")
                        search_all(eve_t, 2)
                        delete_step_by_step(2)
                    if how == 3:
                        imp_t = input("Importance: ")
                        if check_imp(int(imp_t)):
                            search_all(imp_t, 4)
                            delete_step_by_step(4)
                    if how == 0:
                        go_to_start()
                        date_del.clear()
                except ValueError:
                    print("The Choose entered is incorrect. The Choose should be from 0 to 3")
        except ValueError:
            print("The Choose entered is incorrect. The Choose should be from 0 to 3")
except KeyboardInterrupt:
    print("Something wrong")
