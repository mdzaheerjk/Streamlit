import streamlit as st
from io import StringIO

st.set_page_config(
    page_title='Streamlit demo app',
    page_icon='🚀',
    layout='centered'
)
st.title("Ultimate Data Science")

st.subheader("Level 1")
st.write("This is batch number 2 of ultimate data science bootcamp")

tab1,tab2,tab3=st.tabs(['Home','Dashboard','settings'])


with tab1:
    st.write("Welcome to Home Tab!")

    col1,col2,col3=st.columns(3)

    with col1:
        st.write("Left Section (Home)!")
        st.button("Click Left Section Button ",type='primary')

    with col2:
        st.write("Center Section (Home)!")
        st.button("Click Center Section Button",type='secondary')
    with col3:
        st.write("Right Section (Home)!")
        st.button("Click Left Section Button ",type='tertiary')
with tab2:
    st.write("Welcome to Dashbord Tab!")
with tab3:
    st.write("Welcome to Settings Tab!")

st.divider()

st.subheader('level 2')

with st.container(height=200,border=True):
    for i in range(101):
        st.write(f"Hello {i}")

st.divider()

st.subheader("Level 3 -Widgets")

if st.button("Say Hello"):
    st.write("Hello There")

st.link_button("Streamlit Widget Page Redirect",url='https://docs.streamlit.io/develop/api-reference/widgets')

a=0
print(a)
name=st.text_input('Enter Name')
a+=1
print(a)
print(name)
st.write(f"hello {name}")

count=0
if st.button("Click her to add one to the count"):
    count+=1
    st.write(f"hello there the current count value is {count}")

u_name=st.text_input("user name")
p_u_name=st.text_input("Passoword ",type='password')
bio=st.text_area("Tell us about Yourself",height=200)

st.subheader("Level 4 - widgets")


import datetime
today=datetime.date.today()
picked_data=st.date_input("Pick a Date",today)
st.write(picked_data)

st.divider()

upload_file=st.file_uploader("Upload a csv ",type=['csv','txt'])
if upload_file is not None:
    stringio=StringIO(upload_file.getvalue().decode('utf-8'))
    string_data=stringio.read()

    st.write(f"{type(upload_file)}")
    st.write(f"{type(string_data)}")

    st.write('File contents :')
    st.code(string_data,language='text')

st.warning("File Loading Warning!")
st.error("Error!")
st.info("Here is a helpfull tip!")

st.divider()

if 'count' not in st.session_state:
    st.session_state.count=0
if st.button("Increment"):
    st.session_state.count+=1
st.write(st.session_state.count)
st.divider()

st.title('Main Title')
st.header("Section Header")
st.subheader("sub-section")

st.markdown("we have **bold** in this statement")
st.markdown("<h1 style='color: blue;'> Custom Html</h1>",unsafe_allow_html=True)
st.divider()

st.subheader('Level 5-Extra ')

import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.write("Streamlit DataFrame Visulation")
st.dataframe(df)

st.write("Streamlit DataFrame Barchart")
st.bar_chart(df)

st.image(r"C:/Users/zahee/Downloads/vk.jpg",caption='My Image ',width=400)
st.divider()

import time
bar=st.progress(0)
for percent in range(100):
    time.sleep(0.1)
    bar.progress(percent+1)
st.divider()

text_to_save='1,2,3,4,5'
st.download_button(
    label='Downlaod text file',
    data=text_to_save,
    file_name='dummy_csv.txt',
    mime='text/plain'
    )