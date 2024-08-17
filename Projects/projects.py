import streamlit as st
from PIL import Image
import base64
from Projects.project_1 import project_1_page
from Projects.project_2 import project_2_page
from Projects.project_3 import project_3_page
from Projects.project_4 import project_4_page
from Projects.project_5 import project_5_page
from Projects.project_6 import project_6_page
from Projects.project_7 import project_7_page
from Projects.project_8 import project_8_page
from Projects.project_9 import project_9_page


def projects_page(project_page=None):
    # Proje verileri
    projects = [
        {
            "name": "Project 1",
            "title": "**Breast Cancer Prediction**",
            "description": "Clustering and Analysis for Breast Cancer Dataset",
            "image_path": "img_1.png",  # Dosya yolunu düzeltin
            "detail_function": project_1_page  # Detay fonksiyonu
        },
        {
            "name": "Project 2",
            "title": "**Prediction of Diabetes Risk**",
            "description": "Predcition Diabet Risk with Random Forest Algorithm",
            "image_path": "diabet.png",  # Dosya yolunu düzeltin
            "detail_function": project_2_page  # Henüz tanımlanmadı
        },
        {
            "name": "Project 3",
            "title": "E-Commerce Review Analysis",
            "description": "Sentiment Analysis using Machine Learning Models",
            "image_path": "reviews.jpeg",  # Dosya yolunu düzeltin
            "detail_function": project_3_page  # Detay fonksiyonu
        },
        {
            "name": "Project 4",
            "title": "Customer Segmentation and CLV",
            "description": "Customer Segmentation Analysis and Prediction of Customer Life time Value",
            "image_path": "img_2.png",  # Dosya yolunu düzeltin
            "detail_function": project_4_page  # Detay fonksiyonu
        },
        {
            "name": "Project 5",
            "title": "Customer Churn Prediction",
            "description": "Customer Churn Prediction",
            "image_path": "img_3.png",  # Dosya yolunu düzeltin
            "detail_function": project_5_page  # Detay fonksiyonu
        },
        {
            "name": "Project 6",
            "title": "Göğüs Kanseri Teşhisi için Kümeleme Projesi",
            "description": "Kümeleme Projesi",
            "image_path": "img_1.png",  # Dosya yolunu düzeltin
            "detail_function": project_6_page  # Detay fonksiyonu
        },
        {
            "name": "Project 7",
            "title": "Göğüs Kanseri Teşhisi için Kümeleme Projesi",
            "description": "Kümeleme Projesi",
            "image_path": "img_1.png",  # Dosya yolunu düzeltin
            "detail_function": project_7_page  # Detay fonksiyonu
        },
        {
            "name": "Project 8",
            "title": "Göğüs Kanseri Teşhisi için Kümeleme Projesi",
            "description": "Kümeleme Projesi",
            "image_path": "img_1.png",  # Dosya yolunu düzeltin
            "detail_function": project_8_page  # Detay fonksiyonu
        },
        {
            "name": "Project 9",
            "title": "Göğüs Kanseri Teşhisi için Kümeleme Projesi",
            "description": "Kümeleme Projesi",
            "image_path": "img_1.png",  # Dosya yolunu düzeltin
            "detail_function": project_9_page  # Detay fonksiyonu
        },
        # Diğer projeler
    ]

    # CSS ile tasarımı düzenle
    st.markdown(
        """
        <style>
        .project-card {
            display: flex;
            align-items: flex-start;
            background-color: #f5f5f5;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
        }
        .project-image {
            border-radius: 10px;
            margin-right: 20px;
            flex-shrink: 0;  /* Resimlerin boyutunu kartın içinde sabit tutar */
            width: 200px;    /* Resim genişliği */
            height: 200px;   /* Resim yüksekliği */
        }
        .project-info {
        color: black;  /* Yazı rengi */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Başlık
    st.title("Projects")

    # Projeleri listele
    for project in projects:
        # Proje kartı
        st.markdown(
            f"""
                    <div class="project-card">
                        <img src="data:image/png;base64,{get_base64_encoded_image(f"Projects/Images/{project.get('image_path', '')}")}" class="project-image">
                        <div>
                            <h3>{project.get("name", "")}</h3>
                            <p>{project.get("description", "")}</p>
                        </div>
                    </div>
                    """,
            unsafe_allow_html=True
        )

        # Detayları gösteren expander
        with st.expander(f"{project.get('name', '')} Details", expanded=False):
            if project["detail_function"]:
                project["detail_function"]()

    st.write("")
    st.markdown('<div style="background-color: #f0f0f0; padding: 10px; border-radius: 10px;">'
                '<h5 style="color: #333333;">Visit my Github repos for all projects.</h5>'
                '</div>', unsafe_allow_html=True)
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()



