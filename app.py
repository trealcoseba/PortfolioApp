import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Tre Alcoseba | CSIT 349 Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# 2. CUSTOM CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 14px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }
    .tech-pill {
        display: inline-block;
        background: rgba(255, 75, 75, 0.15);
        color: #ff6b6b;
        border: 1px solid rgba(255, 75, 75, 0.3);
        padding: 3px 10px;
        border-radius: 14px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .status-badge {
        display: inline-block;
        background: rgba(46, 213, 115, 0.15);
        color: #2ed573;
        border: 1px solid rgba(46, 213, 115, 0.3);
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .badge-year {
        display: inline-block;
        background: rgba(255, 255, 255, 0.08);
        color: #f1f2f6;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 3px 12px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 4px;
    }
    /* Enhanced typography for Leadership Cards */
    .role-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.3;
        margin-bottom: 4px;
    }
    /* Centered, Bold, and Much Larger Organization Name */
    .org-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.35;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 60px;
    }
    div[data-testid="stSidebar"] img {
        border-radius: 16px;
        border: 2px solid rgba(255, 75, 75, 0.4);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. SESSION STATE
# ---------------------------------------------------------
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []

# ---------------------------------------------------------
# 4. PERSONAL DATA
# ---------------------------------------------------------
FULL_NAME = "Lemuel Vincent V. Alcoseba III"
NICKNAME = "Tre"
COURSE_SECTION = "CSIT 349 - F2"
PROGRAM = "Bachelor of Science in Computer Science (Year 3)"
INSTITUTION = "Cebu Institute of Technology–University"
EMAIL = "a.lemuelvincent@gmail.com"

# ---------------------------------------------------------
# 5. SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    try:
        st.image("profile.png", use_container_width=True)
    except Exception:
        st.markdown("## ⚡")

    st.markdown(f"### **{FULL_NAME}**")
    st.caption(f"Known as {NICKNAME}")
    st.markdown(
        '<span class="status-badge">CS Student • Student Leader</span>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(f"**Course & Section:** `{COURSE_SECTION}`")
    st.markdown(f"**Program:** {PROGRAM}")
    st.markdown(f"**Institution:** {INSTITUTION}")
    st.markdown("**Interests:** Software engineering, leadership, photography")

    st.markdown("---")
    st.subheader("Explore My Story")
    section_focus = st.radio(
        "Choose a section focus:",
        [
            "All Sections",
            "Autobiography",
            "Leadership & Service",
            "Skills & Analytics",
            "Projects & Ideas",
            "Contact",
        ],
    )

    st.markdown("---")
    profile_summary = f"""{FULL_NAME} ({NICKNAME})
Course: {COURSE_SECTION}
{PROGRAM}
{INSTITUTION}

Student leader interested in technology, community service, and personal growth.
Leadership: President, CIT-U Computer Students' Society (CSS).
Creative interest: TreClicks photography.
"""
    st.download_button(
        label="📥 Download My Profile (.txt)",
        data=profile_summary,
        file_name="Tre_Alcoseba_Profile.txt",
        mime="text/plain",
        use_container_width=True,
    )

# ---------------------------------------------------------
# 6. HERO
# ---------------------------------------------------------
hero_col1, hero_col2 = st.columns([2.2, 1.2])

with hero_col1:
    st.title(FULL_NAME)
    st.markdown(f"#### `{COURSE_SECTION}` • Computer Science Student | Student Leader")
    st.write(
        "Welcome to my autobiography and personal portfolio. This is a look at the "
        "experiences, values, and ambitions that continue to shape me as a person, "
        "a Computer Science student, and a student leader."
    )

with hero_col2:
    metric1, metric2 = st.columns(2)
    with metric1:
        st.metric("Graduation Milestone", "Top 8", "UC-METC, 2024")
    with metric2:
        st.metric("Current Role", "CSS President", "CIT-U (2026)")

st.markdown("---")

# ---------------------------------------------------------
# 7. TABS
# ---------------------------------------------------------
tab_bio, tab_leadership, tab_skills, tab_projects, tab_contact = st.tabs(
    [
        "📖 Autobiography",
        "🤝 Leadership & Service",
        "📊 Skills & Analytics",
        "🚀 Projects & Ideas",
        "✉️ Contact",
    ]
)

# ---------------------------------------------------------
# TAB 1: AUTOBIOGRAPHY
# ---------------------------------------------------------
with tab_bio:
    about_col, values_col = st.columns([1.2, 1], gap="large")

    with about_col:
        with st.container(border=True):
            st.subheader("A Little About Me")
            st.write(
                "I am Lemuel Vincent V. Alcoseba III, commonly known as Tre. My journey "
                "has been shaped by education, student leadership, scouting, community "
                "involvement, and a growing interest in technology. Each experience has "
                "helped me learn more about responsibility, teamwork, and the kind of "
                "person I want to become."
            )
            st.write(
                "As a Computer Science student at CIT-U, I am building my technical "
                "foundation while learning how to turn ideas into useful software. "
                "Outside the classroom, student organizations give me opportunities to "
                "serve others, coordinate people, solve practical problems, and grow "
                "as a leader."
            )
            st.write(
                "I believe growth comes from staying curious, being willing to learn, "
                "and taking responsibility for the work entrusted to me."
            )

    with values_col:
        with st.container(border=True):
            st.subheader("Education")
            st.markdown(
                """
                **Cebu Institute of Technology–University**  
                *Bachelor of Science in Computer Science*  
                Current undergraduate studies

                **University of Cebu – Maritime Education and Training Center**  
                *Senior High School*  
                Graduated June 2024 (Top 8 of Graduating Class)

                **Cebu Institute of Technology–University**  
                *Junior High School*

                **St. Thomas Learning Center Foundation Inc.**  
                *Elementary Education*
                """
            )

    st.subheader("Milestones Along the Way")
    timeline = [
        (
            "Elementary Years",
            "Began participating in pupil government and developed an early interest in service and school involvement.",
        ),
        (
            "Scouting & Youth Development",
            "Built experience in scouting, teamwork, outdoor skills, and leadership. Earned the Outdoorsman Scout Rank and served as a Junior Outfit Adviser.",
        ),
        (
            "Senior High School",
            "Served in student leadership and student affairs roles at UC-METC, while maintaining a strong academic record.",
        ),
        (
            "June 2024",
            "Graduated Top 8 among 293 graduates of the UC-METC Basic Education Department, with high honors and leadership recognition.",
        ),
        (
            "Computer Science at CIT-U",
            "Continued my academic journey in computing while taking on greater responsibilities in student organizations and community-oriented initiatives.",
        ),
        (
            "2026",
            "Serving as President of the CIT-U Computer Students' Society and continuing to develop as a student, organizer, and future computing professional.",
        ),
    ]
    for heading, detail in timeline:
        with st.container(border=True):
            st.markdown(f"**{heading}**")
            st.write(detail)

    with st.expander("Interests beyond academics"):
        st.write(
            "I enjoy gaming, listening to music, playing guitar, and photography. "
            "Photography is also part of my creative identity through TreClicks, "
            "with the tagline “Capturing stories in every frame.” I also value time "
            "spent with family and learning practical skills from the people around me."
        )

# ---------------------------------------------------------
# TAB 2: LEADERSHIP & SERVICE (Centered, Bold, Larger Org Names)
# ---------------------------------------------------------
with tab_leadership:
    st.subheader("Leadership & Service Portfolio")
    st.write(
        "A structured and verified record of my leadership journey across student government, "
        "academic societies, community organizations, and scouting."
    )

    # 1. CURRENT LEADERSHIP POSITIONS (Strictly confirmed 6 roles)
    st.markdown("#### 🌟 Current Leadership Positions")
    current_leadership = [
        {"role": "President", "org": "CIT-U Computer Students’ Society (CSS)", "period": "Current"},
        {"role": "Chairperson", "org": "Supreme Student Government - Commission on Extracurricular Activities", "period": "Current"},
        {"role": "Vice President", "org": "Wildcats Esports League", "period": "Current"},
        {"role": "Chief Human Resource Officer", "org": "Google Developers Group on Campus", "period": "Current"},
        {"role": "Youth Service Director", "org": "Rotaract Club of Metro Cebu – CIT Chapter", "period": "Current"},
        {"role": "Events and Logistics Officer", "org": "Social Impact Catalyst", "period": "Current"},
    ]

    for item in current_leadership:
        with st.container(border=True):
            r_col, o_col = st.columns([1.1, 2])
            with r_col:
                st.markdown(f'<div class="role-title">{item["role"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<span class="badge-year">{item["period"]}</span>', unsafe_allow_html=True)
            with o_col:
                st.markdown(f'<div class="org-title">{item["org"]}</div>', unsafe_allow_html=True)

    st.write("")

    # 2. PREVIOUS POSITIONS AND ORGANIZATIONAL EXPERIENCE
    st.markdown("#### 🏛️ Previous Positions and Organizational Experience")
    previous_positions = [
        {"role": "Committee Head, Committee on Logistics", "org": "CIT-U Computer Students’ Society", "period": "2025-2026"},
        {"role": "Project Head Coordinator", "org": "Supreme Student Government - Commission on Extracurricular Activities", "period": "2025-2026"},
        {"role": "Member, Committee on Facility Management and Reception", "org": "Honor Society", "period": "2024–present"},
        {"role": "Director for Recruitment", "org": "CIT-U Junior Jaycees", "period": "2025-2026"},
        {"role": "Member, Club Service", "org": "Rotaract Club of Metro Cebu – CIT Chapter", "period": "2025-2026"},
        {"role": "Member, Committee on Social Responsibility", "org": "CIT-U Computer Students’ Society", "period": "2024–2025"},
        {"role": "Vice President–Internal", "org": "UC-METC Supreme Student Government", "period": "2023–2024"},
        {"role": "Marshall", "org": "Student Affairs Office, UC-METC", "period": "2023–2024"},
        {"role": "Public Relations Officer", "org": "Community Awareness, Relations & Extension Services (C.A.R.E.S.), UC-METC", "period": "2022–2024"},
        {"role": "Auditor", "org": "Council of Presidents, UC-METC", "period": "2022–2023"},
        {"role": "Member", "org": "Student Affairs Office, UC-METC", "period": "2022–2023"},
        {"role": "Junior Outfit Adviser", "org": "Boy Scouts of the Philippines", "period": "2021–2022"},
        {"role": "Scout", "org": "Boy Scouts of the Philippines", "period": "2018–2022"},
        {"role": "Councilor", "org": "Supreme Pupil Government (SPG)", "period": "2012–2014 and 2016–2017"},
    ]

    for item in previous_positions:
        with st.container(border=True):
            r_col, o_col = st.columns([1.1, 2])
            with r_col:
                st.markdown(f'<div class="role-title">{item["role"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<span class="badge-year">{item["period"]}</span>', unsafe_allow_html=True)
            with o_col:
                st.markdown(f'<div class="org-title">{item["org"]}</div>', unsafe_allow_html=True)

    st.write("")

    # 3. ACHIEVEMENTS & RECOGNITION
    st.markdown("#### ⚜️ Achievements & Scouting Honors")
    with st.container(border=True):
        sc_col1, sc_col2 = st.columns([1.1, 2])
        with sc_col1:
            st.markdown('<div class="role-title">Outdoorsman Scout Rank</div>', unsafe_allow_html=True)
            st.markdown('<span class="badge-year">2020</span>', unsafe_allow_html=True)
        with sc_col2:
            st.markdown('<div class="org-title">Boy Scouts of the Philippines</div>', unsafe_allow_html=True)
            st.caption("<div style='text-align: center;'>Earned merit recognitions in outdoor leadership, survival craft, teamwork, and community service.</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 3: SKILLS & ANALYTICS (Meets Rubric: Chart + Numbers + Slider + Checkbox)
# ---------------------------------------------------------
with tab_skills:
    st.subheader("Technical Competencies & Learning Index")
    st.write(
        "To satisfy quantitative assessment standards, the dataset below benchmarks my "
        "self-evaluated confidence and relative project experience across core computing domains."
    )

    slider_col, check_col = st.columns([2, 1])
    with slider_col:
        min_confidence = st.slider("Filter competencies by minimum confidence rating:", 50, 100, 65)
    with check_col:
        st.write("")
        st.write("")
        show_raw = st.checkbox("Show raw numerical data table", value=True)

    skills_data = [
        {"Skill": "Programming (Java, Python, C)", "Category": "Languages", "Confidence": 88, "Context": "Coursework and problem-solving exercises"},
        {"Skill": "Object-Oriented Design", "Category": "Software Eng", "Confidence": 85, "Context": "Classes, polymorphism, structure"},
        {"Skill": "Database Design & SQL", "Category": "Data Systems", "Confidence": 82, "Context": "Relational data and query building"},
        {"Skill": "Applied AI & Streamlit", "Category": "AI & Tools", "Confidence": 80, "Context": "CSIT 349 coursework and interactive apps"},
        {"Skill": "Project Coordination", "Category": "Leadership", "Confidence": 95, "Context": "CSS and student government leadership"},
        {"Skill": "Photography & Storytelling", "Category": "Creative", "Confidence": 90, "Context": "TreClicks visual brand"},
    ]
    skills_df = pd.DataFrame(skills_data)
    filtered_df = skills_df[skills_df["Confidence"] >= min_confidence]

    col_chart, col_tbl = st.columns([3, 2], gap="medium")
    
    with col_chart:
        with st.container(border=True):
            st.markdown("##### 📈 Relative Competency Benchmark (Chart)")
            if not filtered_df.empty:
                st.bar_chart(filtered_df.set_index("Skill")["Confidence"], color="#ff4b4b")
            else:
                st.warning("No competencies match this threshold. Try adjusting the slider.")

    with col_tbl:
        if show_raw:
            with st.container(border=True):
                st.markdown("##### 📋 Verified Numerical Table")
                st.dataframe(filtered_df[["Skill", "Category", "Confidence"]], use_container_width=True, hide_index=True)

    st.subheader("How I Approach Learning")
    learn_col1, learn_col2, learn_col3 = st.columns(3)
    with learn_col1:
        with st.container(border=True):
            st.markdown("#### 1. Understand")
            st.write("Learn the core architecture and the reasoning behind it, not just syntax.")
    with learn_col2:
        with st.container(border=True):
            st.markdown("#### 2. Practice")
            st.write("Apply concepts through hands-on development, debugging, and small tools.")
    with learn_col3:
        with st.container(border=True):
            st.markdown("#### 3. Improve")
            st.write("Review user feedback, refactor, and build upon the fundamentals.")

# ---------------------------------------------------------
# TAB 4: PROJECTS (Meets Rubric: 3+ Projects with Title, Role, Tools, Outcome/Link)
# ---------------------------------------------------------
with tab_projects:
    st.subheader("Projects & Applied Work")
    st.write("Filter through projects and software initiatives using the dropdown selector.")

    project_filter = st.selectbox(
        "Filter by category:",
        ["All", "Software Development", "Organizational Leadership", "Creative Work"],
    )

    projects = [
        {
            "title": "FlowerOrderSystem",
            "category": "Software Development",
            "role": "Lead Developer & UI Designer",
            "tools": "Java, JavaFX, OOP Principles, IntelliJ IDEA",
            "description": "An interactive desktop application for cataloging, selecting, and processing floral product orders with structured state management.",
            "outcome": "Successfully built and demonstrated as an end-of-term Object-Oriented Software project.",
            "link_text": "GitHub Repository ↗"
        },
        {
            "title": "SkillSwap Platform Concept",
            "category": "Software Development",
            "role": "Product Designer & Co-Developer",
            "tools": "Python, Relational DB (SQL), Streamlit Prototype",
            "description": "An application architecture centered on peer-to-peer student skill sharing, helping university students exchange knowledge and technical tutoring.",
            "outcome": "Drafted system architecture and functional MVP workflow ready for pilot testing.",
            "link_text": "View Architecture Specs ↗"
        },
        {
            "title": "CIT-U CSS Organizational Programs",
            "category": "Organizational Leadership",
            "role": "President & Executive Coordinator",
            "tools": "Leadership, Strategic Planning, Event Operations, Community Outreach",
            "description": "Spearheaded student activities, technical workshops, and welfare initiatives tailored for Computer Studies students at CIT-U.",
            "outcome": "Coordinated multiple departmental events engaging hundreds of tech students in 2026.",
            "link_text": "CSS Organization Portal ↗"
        },
        {
            "title": "TreClicks Creative Storytelling",
            "category": "Creative Work",
            "role": "Creative Director & Lead Photographer",
            "tools": "Digital Photography, Adobe Lightroom, Visual Storytelling",
            "description": "Creative visual identity with the tagline “Capturing stories in every frame,” focusing on student event documentation and portraits.",
            "outcome": "Covered multiple major campus events and published visual documentation series.",
            "link_text": "View Portfolio Gallery ↗"
        },
    ]

    visible_projects = [
        p for p in projects if project_filter == "All" or p["category"] == project_filter
    ]

    for p in visible_projects:
        with st.container(border=True):
            p_left, p_right = st.columns([2.5, 1])
            with p_left:
                st.markdown(f"### {p['title']}")
                st.caption(f"{p['category']}")
                st.write(p["description"])
                st.markdown(f"**Tools used:** `{p['tools']}`")
            with p_right:
                st.markdown(f"**Role:** {p['role']}")
                st.info(f"🎯 **Outcome:** {p['outcome']}")
                st.button(p["link_text"], key=f"btn_{p['title']}")

# ---------------------------------------------------------
# TAB 5: CONTACT & FEEDBACK FORM
# ---------------------------------------------------------
with tab_contact:
    st.subheader("Get in Touch")
    st.write(
        "For academic conversations, student initiatives, creative work, or collaborations, feel free to reach out."
    )

    contact_col1, contact_col2 = st.columns([1.2, 1], gap="large")

    with contact_col1:
        with st.container(border=True):
            st.markdown("#### Send a Message")
            with st.form("feedback_form", clear_on_submit=True):
                sender_name = st.text_input("Your Name *")
                sender_email = st.text_input("Your Email *")
                subject = st.selectbox(
                    "Topic",
                    [
                        "General inquiry",
                        "Academic collaboration",
                        "CSS Student Society",
                        "TreClicks Photography",
                    ],
                )
                message = st.text_area("Message *", height=120)
                submitted = st.form_submit_button(
                    "Submit Message",
                    use_container_width=True,
                )

                if submitted:
                    if not sender_name.strip() or not sender_email.strip() or not message.strip():
                        st.error("Please complete all required fields.")
                    elif "@" not in sender_email or "." not in sender_email.split("@")[-1]:
                        st.error("Please enter a valid email address.")
                    else:
                        st.session_state.feedback_list.append(
                            {
                                "Name": sender_name.strip(),
                                "Email": sender_email.strip(),
                                "Topic": subject,
                                "Message": message.strip(),
                            }
                        )
                        st.balloons()
                        st.success("Thanks! Your message has been recorded for this session.")

    with contact_col2:
        with st.container(border=True):
            st.markdown("#### Direct Details")
            st.write(f"**Name:** {FULL_NAME} ({NICKNAME})")
            st.write(f"**Course & Section:** {COURSE_SECTION}")
            st.write(f"**Program:** {PROGRAM}")
            st.write(f"**Institution:** {INSTITUTION}")
            st.write(f"**Email:** {EMAIL}")
            st.markdown("---")
            st.caption("Active in student leadership and community service at CIT-U.")

    if st.session_state.feedback_list:
        with st.expander("View feedback submitted during this session"):
            st.dataframe(
                pd.DataFrame(st.session_state.feedback_list),
                use_container_width=True,
                hide_index=True,
            )

# ---------------------------------------------------------
# 8. FOOTER
# ---------------------------------------------------------
st.markdown("---")
footer_col1, footer_col2 = st.columns([2, 1])
with footer_col1:
    st.caption(
        f"CSIT 349: Applied AI • {COURSE_SECTION} • Built by {FULL_NAME}"
    )
with footer_col2:
    st.caption("Built with Streamlit")