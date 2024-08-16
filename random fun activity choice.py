from tkinter import *
import random

#make window
window = Tk()
window.title("Activity Picker")
window.iconbitmap("icon.ico")
window.geometry("300x300")

#list options
things_I_Enjoy = ["Draw","watch youtube videos","watch cartoons","Watch anime","read manga","read webtoons","read fanfiction","meditate","play games"]
pC_games = ["genshin","the great ace attorney","cities skyline","friday night funkin","my hero one’s justice","my hero one’s justice 2","street fighter x tekken","ace attorney trilogy"]
mobile_Games = ["cookie run","obey me","enstars","disney tw","lovlive school idol project","arcana twilight","love live All stars","project sekai"]
all_games = ["genshin","the great ace attorney","cities skyline","friday night funkin","my hero one’s justice","my hero one’s justice 2","street fighter x tekken","ace attorney trilogy","cookie run","obey me","enstars","disney tw","lovlive school idol project","arcana twilight","love live All stars","project sekai"]
break_Activities = ["watch [genshin] cutscenes","Learn to play chess","Watch anime", "watch a movie","write a letter to my future self","radio taisho","walk","cookie run stretch"]

#functions
def hobby_picker():
    x = random.choice(things_I_Enjoy)
    return x
def pc_picker():
    x = random.choice(pC_games)
    return x
def mobile_picker():
    x = random.choice(mobile_Games)
    return x
def allGames_picker():
    x = random.choice(all_games)
    return x
def break_picker():
    x = random.choice(break_Activities)
    return x
def home():
        result_label.pack_forget()
        ret_but.pack_forget()
        game_Random.pack_forget()
        game_Mobile.pack_forget()
        game_PC.pack_forget()
        game_label.pack_forget()
        hobby.pack()
        break_But.pack()

#hobby window
#answer, retry button, go back to main
def hobby_page():
    break_But.pack_forget()
    hobby.pack_forget()
    result = hobby_picker()
    if(result == "play games"):
        game_label.pack()
        game_PC.pack()
        game_Mobile.pack()
        game_Random.pack()
    else:
        result_label.config(text = result)
        result_label.pack()
    ret_but.pack()
   
        

#if play game pick: pc, mobile, random, retry
#game choice
def game_type_PC():
    break_But.pack_forget()
    hobby.pack_forget()
    result = pc_picker()
    result_label.config(text = result)
    result_label.pack()
    ret_but.pack()

def game_type_Mobile():
    break_But.pack_forget()
    hobby.pack_forget()
    result = mobile_picker()
    result_label.config(text = result)
    result_label.pack()
    ret_but.pack()


def game_type_Random():
    break_But.pack_forget()
    hobby.pack_forget()
    result = allGames_picker()
    result_label.config(text = result)
    result_label.pack()
    ret_but.pack()

#break window
#answer, retry, go back to main
def break_page():
    break_But.pack_forget()
    hobby.pack_forget()
    result = break_picker()
    result_label.config(text = result)
    result_label.pack()
    ret_but.pack()

#main window
#2 buttons hobby or break
hobby = Button(window, text = "Hobby", command= hobby_page)
hobby.pack()
break_But = Button(window, text = "Break", command = break_page)
break_But.pack()
ret_but = Button(window, text = "Main \n Menu", command=home)
result_label = Label(window, text = "Default")
game_label = Label(window, text= "Pick A Game Type!!!")
game_PC = Button(window, text = "PC",command = game_type_PC)
game_Mobile = Button(window, text = "Mobile", command = game_type_Mobile)
game_Random = Button(window, text = "Random", command = game_type_Random)

#display window
window.mainloop()