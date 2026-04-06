import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:#FF69B4;'>Hello.. Welcome to my first Dashboard 💖</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color:#FF69B4;'>This is about me</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#FF69B4;'>Aku mahasiswa Informatika semester 2 yang memiliki minat dalam mempelajari teknologi dan juga bahasa ✨</p>",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("aku.jpg.jpeg", width=200)

with col2:
    st.image("poto.jpg.jpg", width=200)

with col3:
    st.image("aku2.jpg.jpg", width=200)

st.markdown(
    """
    <h3 style='color:#FF69B4;'>About Me 💖</h3>
    <p style='color:#FF69B4;'>
    👩 Nama lengkap aku, Cindy Amelia <br>
    📍 Aku lahir di Cirebon, 11 Februari 2006 <br>
    🎂 Umurku 19 tahun <br>
    🎨 Hobiku belajar bahasa, eksplorasi teknologi, dan scroll tiktok hehe..
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#FF69B4;'>Di semester dua ini, aku belajar banyak hal tentang dunia teknologi, ada dua bahasa pemograman yang telah aku pelajari yaitu c++ dan juga python. Selain belajar tentang dunia per codingan, aku juga senang belajar bahasa loo... aku suka belajar bahasa Arab!. Nihh aku kasih buktinya..</p>",
    unsafe_allow_html=True
)
col1, col2, = st.columns(2)

with col1:
    st.image("aku3.jpg", width=300)

with col2:
    st.image("aku4.jpg", width=300)

st.markdown(
    "<p style='color:#FF69B4;'>Untuk saat ini, aku sedang fokus untuk membangun personal branding ku dan juga membangun portofolio ku, yaa walaupun masih kecil-kecilan. Aku rajin ikut kursus online, bangun relasi dengan mahasiswa lain dan ikut kegiatan eksternal di luar kampus. </p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color:#FF69B4;'>Harapan terbesarku ke depannya tidak hanya ingin menjadi ahli di bidang IT, tapi juga menjadi pribadi yang bisa memberikan manfaat nyata melalui ilmu yang telah aku pelajari😊. Oke cukup sekian project kecil-kecilanku ini yaa.. semoga kedepannya aku bisa bangun project yang lebih besar dan lebih bagus lagi. Sebelum ituu yuk saling konek LinkedIn🤩 </p>",
    unsafe_allow_html=True
)