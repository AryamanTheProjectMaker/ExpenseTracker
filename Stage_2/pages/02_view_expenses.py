import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = r"data/expense.csv"

def execution():
    df=pd.read_csv(excel_file_path)
    total=df["Amount"].max()
    st.subheader(f'Gold Coins:{str(int(total)//200)}🪙 ')

    date_from=st.date_input("From Date :date:")
    date_to=st.date_input("to date")

    st.write("Amount")
    amount_min=st.slider("Minimum value",min_value=0,max_value=200000,value=0,step=10)
    amount_max=st.slider("Maximum value",min_value=0,max_value=200000,value=200000,step=10)
    category = st.multiselect("Categories", [
        "Housing", "Utilities", "Transportation", "Food", "Healthcare",
        "Insurance", "Debt Payments", "Entertainment", "Personal Care",
        "Education", "Savings", "Taxes", "Miscellaneous"
    ], placeholder="You can choose multiple option(s)")

    df["Date"]=pd.to_datetime(df["Date"])
    date_from,date_to=pd.to_datetime(date_from),pd.to_datetime(date_to)

    if len(category)==0:
        condition=((df["Date"]>=date_from) & (df["Date"]<=date_to) & (df["Amount"]>=amount_min) & (df["Amount"]<=amount_max) )
        df=df[condition]
    else:
        condition=((df["Date"]>=date_from) & (df["Date"]<=date_to) & (df["Amount"]>=amount_min) & (df["Amount"]<=amount_max) & (df["Category"].isin(category)))
        df=df[condition]


    st.title("Expenses 📑")
    st.dataframe(df.reset_index(drop=True))

    st.title("Amount")
    st.line_chart(df["Amount"])

    st.title("Categories📇")
    category_df=df.groupby("Category")["Amount"].sum()

    fig,ax=plt.subplots()
    ax.pie(category_df,labels=category_df.index,autopct="%.2f",shadow=True)
    fig.set_facecolor("none")
    st.pyplot(fig)

try:
    execution()
except Exception as e:
    st.title("Please add some expenses")
    st.write(e)

