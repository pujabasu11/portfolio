import streamlit as st

# Page Configuration
st.set_page_config(page_title="MBA Portfolio - [Your Name]", layout="centered")

# Sidebar - Contact Info
st.sidebar.title("📇 Contact")
st.sidebar.markdown("""
**[Your Name]**  
MBA Candidate | [Your Specialization]  
📧 [your.email@example.com]  
📍 [City, Country]  

[LinkedIn](https://linkedin.com/in/your-profile)  
[GitHub](https://github.com/your-username)  
[Twitter](https://twitter.com/your-handle)
""")

# Main Title
st.title("👋 Hello, I'm [Your Full Name]")
st.markdown("### MBA Candidate | [Your University Name] | Class of [Year]")

# Summary Section
st.header("📝 Professional Summary")
st.write("""
Motivated and results-driven MBA candidate with a strong foundation in [Finance/Marketing/Strategy/Operations/etc.], and hands-on experience in solving complex business problems through data-driven insights. 
Possess strong analytical thinking, leadership, and cross-functional collaboration skills. Currently seeking opportunities in [Industry/Role], where I can leverage my business acumen and strategic mindset.
""")

# Education Section
st.header("🎓 Education")
st.write("""
**Master of Business Administration (MBA)**  
[University Name], [Location] – Class of [Year]  
- Specialization: [Your Focus Area]  
- GPA: [If Applicable]  
- Key Courses: Strategic Management, Marketing Analytics, Financial Modeling  

**Bachelor of [Your Degree]**  
[University Name], [Location] – [Year]  
- Relevant Coursework: [List a few courses or achievements]
""")

# Experience Section
st.header("💼 Professional Experience")
st.write("""
**[Job Title]** – [Company Name], [Location]  
*[Month, Year] – [Month, Year]*  
- Led [project/initiative], achieving [measurable outcome].  
- Conducted market analysis to support [strategy/product].  
- Collaborated with cross-functional teams on [key task].

**[Internship Title]** – [Company Name], [Location]  
*[Month, Year] – [Month, Year]*  
- Designed a [report/dashboard/model] used by leadership to [impact].  
- Supported [business function], resulting in [result/achievement].
""")

# Skills Section
st.header("🛠️ Skills")
st.write("""
- **Business & Strategy:** SWOT Analysis, Business Model Canvas, Go-to-Market Strategy  
- **Analytics & Tools:** Excel, SQL, Python, Tableau, Power BI  
- **Soft Skills:** Leadership, Communication, Teamwork, Problem-solving
""")

# Projects Section
st.header("🚀 Key Projects")
st.write("""
**Market Entry Strategy for [Company]**  
Developed a comprehensive entry strategy into the [new market] including competitive analysis, pricing, and financial projections.

**Customer Segmentation using Python**  
Used clustering techniques on customer datasets to improve targeting and marketing ROI for a retail brand.

**Operations Optimization Case**  
Simulated production schedules to improve efficiency by 15% in a capstone project.

More on: [GitHub](https://github.com/your-username)
""")

# Hobbies Section
st.header("🎯 Interests & Hobbies")
st.write("""
Passionate about startups, emerging tech, behavioral economics, and global markets.  
Outside of work, I enjoy [Hobby 1], [Hobby 2], and volunteering for [cause/organization].
""")

# Footer
st.markdown("---")
st.markdown("© [Your Name] • Built with ❤️ using Streamlit")

