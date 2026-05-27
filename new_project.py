import streamlit as st
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import graphviz

st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Display another image from a URL
st.subheader("Image from Google:")
image_url = "https://awsimages.detik.net.id/community/media/visual/2024/08/21/giant-panda-atau-panda-raksasa.jpeg"
st.image(image_url)

# Display a video from YouTube using an iframe (Streamlit does not natively support YouTube embeds)
st.subheader("Video from YouTube:")
youtube_url = "https://www.youtube.com/watch?v=ljoY1W6gPnY"
st.components.v1.html(
    f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_url.split('=')[-1]}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, 
    height=315
)
st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()

st.subheader("Progress Bar")
st.progress(10)

st.subheader("Wait the execution")
with st.spinner("Wait for it..."):
    time.sleep(2)

st.balloons()  # Celebration balloons
st.progress(2)  # Progress bar
with st.spinner('Wait for it...'):
    time.sleep(2)  # Simulating a process delay

st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male","Female"])

with st.container():
    st.write("This is inside the container")
container = st.container()
container.write("This is written inside the container")
st.write("THis is written outside the container")

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

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']
)
st.map(df)
