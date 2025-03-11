import streamlit as st
from PIL import Image


NAME = "Онлайн-игра «Магический мир»"
URL = "https://mworld.mobi/?channelId=48644"
START_GAME = "Начни игру!"


st.set_page_config(
    page_title=NAME,
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

top_image = Image.open('static/magmir.jpg')
st.sidebar.markdown(f'<center><b>{NAME}</b></center>', unsafe_allow_html=True)
st.sidebar.markdown('<center>Прокачай своих героев и соревнуйся с другими игроками на арене, играя в «Три в ряд»'
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
        'src="https://online-vitrina.ru/img/magi/igra.png"></a></center>')

st.markdown(
    f"<br><hr><center>Все права защищены &copy; 2025 "
    f"<a href='{URL}' target='_blank'>{NAME}</a></center>",
    unsafe_allow_html=True)
