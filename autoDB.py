from cgitb import text
import imp
import sqlite3 as sql
import Function

Function.Text_Welcome()


text = input()
if text == "1":
    Function.OpenDB()

# 还是输出"1"
print(text)
print("\a")




Function.Text_control()

text = input()
if text == "1":
    Function.CreatTable()


# TODO 插入数据









str = input("OVER")
print (str)