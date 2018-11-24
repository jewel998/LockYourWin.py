# LockYourWin.py
A python GUI virus to temporarily lockup your Windows PC at every startup, unless the desired password is entered.

## About the Application:
The application blocks all the keystrokes when the app is run and runs at a full screen mode such that it's not possible to switch apps.
It even kills the Task Manager application when it is run, during it's execution through the handling of multiple threads.
This application has to be run as a superuser, i.e. **Administrator**. And whenever the program is run, it stores itself in the startup such that it executes when the computer boots up.
P.S.- The default password is 1234567890.

## The libraries used are:
1. tkinter
2. getpass
3. os
4. threading
5. pythoncom
6. pyHook
7. subprocess
8. time

## Additional libraries to be installed are:
+ tkinter
+ pyHook
+ pythoncom

## Bugs in the program
To access the files, a live USB can be created such that it can be manually removed from the Startup of the administrator with sufficient privileges.

#### Thanks for visiting my repo.
#### Support me with your queries at:
Facebook: <a href="http://www.facebook.com/jewel.barman">Jewel Barman</a>
Quora: <a href="https://www.quora.com/profile/Jewel-Barman-3">Jewel Barman</a>
