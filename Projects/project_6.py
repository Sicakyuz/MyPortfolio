import streamlit as st
from PIL import Image

def project_6_page():
    st.title("Göğüs Kanseri Teşhisi için Kümeleme Projesi")

    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/img_1.png")
    st.image(image, caption='', use_column_width=True)

    st.markdown("Bu proje, göğüs kanseri teşhisinde kullanılan kümeleme algoritmalarını uygulamayı amaçlamaktadır.")

    st.header("Proje Amacı")
    st.write("""
    Bu proje, göğüs kanseri teşhisi için kullanılan veri setini analiz etmek ve farklı kümeleme 
    algoritmaları kullanarak verileri kümelere ayırmayı hedeflemektedir. Ayrıca, kümeleme sonuçlarını 
    değerlendirmek ve hangi algoritmanın daha iyi performans gösterdiğini belirlemek amacıyla 
    çeşitli metrikler kullanılmaktadır.
    """)

    st.header("Kullanılan Algoritmalar")
    st.write("""
    Projede kullanılan temel kümeleme algoritmaları şunlardır:
    - KMeans: Verileri belirli sayıda kümeye bölen geleneksel bir kümeleme algoritması.
    - DBSCAN: Yoğunluk tabanlı bir kümeleme algoritması.
    - Agglomerative Clustering: Hiyerarşik bir kümeleme algoritması.
    """)

    st.header("Proje Sonuçları")
    st.write("""
    Projede elde edilen sonuçlar şunlardır:
    - KMeans, verileri belirli özelliklere göre iki ana kümeye ayırdı ve iyi bir performans sergiledi.
    - DBSCAN, verileri yoğunluk tabanlı olarak kümelere ayırdı ve bazı verileri gürültü olarak tanımladı.
    - Agglomerative Clustering, hiyerarşik bir yapı oluşturarak verileri kümelere ayırdı.

    Bu sonuçlar, göğüs kanseri teşhisi için kümeleme algoritmalarının etkin bir şekilde kullanılabileceğini 
    göstermektedir.
    """)

    st.header("Proje Detayları")
    st.write("""
    Projede kullanılan veri seti, göğüs kanseri teşhisi için Wisconsin Üniversitesi Hastanesi'nden toplanmıştır. 
    Veri seti, kanser hücrelerinin özelliklerini içermektedir ve makine öğrenimi algoritmalarının eğitilmesi ve 
    değerlendirilmesi için kullanılmaktadır.
    """)

    st.header("Sonuç")
    st.write("""
    Bu proje, göğüs kanseri teşhisi için kümeleme algoritmalarının potansiyelini göstermektedir. 
    Kümeleme algoritmaları, büyük veri setlerini analiz etmek ve kanser teşhisi için değerli 
    bilgiler sağlamak için kullanılabilir.
    """)
