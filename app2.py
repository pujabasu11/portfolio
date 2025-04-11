import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="MBA Portfolio - [Your Name]", layout="wide")

# ---- Custom CSS ----
def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main-title {
            font-size: 2.8rem;
            font-weight: 600;
            color: #1F4E79;
        }

        .section-header {
            font-size: 1.5rem;
            margin-top: 2rem;
            color: #0B3C5D;
            border-bottom: 2px solid #EAECEE;
            padding-bottom: 0.5rem;
        }

        .info-card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        .profile-pic {
            border-radius: 50%;
            width: 180px;
            border: 4px solid #1F4E79;
        }

        .social-icons a {
            text-decoration: none;
            color: #1F4E79;
            font-weight: 500;
            margin-right: 15px;
        }

        .footer {
            margin-top: 3rem;
            font-size: 0.9rem;
            text-align: center;
            color: #888;
        }
    </style>
    """, unsafe_allow_html=True)

# ---- Load CSS ----
load_css()

# ---- Main Layout ----
col1, col2 = st.columns([1, 3])

with col1:
   # profile_pic = Image.open("profile.jpg")  # Replace with your image
    #st.image(profile_pic, caption='[Your Name]', use_column_width=False)

with col2:
    st.markdown("<div class='main-title'>👋 Hi, I'm [Your Name]</div>", unsafe_allow_html=True)
    st.write("MBA Candidate at [Your University] | Specializing in [e.g. Marketing, Strategy, Finance]")
    st.markdown("""
    <div class='social-icons'>
        📧 [your.email@example.com]  
        🔗 <a href='https://linkedin.com/in/your-profile' target='_blank'>LinkedIn</a>
        💻 <a href='https://github.com/your-github' target='_blank'>GitHub</a>
        🐦 <a href='https://twitter.com/your-handle' target='_blank'>Twitter</a>
    </div>
    """, unsafe_allow_html=True)

# ---- Summary ----
st.markdown("<div class='section-header'>📝 Professional Summary</div>", unsafe_allow_html=True)
st.markdown("""
<div class='info-card'>
Motivated and results-oriented MBA candidate with strong analytical, strategic, and leadership skills. 
Experienced in [finance, marketing, operations], with a proven track record in solving complex business problems through data-driven insights and cross-functional collaboration.
</div>
""", unsafe_allow_html=True)

# ---- Education ----
st.markdown("<div class='section-header'>🎓 Education</div>", unsafe_allow_html=True)
st.markdown("""
<div class='info-card'>
<b>MBA, [Your Specialization]</b>  
[Your University], [Location] — Class of [Year]  
- GPA: [GPA]  
- Key Courses: Corporate Strategy, Financial Modeling, Marketing Analytics

<b>Bachelor's in [Your Degree]</b>  
[University Name], [Location] — [Year]  
</div>
""", unsafe_allow_html=True)

# ---- Experience ----
st.markdown("<div class='section-header'>💼 Experience</div>", unsafe_allow_html=True)
st.markdown("""
<div class='info-card'>
<b>[Job Title]</b> – [Company Name]  
<i>[Month, Year] – [Month, Year]</i>  
• Spearheaded [project/initiative] to improve [result].  
• Conducted analysis leading to [impact].  
• Collaborated with cross-functional teams on [goal].

<b>[Internship Title]</b> – [Company Name]  
<i>[Month, Year] – [Month, Year]</i>  
• Worked on [business case/model/dashboard].  
• Presented insights to senior management.
</div>
""", unsafe_allow_html=True)

# ---- Skills ----
st.markdown("<div class='section-header'>🧠 Skills</div>", unsafe_allow_html=True)
st.markdown("""
<div class='info-card'>
<b>Business & Strategy:</b> Competitive Analysis, GTM Strategy, SWOT, PESTEL  
<b>Analytics & Tools:</b> Excel, SQL, Python, Tableau, Power BI  
<b>Soft Skills:</b> Leadership, Communication, Teamwork, Time Management  
</div>
""", unsafe_allow_html=True)

# ---- Projects ----
st.markdown("<div class='section-header'>🚀 Key Projects</div>", unsafe_allow_html=True)
st.markdown("""
<div class='info-card'>
<b>Market Entry Strategy – [Company Name]</b><br>
Developed a go-to-market strategy for expansion into Southeast Asia including pricing, competitor benchmarking, and financial forecasts.

<b>Customer Segmentation Using Python</b><br>
Applied K-means clustering on customer transaction data to improve targeting and marketing efficiency by 25%.

<b>Operations Optimization Model</b><br>
Created simulation models to streamline production processes and reduce cost by 15%.
</div>
""", unsafe_allow_html=True)

# ---- Hobbies ----
st.markdown("<div class='section-header'>🎯 Interests & Hobbies</div>", unsafe_allow_html=True)
st.markdown("""
<div class='info-card'>
Apart from business strategy and data analytics, I enjoy hiking, photography, playing chess, and following startup trends and behavioral economics.
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("<div class='footer'>© 2025 [Your Name] • Designed with ❤️ using Streamlit</div>", unsafe_allow_html=True)
