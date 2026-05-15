import streamlit as st
import pandas as pd
import os
folder_path="data"
file_path="data/feedback.csv"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(file_path):
    expenses=pd.DataFrame(columns=["Name","Feedback","rating"])
    expenses.to_csv(file_path,index=False)
def clear():
    st.session_state.name=""
    st.session_state.feedback=""

def  insert(Name,Feedback,rating):
    dataframe=pd.read_csv(file_path)
    length=len(dataframe)
    if Name!="" and Feedback!="":
        dataframe.loc[length]=[Name,Feedback,rating]
        dataframe.to_csv(file_path,index=False)
        st.balloons()
    else:
        st.error("Please provide the requred feilds",icon="⚠️")

   
Name = st.text_input('Please enter your Name', key='name' )
Feedback = st.text_input('Please add your Feedback ', key='feedback' )
rating =  st.select_slider("Please provide a rating from 1-5", [1, 2, 3, 4, 5])
emoji_holder=st.empty()
if rating==1:
    emoji_holder.subheader("We will definetly improve 😢")
if rating==2:
    emoji_holder.subheader("We will add your feedback to become a much better website ")

if rating==3:
    emoji_holder.subheader("Glad you are content. We will try to find some more ways to improve 😐")

if rating==4:
    emoji_holder.subheader("Seems like you like it 🙂")
if rating==5:
    emoji_holder.subheader("Thanks for loving our website so much 😻")

coll1,coll2=st.columns([0.25,0.9])
with coll1:
    Add_Button=st.button("Submit 💸")
with coll2:
    Clear_Button=st.button("Clear ✂️",on_click=clear )

if Add_Button:
    insert(Name,Feedback,rating)
    st.success("Thank you for your valuble feedback")
st.subheader("past feedback")
dataframe=pd.read_csv(file_path)
st.dataframe(dataframe)

