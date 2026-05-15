import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

excel_file_path = r"data/expense.csv"
def generate_wordcloud(text):
    Wordcloud=WordCloud(width=400,height=400,background_color=None).generate(text)
    fig, ax = plt.subplots()
    ax.imshow(Wordcloud,interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

def execution():
    try:
        df=pd.read_csv(excel_file_path)

        if len(df) != 0:
            max_amt=df[df["Amount"] == df["Amount"].max()]
            st.subheader("You are spending the most here 😢 ")
            st.dataframe(max_amt.reset_index(drop=True))

            min_amt=df[df["Amount"] == df["Amount"].min()]
            st.subheader("You are spending the Least here 😻 ")
            st.dataframe(min_amt.reset_index(drop=True))

            most_trans_date=(
                df.groupby(by="Date").size().nlargest(1).index
            )

            st.subheader("You made the most numer of transactions on 📆 ")
            st.dataframe(most_trans_date)
            least_trans_date=(
                df.groupby(by="Date").size().nsmallest(1).index
            )

            st.subheader("You made the least numer of transactions on 📆 ")
            st.dataframe(least_trans_date)

            most_category=df["Category"].mode()
            st.subheader("The categories for which you are spending the most 📦")
            st.dataframe(most_category)
            
            least_category=df["Category"].value_counts().idxmin()
            st.subheader("The categories for which you are spending the least 😌")
            st.dataframe(df[df["Category"]==least_category]["Category"].reset_index(drop=True))
             
            description_data="".join(list(df["Description"].values))
            st.subheader("Description cloud🗨️")
            generate_wordcloud(description_data)
        else:
            st.header("Please add some expennses before analyzing it")
    except FileExistsError:
        st.header("Please add somme expenses before analyzing it")

execution()