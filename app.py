import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Your Name - Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #f0f2f6;
        padding-bottom: 0.5rem;
    }
    .experience-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.2rem;
    }
    .experience-company {
        font-size: 1.1rem;
        color: #4682B4;
        margin-bottom: 0.2rem;
    }
    .experience-date {
        font-size: 0.9rem;
        color: #808080;
        margin-bottom: 0.5rem;
    }
    .skill-box {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 5px 10px;
        margin: 5px;
        display: inline-block;
    }
    .social-icons a {
        margin-right: 15px;
        text-decoration: none;
    }
    .project-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .contact-info {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    # Replace with your own image
    st.image("https://via.placeholder.com/300", width=250)

    st.markdown("## Navigation")
    nav_selection = st.radio("Go to",
                             ["Summary", "Experience", "Education", "Skills", "Projects", "Hobbies", "Contact"])

    st.markdown("---")
    st.markdown("## Social Links")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a>""",
                    unsafe_allow_html=True)
    with col2:
        st.markdown("""<a href="https://github.com/yourusername" target="_blank">GitHub</a>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<a href="https://twitter.com/yourhandle" target="_blank">Twitter</a>""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-header">Your Name</div>', unsafe_allow_html=True)
st.markdown('**Professional Title** | City, Country | email@example.com')

# Summary section
if nav_selection == "Summary":
    st.markdown('<div class="section-header">Professional Summary</div>', unsafe_allow_html=True)
    st.write("""
    I am a passionate [Your Profession] with [X years] of experience in [Your Field]. 
    Specializing in [Your Specialization], I have successfully delivered projects for 
    [types of clients/companies]. I am skilled in [Key Skills] and committed to 
    [what you're passionate about in your work].

    Currently seeking opportunities to [your career goals].
    """)

# Experience section
elif nav_selection == "Experience":
    st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)

    # Experience 1
    st.markdown('<div class="experience-title">Senior Developer</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-company">ABC Technology Inc.</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-date">January 2020 - Present</div>', unsafe_allow_html=True)
    st.markdown("""
    - Led development of a cloud-based solution that increased client efficiency by 35%
    - Managed a team of 5 developers across 3 different time zones
    - Implemented CI/CD pipeline that reduced deployment time by 40%
    - Collaborated with product management to define and prioritize features
    """)

    # Experience 2
    st.markdown('<div class="experience-title">Web Developer</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-company">XYZ Solutions</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-date">March 2017 - December 2019</div>', unsafe_allow_html=True)
    st.markdown("""
    - Developed responsive web applications using React and Node.js
    - Implemented RESTful APIs that served data to various client applications
    - Optimized database queries resulting in 30% performance improvement
    - Collaborated with UX designers to implement user-friendly interfaces
    """)

# Education section
elif nav_selection == "Education":
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

    # Education 1
    st.markdown('<div class="experience-title">Master of Science in Computer Science</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-company">University Name</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-date">2015 - 2017</div>', unsafe_allow_html=True)
    st.write("Thesis: 'Topic of Your Thesis'")
    st.write("GPA: 3.8/4.0")

    # Education 2
    st.markdown('<div class="experience-title">Bachelor of Science in Information Technology</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="experience-company">University Name</div>', unsafe_allow_html=True)
    st.markdown('<div class="experience-date">2011 - 2015</div>', unsafe_allow_html=True)
    st.write("Minor: Business Administration")
    st.write("GPA: 3.7/4.0")

    # Certifications
    st.markdown('<div class="section-header">Certifications</div>', unsafe_allow_html=True)
    st.markdown("""
    - AWS Certified Developer - Associate (2023)
    - Google Professional Cloud Developer (2022)
    - Certified Scrum Master (2021)
    """)

# Skills section
elif nav_selection == "Skills":
    st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)

    # Technical Skills
    st.subheader("Technical Skills")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="skill-box">Python</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">JavaScript</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">React</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">Node.js</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="skill-box">SQL</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">MongoDB</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">Docker</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">AWS</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="skill-box">Git</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">CI/CD</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">RESTful APIs</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">GraphQL</div>', unsafe_allow_html=True)

    # Soft Skills
    st.subheader("Soft Skills")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="skill-box">Team Leadership</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">Project Management</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="skill-box">Problem Solving</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">Communication</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="skill-box">Agile/Scrum</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-box">Time Management</div>', unsafe_allow_html=True)

# Projects section
elif nav_selection == "Projects":
    st.markdown('<div class="section-header">Key Projects</div>', unsafe_allow_html=True)

    # Project 1
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("E-Commerce Platform")
        st.write("**Technologies:** React, Node.js, MongoDB, AWS")
        st.write("""
        Developed a full-stack e-commerce solution with secure payment integration, 
        inventory management, and user authentication. Implemented responsive design
        and optimization techniques resulting in 50% faster page load times.
        """)
        cols = st.columns([1, 1])
        with cols[0]:
            st.markdown("[GitHub Repo](https://github.com/yourusername/project)")
        with cols[1]:
            st.markdown("[Live Demo](https://example.com)")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 2
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("Data Visualization Dashboard")
        st.write("**Technologies:** Python, Streamlit, Pandas, Plotly")
        st.write("""
        Created an interactive dashboard for analyzing business metrics and KPIs.
        Features include real-time data updates, customizable views, and export functionality.
        Used by management team to make data-driven decisions.
        """)
        cols = st.columns([1, 1])
        with cols[0]:
            st.markdown("[GitHub Repo](https://github.com/yourusername/project)")
        with cols[1]:
            st.markdown("[Live Demo](https://example.com)")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 3
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("Machine Learning Recommendation System")
        st.write("**Technologies:** Python, TensorFlow, Flask, Docker")
        st.write("""
        Developed a recommendation engine that increased user engagement by 28%.
        Implemented collaborative filtering and content-based approaches with A/B testing
        to optimize recommendation accuracy.
        """)
        cols = st.columns([1, 1])
        with cols[0]:
            st.markdown("[GitHub Repo](https://github.com/yourusername/project)")
        with cols[1]:
            st.markdown("[Case Study](https://example.com)")
        st.markdown('</div>', unsafe_allow_html=True)

# Hobbies section
elif nav_selection == "Hobbies":
    st.markdown('<div class="section-header">Hobbies & Interests</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏃‍♂️ Fitness")
        st.write("""
        I enjoy staying active through running, swimming, and yoga.
        Completed two half-marathons and currently training for a full marathon.
        """)

        st.subheader("📚 Reading")
        st.write("""
        Avid reader of science fiction, philosophy, and technical books.
        Current favorite authors include Liu Cixin, Ted Chiang, and Ray Dalio.
        """)

    with col2:
        st.subheader("🎸 Music")
        st.write("""
        Play guitar in a local band. Enjoy everything from classical to rock.
        Recently started learning piano as well.
        """)

        st.subheader("✈️ Travel")
        st.write("""
        Passionate about exploring different cultures and cuisines.
        Have visited 15 countries across 4 continents. Next destination: Japan.
        """)

# Contact section
elif nav_selection == "Contact":
    st.markdown('<div class="section-header">Contact Information</div>', unsafe_allow_html=True)

    st.markdown('<div class="contact-info">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📧 Email")
        st.write("email@example.com")

        st.subheader("📱 Phone")
        st.write("+1 (555) 123-4567")

    with col2:
        st.subheader("📍 Location")
        st.write("City, Country")

        st.subheader("💼 Work Status")
        st.write("Open to new opportunities")
    st.markdown('</div>', unsafe_allow_html=True)

    # Contact form
    st.markdown('<div class="section-header">Get In Touch</div>', unsafe_allow_html=True)

    contact_form = st.form(key="contact_form")
    with contact_form:
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        st.success("Thanks for reaching out! I'll get back to you shortly.")

# Footer
st.markdown("---")
st.markdown("© 2025 Your Name | Portfolio created with Streamlit")