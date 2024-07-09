import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("CURRENCY_API_KEY")

st.header("Simple Currency Converter")

v1 = st.text_input("Enter the currency code of your initial currency(eg: USD,INR,etc)")

v2 = st.text_input(
    "Enter the curency code of the currency you want to convert to(eg: USD,INR,etc)"
)

val = round(st.number_input("Enter amount of original currency"), 2)

booly = v1 and v2

if booly:

    url = (
        "http://api.exchangeratesapi.io/v1/latest?access_key="
        + API_KEY
        + "&symbols="
        + v1
        + ","
        + v2
    )

    data = data = requests.get(url)

    real_data = data.json()

    c1 = real_data["rates"][v2]

    c2 = real_data["rates"][v1]

    new_val = round((val * c1 / c2), 2)

    stringy = str(val) + " " + v1 + " is " + str(new_val) + " " + v2

    st.write(stringy)
else:
    st.write("Please input two currency codes")
