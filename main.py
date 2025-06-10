import streamlit as st
import pandas as pd
# Thiết lập giao diện trang
st.set_page_config(page_title="Đăng nhập hệ thống", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
        .stTextInput > div > div > input {
            background-color: #f9f9f9;
        }
        .login-box {
            max-width: 400px;
            margin: auto;
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("## 🔐 Đăng nhập hệ thống")

    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng nhập"):
        if username == "admin" and password == "123456":
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tài khoản hoặc mật khẩu.")
    st.markdown("</div>", unsafe_allow_html=True)
