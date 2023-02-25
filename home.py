import datetime

import pandas as pd
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Multipage App",
    page_icon=":tada:",
    layout="wide"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- Load Assets ---
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ayzd33dj.json")
img_contact_form = Image.open("imgs/p1.jpeg")
img_lottie_animation = Image.open("imgs/rp.jpeg")

# --- Header Section ---
with st.container():
    st.title("Main Page")
    st.sidebar.success("Select a page above.")

    # my_input = st.text_input("Input a text here ", st.session_state["my_input"])
    #
    # if "my_input" not in st.session_state:
    #     st.session_state["my_input"] = ""
    # submit = st.button("Submit")
    #
    # if submit:
    #     st.session_state["my_input"] = my_input
    #     st.write('You have entered: ', my_input)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("""
        ON my YouTube channel I am creating tutorials form people who:
        - are interested in ...
        - want to do ...
        - wants to learn ...
        
        If this sounds interesting to you, ...
        """)
        st.write("[YouTube Channel >](https://www.saibanaweb.com)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# --- Projects ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader('Integrate Lottie Animation Inside Your Streamlit App')
        st.write("""
        Learn how to use Lottie Files in Streamlit!
        Animations make our web more engaging and fun, and Lottie Files are the easiest way to do ...
        In this tutorial, I'll show you exactly how to do it
        """)
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How to Add a contact form to your streamlit App")
        st.write("""
        Want to add a contact form to your Streamlit website?
        In this video, ...
        """)
        st.markdown("[Watch Video ...](https://youtu.be/FOULV9Xij_8)")

with st.container():
    st.write("---")
    st.title('Map')
    st.write("---")

with st.container():
    first, second = st.columns(2)
    form_ = st.form("my_form")
    with form_:
        with first:
            st.session_state.horizontal = True
            razcvi = st.text_input("Razti: ")
            gzvts = st.text_input("Gzxlp: ")
            amb_radio = st.radio('Selecione o ambiente:',
                                 options=('AX', 'BZ', 'IX', 'RU'),
                                 horizontal=st.session_state.horizontal)
            amb = 1 if amb_radio == 'BR' else 2 if amb_radio == 'B2' else 3 if amb_radio == 'B3' else 4

        with second:
            st.session_state.horizontal = True
            tipo_radio = st.radio('Escolha do tipo de mapa:',
                                  options=('Direto', 'Inverso'),
                                  horizontal=st.session_state.horizontal)
            st.write("""
                        Direto -> passa condição
                        
                        Inverso -> recebe condição
                     """)
            tipo = 1 if tipo_radio == 'Direto' else 2

        with first:
            submitted = form_.form_submit_button("Submit")
            st.write(f'tipo: {tipo}\nambiente: {amb}')
            if submitted:
                if len(gzvts) > 4:
                    st.write('Tamanho máximo para grupo é de 4 caracteres')

                if len(razcvi) > 8:
                    st.write('Tamanho máximo para rotina é de 8 caracteres')
                if len(gzvts) <= 4 and len(razcvi) <= 8:
                    st.write(f'Rotina {razcvi}, Grupo: {gzvts}')

st.header('st.write')
df = pd.DataFrame({
    'first col': [1, 2, 3, 4],
    'second col': [10, 20, 30, 40]
})
st.write(df)

st.subheader('Date slider')
initial_date = datetime.datetime.strptime("01/01/2023", "%d/%m/%Y")
k = 365
dates_generated = list(pd.date_range(initial_date, periods=k))
start_time, end_time = st.select_slider(
    "Date range for the event?",
    options=dates_generated,
    value=(dates_generated[0], dates_generated[-1]))

st.subheader('Time slider')
time_generated = pd.period_range(start='2023-01-01', end='2023-01-01', freq='H')
start = '2023-01-01'
end = '2023-01-31'
dates = list(pd.date_range(start=start, end=end, freq='H'))

i = 0
h = [hora.strftime("%H:%M:%S") for hora in dates if (i := i + 1) < 24]
for elm in h:
    st.write(elm)

st.write(f'The event should happen between {start_time.strftime("%d/%m/%Y")} and {end_time.strftime("%d/%m/%Y")}')
