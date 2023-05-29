import streamlit as st

st.title("Welcome to BMI Calculator")

weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

if(status == 'cms',):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(status == 'meters'):
    try: 
        height = st.number_input('Meters')
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")

else: 
    height = st.number_input('Feet')
   
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}." .format(bmi))
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.warning("You are underweight")
    elif(bmi >= 25 and bmi < 30):
        st.success("Healthy")
    elif(bmi >= 30):
        st.error("EXtremely Overweight")
