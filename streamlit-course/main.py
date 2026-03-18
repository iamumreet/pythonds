import streamlit as st
import pandas as pd

users = {
    "name": ['Amrit', 'Bobby', 'Smile'],
    "age": [24,26,32]
}

pd.DataFrame(users)
st.title("My Web App")
st.write("user list")
st.dataframe(users)