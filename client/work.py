import streamlit as st
import requests

st.markdown(
    """
    <style>
    .stApp {
        background:linear-gradient(135deg, #667eea, #764ba2);
    }
    </style>
    """,
    unsafe_allow_html=True
)



Fast_URL = "http://127.0.0.1:8000/login"

st.title(f"Streamlit + FastAPI Trial")

st.write("Write a message to FastAPI")

username = st.text_input("Username")
password = st.text_input("Password",type="password")

if st.button("Login"):
    try:
        response = requests.post(Fast_URL, json={"username": username,"password":password})
        if response.status_code == 200:
            st.success("message")
        else:
            error_data = response.json()
            st.error(error_data.get("detail", "Login failed"))
    except Exception as e:
        st.error(f"This is the error--> {e}")
else:
    st.warning("Please enter both username and password")

# us_inp = st.text_input("Enter your message:")

# if st.button("send to fastapi"):
#     if us_inp:
#         response = requests.post(
#             f"{Fast_URL}/send",
#             json={"text":us_inp}
#         )

#         if response.status_code == 200:
#             data = response.json()
#             st.success(data["response"])
#         else:
#             st.error("Error with communicating with backend")

