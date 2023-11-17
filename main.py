from tkinter import *
import random
import threading
import pip
import time
import datetime
from tkinter import colorchooser
import pygame

def bg_music():
    pygame.init()
    pygame.mixer.music.load('price-of-freedom-33106.mp3')
    pygame.mixer.music.play(loops=1000)

music = threading.Thread(target=bg_music)
music.start()

def countdown(value):
    global money

    def countdown_time(value):
        global money
        global money
        global seconds_money

        seconds_money += value

        label_seconds.config(text='money per second: ' + str(seconds_money))

        while True:
            time.sleep(1)
            money += value
            label_money.config(text='money: ' + str(money))

    x = threading.Thread(target=countdown_time, args=(value,))
    x.start()


def countdown1(value):
    global money

    def countdown_time(value):
        global money
        global money
        global seconds_money
        seconds_money += value

        label_seconds.config(text='money per second: ' + str(seconds_money))

        label_seconds.config(text='current stage of money per second: ' + str(value))

        while True:
            time.sleep(1)
            money += value
            label_money.config(text='money: ' + str(money))

    x = threading.Thread(target=countdown_time, args=(value,))
    x.start()


def countdown2(value):
    global money

    def countdown_time(value):
        global money
        global money
        global seconds_money
        seconds_money += value

        label_seconds.config(text='money per second: ' + str(seconds_money))

        label_seconds.config(text='current stage of money per second: ' + str(value))

        while True:
            time.sleep(1)
            money += value
            label_money.config(text='money: ' + str(money))

    x = threading.Thread(target=countdown_time, args=(value,))
    x.start()


def countdown3(value):
    global money

    def countdown_time(value):
        global money
        global seconds_money
        seconds_money += value

        label_seconds.config(text='money per second: ' + str(seconds_money))

        while True:
            time.sleep(1)
            money += value
            label_money.config(text='money: ' + str(money))

    x = threading.Thread(target=countdown_time, args=(value,))
    x.start()


def countdown4(value):
    global money

    def countdown_time(value):
        global money
        global seconds_money
        seconds_money += value

        label_seconds.config(text='money per second: ' + str(seconds_money))

        while True:
            time.sleep(1)
            money += value
            label_money.config(text='money: ' + str(money))

    x = threading.Thread(target=countdown_time, args=(value,))
    x.start()


##########################################################################

def mainclick(value):
    global money
    global click_power
    money += value
    label_money.config(text='money: ' + str(money))

def click_1(value):
    global money
    global click_power

    def check_if_true():
        if money >= 25:
            return True


        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money = money - 25
        click_power += value
        label_money.config(text='money: ' + str(money))
        labelclick.config(text='click power: ' + str(click_power))


def click_2(value):
    global money
    global click_power

    def check_if_true():
        if money >= 300:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 300
        click_power += value
        label_money.config(text='money: ' + str(money))
        labelclick.config(text='click power: ' + str(click_power))


def click_3(value):
    global money
    global click_power

    def check_if_true():
        if money >= 500:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 500
        countdown(value)


def click_4(value):
    global money
    global click_power

    def check_if_true():
        if money >= 4000:
            return True


        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 4000
        countdown(value)


def click_5(value):
    global money
    global click_power

    def check_if_true():
        if money >= 20000:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 20000
        countdown(value)


def click_6(value):
    global money
    global click_power

    def check_if_true():
        if money >= 200000:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money = money - 200000
        click_power += value
        label_money.config(text='money: ' + str(money))
        labelclick.config(text='click power: ' + str(click_power))


def click_7(value):
    global money
    global click_power

    def check_if_true():
        if money >= 300000:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 300000
        countdown(value)


def click_8(value):
    global money
    global click_power

    def check_if_true():
        if money >= 300000:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 500000
        countdown(value)


def click_9(value):
    global money
    global click_power

    def check_if_true():
        if money >= 1000000:
            return True

        else:
            return False

    check_if_true()
    if check_if_true() is True:
        money -= 1000000
        countdown(value)


def restart():
    global money
    global click_power
    global seconds_money
    global button_help
    money = 0
    click_power = 1
    seconds_money = 0
    label_money.config(text='money: ' + str(money))
    label_seconds.config(text='current stage of money per second: ' + str(seconds_money))
    labelclick.config(text='click power: ' + str(click_power))
    button_help.place(x=600, y=200)


def change_color():
    color = colorchooser.askcolor()
    window.config(bg=color[1])


def need_help():
    global label_need_help

    def closeneedhelp():
        label_need_help.place_forget()
        buttonhaha.place_forget()

    label_need_help = Label(window,
                            text='Hello user,\nthis game is really easy.\nMillionaire offers many upgrades\nin order so it is easier to earn money!\nThe goal of this game\nis to become a millionaire as quickly\nas possible.\nYou can play this game with friends\nwho have also downloaded the game\nand you can do a competition.\nAre you ready?\nLETS ROCK IT!!! '
                            , font=('comic sans', 15))
    label_need_help.place(y=500, x=200)
    buttonhaha = Button(window, text='CLOSE', command=closeneedhelp, bg='lime')
    buttonhaha.place(x=550, y=500)


def close_upgrades():
    pass





###########################################################################


window = Tk()

money = 0





click_power = 1

seconds_money = 0

window.geometry('800x800')

icon = PhotoImage(file='money.png')
window.iconphoto(True, icon)
window.title('millionaire')

label_money = Label(window, text='money: ' + str(money), font=('consolas', 20, 'bold'))
label_money.place(x=200, y=0)

labelclick = Label(window, text='click_power power: ' + str(click_power), font=('consolas', 20, 'bold'))
labelclick.place(x=200, y=50)

label_seconds = Label(window, text='current stage of money per second: ' + str(seconds_money),
                      font=('consolas', 20, 'bold'))
label_seconds.place(x=210, y=100)


def show_all():
    def show():
        def close_upgrades():
            buttonhaha1.place_forget()
            buttonmain.place_forget()
            button1.place_forget()
            button2.place_forget()
            button3.place_forget()
            button4.place_forget()
            button5.place_forget()
            button6.place_forget()
            button7.place_forget()
            button8.place_forget()
            show_upgrades.place(x=0, y=50)

        buttonhaha1 = Button(window, text='CLOSE', command=close_upgrades, bg='lime')
        buttonhaha1.place(x=0, y=590)

        show_upgrades.place_forget()
        buttonmain = Button(window, text='increase click_power power by 5\n25$', command=lambda: click_1(5),
                            font=('MV Boli', 10))
        buttonmain.place(x=0, y=40)

        button1 = Button(window, text='increase click_power power by 30\n300$', command=lambda: click_2(30),
                         font=('MV Boli', 10))
        button1.place(x=0, y=100)

        button2 = Button(window, text='increase money per second by 5\n500$', command=lambda: click_3(5),
                         font=('MV Boli', 10))
        button2.place(x=0, y=160)

        button3 = Button(window, text='increase money per second by 50\n4 000$', command=lambda: click_4(50),
                         font=('MV Boli', 10))
        button3.place(x=0, y=220)

        button4 = Button(window, text='increase money per second by 200\n200 00$', command=lambda: click_5(200),
                         font=('MV Boli', 10))
        button4.place(x=0, y=280)

        button5 = Button(window, text='increase click_power power by 2000\n200 000$', command=lambda: click_6(2000),
                         font=('MV Boli', 10))
        button5.place(x=0, y=340)

        button6 = Button(window, text='increase money per second by 5000\n300 000$', command=lambda: click_7(3000),
                         font=('MV Boli', 10))
        button6.place(x=0, y=400)

        button7 = Button(window, text='increase money per second by 10k \n500 000$', command=lambda: click_8(10000),
                         font=('MV Boli', 10))
        button7.place(x=0, y=460)

        button8 = Button(window, text='increase money per second by 100k \n1 000 000$', command=lambda: click_9(100000),
                         font=('MV Boli', 10))
        button8.place(x=0, y=520)

    show_upgrades = Button(window, text='SHOP', command=show, height=10, width=10, bg='cyan', font=('comic sans', 20))
    show_upgrades.place(x=0, y=50)


show_all()

restart_button = Button(window, text='RESTART', command=restart, font=('consolas', 20, 'italic'))
restart_button.place(x=600, y=0)


def seeleaderboard():
    window.geometry('2000x800')


def upd():
    listl.append(money)
    listl.sort()
    listl.reverse()
    labelleader1.config(text='1# ' + str(listl[0]))
    if len(listl) >= 2:
        labelleader2.config(text='2# ' + str(listl[1]))
    if len(listl) >= 3:
        labelleader3.config(text='3# ' + str(listl[2]))
    if len(listl) >= 4:
        labelleader4.config(text='4# ' + str(listl[3]))
    if len(listl) >= 5:
        labelleader5.config(text='5# ' + str(listl[4]))


listl = []

seeleaderboard1 = Button(window, text='SEE \nLEADERBOARD', command=seeleaderboard, font=('consolas', 10, 'italic'))
seeleaderboard1.place(x=600, y=60)

labelleader = Label(window, text='LEADERBOARD:', font=('consolas', 20, 'italic'))
labelleader.place(x=1000, y=100)

labelleader1 = Label(window, text='1# ', font=('consolas', 20, 'italic'))
labelleader1.place(x=1000, y=150)

labelleader2 = Label(window, text='2# ', font=('consolas', 20, 'italic'))
labelleader2.place(x=1000, y=200)

labelleader3 = Label(window, text='3# ', font=('consolas', 20, 'italic'))
labelleader3.place(x=1000, y=250)

labelleader4 = Label(window, text='4# ', font=('consolas', 20, 'italic'))
labelleader4.place(x=1000, y=300)

labelleader5 = Label(window, text='5# ', font=('consolas', 20, 'italic'))
labelleader5.place(x=1000, y=350)

uptadebutton = Button(window, text='UPDATE', command=upd, font=('consolas', 20,), bg='yellow', fg='red', borderwidth=20)
uptadebutton.place(x=1200, y=0)

window.resizable(False, False)

color_button = Button(window, text='change background color', command=change_color, bg='light pink')
color_button.place(x=450, y=10)

image6 = PhotoImage(file='dollar (2).png')
need_help = Button(window, text='need help?', command=need_help)
need_help.place(x=400, y=500)

mainclickbutton = Button(window, image=image6, command=lambda: mainclick(click_power), borderwidth=0)
mainclickbutton.place(x=300, y=200)

window.mainloop()

###########################################################################


###########################################################################