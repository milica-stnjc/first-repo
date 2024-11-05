import streamlit as st
import segno
import time

st.set_page_config(
    page_title="QR-CODE",
    page_icon="🧳")

st.image("images/main_banner.jpg")

st.title("QR Code Generator")

url = st.text_input("Enter the URL you want to encode:")

def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.save("images/qrcode_streamlit.png",
                scale=5)

if url:
    with st.spinner("Generate QR Code"):
        time.sleep(3)
    generate_qrcode(url)
    st.image("images/qrcode_streamlit.png")

st.markdown("Made by Milica Stanojic")