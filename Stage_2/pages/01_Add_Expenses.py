import streamlit as st
import pandas as pd
import os
folder_path="data"
file_path="Stage_2/data/expense.csv"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(file_path):
    expenses=pd.DataFrame(columns=["Date","Category","Description","Currency Type","Importance","Amount"])
    expenses.to_csv(file_path,index=False)
def clear():
    st.session_state.desc=""
    st.session_state.am=0
def  insert(date,category,description,currency_type,Importance,amount):
    dataframe=pd.read_csv(file_path)
    length=len(dataframe)
    if description!="" and amount>0:
        dataframe.loc[length]=[date,category,description,currency_type,Importance,amount]
        dataframe.to_csv(file_path,index=False)
        st.balloons()
    else:
        st.error("Please provide a description and a valid amount above 0",icon="⚠️")

date = st.date_input('Date :date:')
category = st.selectbox("Category :card_index_dividers:",("Housing","Utilities","Transportation","Food","Healthcare","Insurance","Debt Payments","Entertainment","Personal Care","Education","Savings","Taxes","Miscellaneous") )
description = st.text_input('Description :flashlight:', key='desc' )
currency_type = st.selectbox("Currency type :heavy_dollar_sign: / :euro:",("Dollars","Euros"))
Importance = st.selectbox("Importance level :heavy_dollar_sign: / :euro:",("1","2","3","4","5","6","7","8","9","10",))
amount = st.number_input('Amount :money_mouth_face:', key='am',min_value=0,step=1,max_value=2000000)
coll1,coll2=st.columns([0.25,0.9])
with coll1:
    Add_Button=st.button("Add Expense 💸")
with coll2:
    Clear_Button=st.button("Clear ✂️",on_click=clear )

if Add_Button:
    insert(date,category,description,currency_type,Importance,amount)
