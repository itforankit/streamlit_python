import streamlit as st
import pandas as pd
st.title('My first app')

name=st.text_input('Enter your name:')

age=st.slider('Enter your age:',0,100,0)    #
#sex=st.radio('Male','Female')

options =["Python","Java","C++"]    
choice = st.selectbox('Which is your favourite language?',options)
st.write('You selected:',choice)

st.write('Hello',name,'your age is:',age)
if name:
    st.write('Hello',name)  

uploaded_file=st.file_uploader('Choose a CSV file',type='csv')
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.write(data)
