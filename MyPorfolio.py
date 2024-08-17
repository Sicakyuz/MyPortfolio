import streamlit as st
import streamlit_option_menu
from cover_page import cover_page
from publications import publications_page
from contact import contact_page
import streamlit.components.v1 as components
from Projects.projects import projects_page

st.set_page_config(page_title="My Portfolio", page_icon=":chart_with_upwards_trend:")

# Define pages


    # Sidebar configuration
with st.sidebar:
    st.image("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/PHOTO-2024-05-30-16-58-28.jpg", width=300)
    st.write("# ÇİĞDEM SICAKYÜZ")

    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin: 20px 0;">
            <a href="mailto:cigdem.sicakyuzl@gmail.com" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/000000/email.png" alt="Email" width="30" height="30">
            </a>
            <a href="https://github.com/Sicakyuz/" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" alt="GitHub" width="30" height="30">
            </a>
            <a href="https://www.kaggle.com/cigdems" target="_blank">
                <img src="https://img.icons8.com/windows/48/1a73e8/kaggle.png" alt="Kaggle" width="30" height="30">
            </a>
            <a href="https://www.linkedin.com/in/csicakyuz/" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/40/0a66c2/linkedin.png" alt="LinkedIn" width="30" height="30">
            </a>
            <a href="https://www.researchgate.net/profile/Cigdem-Sicakyuez" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" alt="ResearchGate" width="30" height="30">
            </a>
            <a href="https://https://scholar.google.com/citations?user=bnp2fx4AAAAJ&hl=tr" target="_blank">
                <img src="https://static-00.iconduck.com/assets.00/google-scholar-icon-512x512-8ggb625i.png" alt="Google Scholar" width="30" height="30">
            </a>
        </div>
        """, unsafe_allow_html=True)
    st.sidebar.title("")

    st.sidebar.title("EDUCATION")

    # Expander oluşturma
    with st.sidebar.expander("EDUCATION"):
        phd_text = "**Ph.D. in Industrial Engineering (2019)**\nÇukurova University, Adana, Turkey\n"
        msc_text = "**M.Sc. in Industrial Engineering (2009)**\nUniversität Bremen, Bremen, Germany\n"
        bs_text = "**B.S. in Industrial Engineering (2001)**\nOsmangazi University, Eskişehir, Turkey\n"

        # İkonlar ve metinleri birleştirme
        phd_content = f"<i class='fas fa-graduation-cap'></i> {phd_text}"
        msc_content = f"<i class='fas fa-graduation-cap'></i> {msc_text}"
        bs_content = f"<i class='fas fa-graduation-cap'></i> {bs_text}"

        # Yan taraftaki çubukta madde madde listeleme
        st.markdown(f"- {phd_content}", unsafe_allow_html=True)
        st.markdown(f"- {msc_content}", unsafe_allow_html=True)
        st.markdown(f"- {bs_content}", unsafe_allow_html=True)

    st.sidebar.title("EXPERIENCE")
    with st.sidebar.expander("EXPERIENCE"):
        assistant_prof_text = "**Assistant Professor (2020-2023)**\nAnkara Science University, Ankara, Turkey\nAdministrative Contribution to University"
        quality_coord_text = "**Quality Coordinator (2021-2022)**\nAnkara Science University, Ankara, Turkey"
        tech_dir_text = "**Director of Technology Transfer Office (2021-2022)**\nAnkara Science University, Ankara, Turkey"
        consultant_text = "**Consultant (2019-2020)**\nMır-Serhat Mining Industry, Malatya, Turkey"
        project_asst_text = "**Project Assistant (1998-2000)**\nLight Rail Systems Project in Eskişehir Metropolitan Municipality"

        # İkonlar ve metinleri birleştirme
        assistant_prof_content = f"<i class='fas fa-briefcase'></i> {assistant_prof_text}"
        quality_coord_content = f"<i class='fas fa-briefcase'></i> {quality_coord_text}"
        tech_dir_content = f"<i class='fas fa-briefcase'></i> {tech_dir_text}"
        consultant_content = f"<i class='fas fa-briefcase'></i> {consultant_text}"
        project_asst_content = f"<i class='fas fa-briefcase'></i> {project_asst_text}"

        # Yan taraftaki çubukta madde madde listeleme
        st.markdown(f"- {assistant_prof_content}", unsafe_allow_html=True)
        st.markdown(f"- {quality_coord_content}", unsafe_allow_html=True)
        st.markdown(f"- {tech_dir_content}", unsafe_allow_html=True)
        st.markdown(f"- {consultant_content}", unsafe_allow_html=True)
        st.markdown(f"- {project_asst_content}", unsafe_allow_html=True)

    # Expander genişliği kadar bir alan ayır
    #st.markdown("---")

    # Düğmeyi oluştur
    st.sidebar.title("")
    st.sidebar.title("LANGUAGE SKILLS")

    # Dil yetenekleri ve CEFR seviyeleri
    language_skills = {
        "English": "B2-C1",
        "German": "B2-C1"
    }

    # CEFR seviyelerine göre dil yeteneklerini gösterme
    cefr_levels = {
        "A1": "Beginner",
        "A2": "Elementary",
        "B1": "Intermediate",
        "B2": "Upper Intermediate",
        "C1": "Advanced",
        "C2": "Proficient"
    }

    for language, cefr_level in language_skills.items():
        st.sidebar.write(f"**{language}:**")
        progress_map = {
            "A1": 10,
            "A2": 30,
            "B1": 50,
            "B2": 70,
            "C1": 90,
            "C2": 100
        }


        if cefr_level == "B2-C1":
            progress_percentage = (progress_map["B2"] + progress_map["C1"]) / 2
            cefr_label = "B2-C1"
        else:
            progress_percentage = progress_map[cefr_level]
            cefr_label = cefr_level
        st.sidebar.progress(progress_percentage / 100)

        # Seviye açıklamasını göster
        st.sidebar.write(f"Level: {cefr_label} ({int(progress_percentage)}%)")

page = streamlit_option_menu.option_menu(
            "Navigation",
            ["Cover","Projects", "Publications", "Contact"],
            icons=["house", "book", "code", "envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )

        # Render the selected page

if page == "Cover":
    cover_page()
elif page == "Publications":
    publications_page()
elif page == "Projects":
    projects_page()
elif page == "Contact":
    contact_page()
