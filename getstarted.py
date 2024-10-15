import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

st.set_page_config(page_title="My first website", page_icon=":tada:", layout="wide")

# Load local Lottie file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding_local = load_lottiefile(r"C:\Users\acer\Downloads\Animation - 1728477839445.json")

# Load Lottie URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding_url = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

# Header section
with st.container():
    st.subheader("This is Marcial")
    st.title("Visionist Leader")
    st.write("I envision a good business establishment that brings generational wealth")
    st.write("Let's do this")

# Content section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """I am a student yet I am trying to learn how to do web design and web development.
            I use canva for my sample web designs, and do coding on visual studio code for its front ends. 
            If I think I'm good enough then I'll put my best outputs on my portfolio. I will use different platforms on where
            I will put my portfolio. I will then start finding clients and earn money."""
        )
    st.write("[Watch here >>>](https://youtube.com/c/CodingIsFun)")
    st.subheader("material goals")
    st.write("list for my 20s")

    with right_column:
        st_lottie(lottie_coding_url, height=200, key="coding")
