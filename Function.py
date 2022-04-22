from cgitb import text
from ctypes.wintypes import INT
import sqlite3 as sql


def Text_Welcome():
    print()
    print("Welcome the AutoDB for Sqlite")
    print("1.Open DataBase 0.Out")

def Text_control():
    print()
    print("What do you want to do?")
    print("1.creat table 2.")







def CreatTable():
    c = cont.cursor()
    c.execute('''CREATE TABLE Test
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL);''')

    cont.commit()
    cont.close()
    print("DONE")






def OpenDB():
    # "x" in a 检查是否包含指定字符
    text = input("DatabaseName:")

    if ".db" in text:  
        # 设置为全局
        global cont 
        cont = sql.connect(text)
        print("Open successfully" + text)

    else :

        print("please add .db")
    return 


