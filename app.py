import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="AI Resume Builder", page_icon="📄", layout="centered")

st.title("📄 AI Resume Builder - Internship Ready")
st.markdown("Build ATS-friendly resume in 2 minutes!")

# Sidebar
st.sidebar.header("Your Details")
name = st.sidebar.text_input("Full Name", "Abhishek Kumar")
email = st.sidebar.text_input("Email", "abhishek@email.com")
phone = st.sidebar.text_input("Phone", "+91 1234567890")
linkedin = st.sidebar.text_input("LinkedIn")
address = st.sidebar.text_input("Address")

st.header("1. Professional Summary")
summary = st.text_area("Summary", "Motivated Computer Science student with strong skills in Python, Cybersecurity, and AI. Seeking internship to apply knowledge.", height=80)

st.header("2. Education")
education = st.text_area("Education", "B.Tech Computer Science, Your University, 2022-2026\nCGPA: 8.5")

st.header("3. Skills")
skills = st.text_area("Skills", "Python, Java, Cybersecurity, AI, Machine Learning, SQL")

st.header("4. Projects")
projects = st.text_area("Projects", "AI Resume Builder - Built using Python and Streamlit\nCybersecurity Tool - Python based scanner")

st.header("5. Internships / Experience")
experience = st.text_area("Experience", "No experience yet - Seeking Internship")

if st.button("Generate Resume PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, name, ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 5, f"{email} | {phone} | {linkedin}", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Professional Summary", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 5, summary)
    pdf.ln(3)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Education", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 5, education)
    pdf.ln(3)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Skills", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 5, skills)
    pdf.ln(3)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Projects", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 5, projects)
    pdf.ln(3)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Experience", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 5, experience)
    
    pdf.output("resume.pdf")
    st.success("Resume Generated! Download below")
    with open("resume.pdf", "rb") as f:
        st.download_button("Download PDF", f, file_name=f"{name}_Resume.pdf")
