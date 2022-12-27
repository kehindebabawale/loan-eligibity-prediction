import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image


#load model
model = pickle.load(open('Loan_status_Prediction_RF.pkl', 'rb'))
# set title
st.set_page_config(
    page_title="Loan Eligibilty prediction App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': "https://github.com/kehindebabawale",
        'About': "# Developed by Babawale Kehinde. This is an *extremely* cool app!"
    }
)
st.title("Loan Eligibilty prediction App")
st.write("Welcome, This is a loan predictor app developed by Babawale kehinde")
#set backgroud inage
background_image  = Image.open('loan background.jpg')
st.image(background_image, width = 1000)

##input features 
st.sidebar.subheader("Please input followings details and click on predict button.")
Name = st.sidebar.text_input("Name")
Current_Loan_Amt =st.sidebar.number_input("Loan Amount",100)
Term = st.sidebar.selectbox('loan Term', ['Long', 'short'])
Credit_Score = st.sidebar.number_input("Credit score", min_value= 0, max_value = 1000 )
Annual_Income = st.sidebar.number_input("Annual income")
Years_in_current_job = st.sidebar.slider("Years in current job", 1,10,1)
Home_Ownership = st.sidebar.selectbox("Home ownership Status", ("Own Home", "Rent", "Home Mortage"))
Monthly_Debt = st.sidebar.number_input("Outstanding Monthly debt")
Years_of_Credit_History = st.sidebar.slider("Year of Credit history", 1,70,1)
Num_of_Open_Accts = st.sidebar.number_input("Number of Account Opened", min_value= 0, max_value = 1000 )
Num_of_Credit_Problems= st.sidebar.slider("Number of credit card problem", 1,70,1)
Current_Credit_Balance = st.sidebar.number_input("Current Credit Balance")
Maximum_Open_Credit = st.sidebar.number_input("Current Credit Limit")
Purpose = st.sidebar.selectbox("purpose of the Loan", ('Home Improvements', 'Debt Consolidation', 'Buy House', 'other',
       'Business Loan', 'Buy a Car', 'major_purchase', 'Take a Trip',
       'Other', 'small_business', 'Medical Bills', 'wedding', 'vacation',
       'Educational Expenses', 'moving', 'renewable_energy'))
##create predict function
def predict():
    row = np.array([Current_Loan_Amt, Term, Credit_Score,
       Annual_Income, Years_in_current_job, Home_Ownership, Purpose,
       Monthly_Debt, Years_of_Credit_History, Num_of_Open_Accts,
       Num_of_Credit_Problems, Current_Credit_Balance,
       Maximum_Open_Credit])
    columns = ['Current_Loan_Amt', 'Term', 'Credit_Score',
       'Annual_Income', 'Years_in_current_job', 'Home_Ownership', 'Purpose',
       'Monthly_Debt', 'Years_of_Credit_History', 'Num_of_Open_Accts',
       'Num_of_Credit_Problems', 'Current_Credit_Balance',
       'Maximum_Open_Credit']
    ### covert features array to pandas dataframe

    X = pd.DataFrame([row], columns= columns)
    

    ##make predictions
    prediction = model.predict(X)[0]

    if prediction ==1:
        st.write("Dear " + str(Name) + " you are currently eligible for "+  str(Current_Loan_Amt) +  " loan." )
        st.balloons()
        Approval_image  = Image.open('loan approval.jpg')
        st.image(Approval_image, width = 500)
    else:
        st.write("Sorry, you are currently not eligible for "+  str(Current_Loan_Amt) +  " loan." )
        Denied_image  = Image.open('OIP.png')
        st.image(Denied_image, width = 500)
st.button("predict", on_click = predict)


