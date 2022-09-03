from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Meet Jethwa"
PAGE_ICON = ":wave:"
NAME = "Meet Jethwa"
DESCRIPTION = """
MTech Artificial Intelligence || Chatbot Developer at Capgemini, Vsiting Faculty at NMIMS.
"""
EMAIL = "meetjethwa3@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCOoR4Ots08TrmlF3zfFRIVw",
    "LinkedIn": "www.linkedin.com/in/meet-jethwa7",
    "GitHub": "https://github.com/Meet2147/Meet2147",
    "Twitter": "https://twitter.com/coder_meet78",
}
PROJECTS = {
    "🏆 Computer Vision - Clicking a selfie on Smile Detection": "https://youtu.be/-TlSB21Iocw",
    "🏆 Computer Vision - Mask Detection": "https://youtu.be/KZINTRXB_hU",
    "🏆 Chatbot Whatsapp Integration - Rasa Chatbot": "https://youtu.be/485sz_Sp2VM",
    "🏆 Smart Mirror Using Raspberry Pi - Raspberry Pi": "https://youtu.be/307gZfO120A",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3+ Years expereince in Software Development, AWS, AWS Lambda, AWS S3, DynamoDB, Serverless
- ✔️ Strong hands on experience and knowledge in Python and MySQL
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: Plotly, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases:  MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Chatbot Developer | Capgemini**")
st.write("06/2022 - Present")
st.write(
    """
- ► Using chatbot frameworks to develop chatbots as per different requirements of clients.
- ► Taking care of the Integrations of Chatbot backend with required frontend apps
- ► Integrated Chatbot to whatsapp, telegram, alexa
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Technical Lead | AAIC**")
st.write("02/2021 - 06/2022")
st.write(
    """
- ► Developed Application api using AWS services
- ► Led a team of 4 Developers, Moderated code written by developers, merged code 
- ► Designed and Developed a project for Unit testing using BDD framework
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Software Associate(Devops) | Xpanxion International**")
st.write("01/2017 - 07/2018")
st.write(
    """
- ► Trained on devops tools and orchestration tools like chef, vagrant
- ► Designed and developed a POC for a client to perform continuous monitoring using zabbix
- ► Performed MySQL queries on Ubuntu Server for timely cleaning of data.
"""
)


# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
