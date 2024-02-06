import os

print("Which task would you like to preform: \n"
             "1: dir \n"
             "2: cd\n"
             "3: mkdir\n"
             "4: echo\n"
             "5: type\n"
             "6: exit\n")

while True:
    task = input("PLease enter task: ")
    if task == "1":
        os.system("dir")  # List directory contents
    elif task == "2":
        os.system("cd")  # the equivalent as pwd and turns it to a string
    elif task == "3":
        os.system("mkdir TestDir")  # Makes directory called TestDir
    elif task == "4":
        os.system("echo Hello World")  # Prints message
    elif task == "5":
        os.system("type file.txt")  # Opens file.txt
    elif task == "6":
        os.system("exit")  # Exits the shell
        break
    else:
        print("invalid value")
