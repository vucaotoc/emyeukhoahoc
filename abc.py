import streamlit as st
import random

st.set_page_config(page_title="Game Oẳn Tù Tì", page_icon="✌️", layout="centered")

# Giao diện
st.title("✊✋✌️ Oẳn Tù Tì")
st.write("Chọn 1 trong 3 và chơi với máy!")

# Danh sách lựa chọn
choices = ["✊ Búa", "✋ Bao", "✌️ Kéo"]
choice_map = {
    "✊ Búa": "rock",
    "✋ Bao": "paper",
    "✌️ Kéo": "scissors"
}

# Người chơi chọn
player_choice = st.radio("Bạn chọn:", choices)

if st.button("👊 Oẳn Tù Tì!"):
    player = choice_map[player_choice]
    computer = random.choice(["rock", "paper", "scissors"])

    st.write(f"🤖 Máy chọn: **{computer}**")
    
    # Kết quả
    if player == computer:
        st.info("⚖️ Hòa nhau rồi!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        st.success("🎉 Bạn thắng!")
    else:
        st.error("😢 Bạn thua rồi!")

    st.markdown("---")

    st.button("Chơi lại")  # chỉ để refresh giao diện

