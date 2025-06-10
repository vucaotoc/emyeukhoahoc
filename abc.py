import streamlit as st
import random

# Tiêu đề ứng dụng
st.title("Trò Chơi Bao Kéo Búa")

# Tùy chọn cho người chơi
choices = ["Bao", "Kéo", "Búa"]
player_choice = st.selectbox("Chọn của bạn:", choices)

# Nút để chơi
if st.button("Chơi"):
    # Máy chọn ngẫu nhiên
    computer_choice = random.choice(choices)
    
    # Hiển thị lựa chọn
    st.write(f"Bạn chọn: {player_choice}")
    st.write(f"Máy chọn: {computer_choice}")
    
    # Xác định kết quả
    if player_choice == computer_choice:
        st.write("Hòa!")
    elif (player_choice == "Bao" and computer_choice == "Búa") or \
         (player_choice == "Kéo" and computer_choice == "Bao") or \
         (player_choice == "Búa" and computer_choice == "Kéo"):
        st.write("Bạn thắng! 🎉")
    else:
        st.write("Máy thắng! 😢")

# Hướng dẫn chơi
st.markdown("""
### Hướng dẫn:
- Bao thắng Búa
- Kéo thắng Bao
- Búa thắng Kéo
Chọn một tùy chọn và nhấn 'Chơi' để bắt đầu!
""")
