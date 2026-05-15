import streamlit as st

# Setup the tabs
tab1, tab2, tab3, tab4 = st.tabs(["Mission", "Hobbies", "Contact","Acheivments"])

with tab1:
    st.title(":blue[Our Mission] :smile:")
    
    # Using a 30/70 split for the image and text
    col1, col2 = st.columns([0.3, 0.7])
    
    with col1:
        # Note: 'Me.png' must be in the same folder as this script
        st.image("Stage_2/Me.png")
                         
    with col2:
        st.subheader(
            "Hi, I am Aryaman Chakraborti. My parents find it hard to manage "
            "and track their expenses. So, I created a website to help them "
            "track and manage their expenses. You can use this to also help "
            "you manage and track your expenses. I hope you all love it!!"
        )

with tab2:
    st.header("Hobbies:",divider="green")
    st.subheader("1)Drawing")
    st.subheader("2)Watching tv")
    st.subheader("3)Playing Video games")
with tab3:
    st.header("Get in Touch")
    st.subheader("Email:ajjep@gmail.com")
    # This turns the text into a clickable link
    st.subheader("Website:gmail.com")
with tab4:
    st.header("Acheivments:trophy::")
    st.subheader("1)I am a black belt in Taekwondo ")
    st.subheader("2)I got gold in ACSl")
    st.subheader("3)I finaled in Debate")
    st.subheader("3)I finaled in speech")

   
