import streamlit as st
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz

st.title("Pertemuan 14")
st.write("Pada pertemuan ke-14 ini, kita akan membahas tentang penggunaan Stream")
st.write("Stream adalah sebuah library Python yang digunakan untuk membuat aplikasi web interaktif dengan mudah. Dengan Stream, kita dapat membuat aplikasi web yang dapat menampilkan data secara real-time, membuat dashboard, dan banyak lagi.")
st.write("Berikut adalah beberapa contoh penggunaan Stream:")

st.title("Mareko Famaogombowo Nazara")
st.header("Matana University Student")
st.markdown("NIM : 20254920001")
st.subheader("Pembelajaran Stream")
st.caption("HAHAHAHAHAHAHAHAHAH")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Display another image from a URL
st.subheader("Image from Google:")
image_url = "https://preview.redd.it/resonator-preview-aemeath-v0-fgsw4lrzu1bg1.jpeg?auto=webp&s=69b7a25b9c8710d19b32c50f21e0d2718566af40"
st.image(image_url)

st.subheader("Songs:")
yt_url = "https://www.youtube.com/watch?v=hv6WWNwPN1c&list=RDhv6WWNwPN1c&start_radio=1"
st.video(yt_url)

st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)
st.text_input('Enter your name')
st.text_area('Enter your address')

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')



st.balloons()

st.subheader("Progress Bar")
st.progress(10)

st.subheader("Wait the execution")
with st.spinner("Wait for it..."):
    time.sleep(2)


st.balloons()  # Celebration balloons
st.progress(10)  # Progress bar
with st.spinner('Wait for it...'):
    time.sleep(2)  # Simulating a process delay
st.success('Done!')

st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male","Female"])
st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")

container = st.container()
container.write("This is written inside the container")
st.write("THis is written outside the container")
with st.container():
    st.write("This is inside the container")

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z']
)
st.altair_chart(chart, use_container_width=True)

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76,-122.4], columns=['lat','lon'])
st.map(df)
