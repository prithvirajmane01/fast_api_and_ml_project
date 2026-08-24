import streamlit as st
import requests

API_URL="http://127.0.0.1:8000/predict"
st.title("loan prediction")

st.markdown("enter the detail")

income=st.number_input("income(lakh)",min_value=1.0)
age=st.number_input("enter the age",min_value=1.0)
loan=st.number_input("enter the loan amount",min_value=1.0)


if st.button("predict premium"):
    input_data={
        "income":income,
        "age":age,
        "loan":loan
    }

    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"predict :**{result['prediction_category']}**")
        else:
            st.error(f"api error:{response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("no connection")
