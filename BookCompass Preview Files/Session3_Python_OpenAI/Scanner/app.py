import streamlit as st
from PIL import Image
st.title("Hello, Streamlit!")

scanned_file = st.file_uploader(label:="Upload a picture to scan", type=["jpg","csv","jpeg","pdf","text"])

if scanned_file is not None:
    data=scanned_file.read()
    print (data)
