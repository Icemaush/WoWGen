from tkinter import *
from PIL import ImageTk, Image
import random
import os

window = Tk()
window.title("WoWGen")
window.geometry("200x225")

frame = Frame(window)
result_frame = Frame(window)
go_btn_frame = Frame(window)

frame.pack()
result_frame.pack()
go_btn_frame.pack()

wowfaction = StringVar()
wowrace = StringVar()
wowclass = StringVar()
wowspec = StringVar()
wowspec_display = StringVar()
theme = IntVar()

factions = ["Alliance", "Horde"]
alliance_dict = {"Dwarf": ["Hunter", "Paladin", "Priest", "Rogue", "Warrior"],
                 "Gnome": ["Mage", "Rogue", "Warlock", "Warrior"],
                 "Human": ["Mage", "Paladin", "Priest", "Rogue", "Warlock", "Warrior"],
                 "Night Elf": ["Druid", "Hunter", "Priest", "Rogue", "Warrior"]}
horde_dict = {"Orc": ["Hunter", "Rogue", "Shaman", "Warlock", "Warrior"],
              "Tauren": ["Druid", "Hunter", "Shaman", "Warrior"],
              "Troll": ["Hunter", "Mage", "Priest", "Rogue", "Shaman", "Warrior"],
              "Undead": ["Mage", "Priest", "Rogue", "Warlock", "Warrior"]}
spec_dict = {"Druid": ["Balance", "Feral", "Restoration1"],
             "Hunter": ["Beastmastery", "Marksmanship", "Survival"],
             "Mage": ["Arcane", "Fire", "Frost"],
             "Paladin": ["Holy1", "Protection1", "Retribution"],
             "Priest": ["Discipline", "Holy", "Shadow"],
             "Rogue": ["Assassination", "Combat", "Subtlety"],
             "Shaman": ["Elemental", "Enhancement", "Restoration"],
             "Warlock": ["Affliction", "Demonology", "Destruction"],
             "Warrior": ["Arms", "Fury", "Protection"]}


def btn_go(event=None):
    wowfaction.set(random.choice(factions))
    if wowfaction.get() == "Alliance":
        wowrace.set(random.choice(list(alliance_dict)))
        wowclass.set(random.choice(alliance_dict[wowrace.get()]))
        wowspec.set(random.choice(spec_dict.get(wowclass.get())))
        wowspec_display.set(wowspec.get().strip("1"))
    else:
        wowrace.set(random.choice(list(horde_dict)))
        wowclass.set(random.choice(horde_dict[wowrace.get()]))
        wowspec.set(random.choice(spec_dict.get(wowclass.get())))
        wowspec_display.set(wowspec.get().strip("1"))

    path = str(os.path.dirname(sys.argv[0]) + "/Images/" + wowclass.get().lower() + ".png")
    classimg = ImageTk.PhotoImage(Image.open(path))
    classimglabel.configure(image=classimg)
    classimglabel.image = classimg

    path2 = str(os.path.dirname(sys.argv[0]) + "/Images/" + wowspec.get().lower() + ".png")
    specimg = ImageTk.PhotoImage(Image.open(path2))
    specimglabel.configure(image=specimg)
    specimglabel.image = specimg

    window.update_idletasks()


def change_theme():
    if theme.get() == 0:
        window.configure(bg="SystemButtonFace")
        for widget in window.winfo_children():
            widget.configure(bg="SystemButtonFace")
        for widget in frame.winfo_children():
            widget.configure(bg="SystemButtonFace", fg="black")
        for widget in result_frame.winfo_children():
            widget.configure(bg="SystemButtonFace", fg="black")
        for widget in go_btn_frame.winfo_children():
            widget.configure(bg="SystemButtonFace", fg="black")
    if theme.get() == 1:
        window.configure(bg="black")
        for widget in window.winfo_children():
            widget.configure(bg="black")
        for widget in frame.winfo_children():
            widget.configure(bg="black", fg="white")
        for widget in result_frame.winfo_children():
            widget.configure(bg="black", fg="white")
        for widget in go_btn_frame.winfo_children():
            widget.configure(bg="black", fg="white")


factionlabel1 = Label(frame, text="Faction: ")
factionlabel1.grid(row=0, column=0)
factionlabel2 = Label(frame, textvariable=wowfaction)
factionlabel2.grid(row=0, column=1)
racelabel1 = Label(frame, text="Race: ")
racelabel1.grid(row=1, column=0)
racelabel2 = Label(frame, textvariable=wowrace)
racelabel2.grid(row=1, column=1)
classlabel1 = Label(frame, text="Class: ")
classlabel1.grid(row=2, column=0)
classlabel2 = Label(frame, textvariable=wowclass)
classlabel2.grid(row=2, column=1)
speclabel1 = Label(frame, text="Spec: ")
speclabel1.grid(row=3, column=0)
speclabel2 = Label(frame, textvariable=wowspec_display)
speclabel2.grid(row=3, column=1)
classimglabel = Label(result_frame)
classimglabel.grid(row=4, column=0, pady=5)
specimglabel = Label(result_frame)
specimglabel.grid(row=4, column=1, pady=5)
gobtn = Button(go_btn_frame, width=8, text="GO", command=btn_go)
gobtn.pack(pady=5)
gobtn.bind("<Return>", btn_go)
themechk = Checkbutton(go_btn_frame, text="Change Theme", variable=theme, command=change_theme)
themechk.pack()

gobtn.focus_set()

window.mainloop()
