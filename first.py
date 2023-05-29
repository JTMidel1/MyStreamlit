import streamlit as st

st.title("Hello little Donald")

st.header("Names of my Heroes")
st.subheader("Donald, Ronald and Natasha")
st.text("Hello Great People of MX City, we are hitting \n the city loud with the buzz of excitement")
st.markdown('### We are here')

st. success("Successfully joined")
st.info('need further information, Hi')
st.warning("You btter be careful nexttime, mayn't be funny as now")
st.error('Oh sorry')
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.write("Text Here")
st.write(range(10))

from PIL import Image
img = Image.open("streamlit.jpg")
st.image(img, width=200)

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")

status = st.radio("Select Gender:", ('Male', 'Female'))
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies:", ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')

st.button("What's up, click me")

if (st.button("About")):
    st.text("Welcome to DRT Study Group!!!")

name = st.text_input("Enter Your name", "Type Here ....")
if(st.button('Submit')):
    result = name.title()
    st.success(result)

level = st.slider("Select the level", 1, 5)
st.text('Selected: {}'.format(level))


