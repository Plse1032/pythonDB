import streamlit as st #wb 框架
import pandas as pd
import numpy as np
import sqlite3 as sql

cont = sql.connect("test.db")
c = cont.cursor()
cursor = c.execute("SELECT id, name from Test")

for row in cursor:
    st.title(row[0])
    st.title(row[1])

print ("数据操作成功")
cont.close()


name = st.text_input('Name')
if not name:
    st.warning('Please input a name.') 
    st.stop()
st.success('Thank you for inputting a name.')