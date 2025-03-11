import streamlit as st
from PIL import Image


NAME = "Online Game «Magic World»"
URL = "https://en.mworld.mobi/?channelId=48644"
START_GAME = "Start Playing!"


st.set_page_config(
    page_title=NAME,
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

top_image = Image.open('static/magmir.jpg')

st.sidebar.markdown(f'<center><b>{NAME}</b></center>', unsafe_allow_html=True)
st.sidebar.markdown('<center>A game of adventure in which you will gather heroes, each possessing unique skills'
                    '<center>', unsafe_allow_html=True)
st.sidebar.markdown(
    f'<center><a href="{URL}" target="_blank">{START_GAME}</a></center>',
    unsafe_allow_html=True
)
st.sidebar.image(top_image, use_container_width='auto')
st.sidebar.markdown(
    f'<center><a href="{URL}" target="_blank">{START_GAME}</a></center>',
    unsafe_allow_html=True
)


st.html(f'<center><strong style="font-size: 70px;">{NAME}</strong></center>')
st.html('<center><img width="80%" '
        'src="https://online-vitrina.ru/img/magi/game.png"></a></center>')
st.html(f'<center><a href="{URL}" target="_blank" alt="{START_GAME}"><img width="20%" '
        'src="https://online-vitrina.ru/img/magi/start.png"></a></center>')

st.markdown(
    f"<br><hr><center>All rights reserved &copy; 2025 "
    f"<a href='{URL}' target='_blank'>{NAME}</a></center>",
    unsafe_allow_html=True)