import streamlit as st
from PIL import Image

# Cấu hình trang
st.set_page_config(page_title="CV - Hanna", page_icon="💼", layout="wide")

# ====== HEADER + ẢNH ======
col1, col2 = st.columns([1, 3])

with col1:
    image = Image.open("avatar.jpg")  # Đặt ảnh cùng thư mục với cv.py
    st.image(image, caption="Hanna - IT Developer", width=150)

with col2:
    st.title("💼 Curriculum Vitae")
    st.subheader("Hanna - IT Developer")
    st.write("📍 Hồ Chí Minh, Việt Nam | 📧 hanna@example.com | 📞 +84 912 345 678")

st.markdown("---")

# ====== GIỚI THIỆU ======
st.header("🧑‍💻 Giới thiệu bản thân")
st.write("""
Tôi là một lập trình viên đam mê công nghệ, có kinh nghiệm trong phát triển phần mềm, web app, và hệ thống cơ sở dữ liệu. 
Tôi yêu thích việc xây dựng giải pháp tự động và tối ưu hóa hiệu suất hệ thống.
""")

# ====== KỸ NĂNG ======
st.header("🛠 Kỹ năng")
skills = {
    "Ngôn ngữ": ["Java", "C#", "Python", "JavaScript"],
    "Web/Frontend": ["HTML", "CSS", "React", "Streamlit"],
    "Cơ sở dữ liệu": ["SQL Server", "MySQL", "SQLite"],
    "Khác": ["Git", "Docker", "REST API", "Postman"]
}
for category, skill_list in skills.items():
    st.subheader(f"🔹 {category}")
    st.write(", ".join(skill_list))

# ====== HỌC VẤN ======
st.header("🎓 Học vấn")
st.write("""
**Cử nhân Công nghệ Thông tin**  
Đại học ABC, 2016 - 2020  
- Chuyên ngành: Hệ thống thông tin  
- GPA: 3.6/4.0
""")

# ====== KINH NGHIỆM ======
st.header("💼 Kinh nghiệm làm việc")
st.write("""
**Lập trình viên Java**  
Công ty XYZ | 2021 - Nay  
- Phát triển và bảo trì các hệ thống ERP nội bộ bằng Java/SQL Server  
- Thiết kế các dashboard bằng AdminLTE, tích hợp REST API và xử lý dữ liệu lớn

**Thực tập sinh Python Developer**  
Công ty DEF | 2020 - 2021  
- Tham gia dự án phát triển phần mềm chấm công bằng Python và Streamlit  
- Viết module trích xuất dữ liệu từ Excel và hiển thị biểu đồ báo cáo
""")

# ====== DỰ ÁN NỔI BẬT ======
st.header("🚀 Dự án nổi bật")
st.write("""
- **CampusExpense Manager**: Ứng dụng quản lý chi tiêu sinh viên (Android + SQLite)  
- **Smart IoT Home**: Hệ thống nhà thông minh điều khiển bằng ESP8266 + Blynk  
- **Appraisal Management System**: Web app đánh giá nhân sự dùng Java Servlet + SQL Server
""")

# ====== LIÊN HỆ ======
st.header("📬 Liên hệ")
with st.form("contact_form"):
    name = st.text_input("Tên của bạn")
    email = st.text_input("Email của bạn")
    message = st.text_area("Tin nhắn")
    submitted = st.form_submit_button("Gửi tin nhắn")
    if submitted:
        st.success("✅ Cảm ơn bạn! Tin nhắn đã được gửi.")

