import streamlit as st
import pandas as pd

# Judul Aplikasi
st.title("Aplikasi Filter Komentar Berdasarkan Sentimen")

# Memuat dataset
@st.cache_data
def load_data():
    df = pd.read_csv("processed_jumbo.csv")
    return df

data = load_data()

# Tampilkan 5 data pertama untuk konfirmasi
st.subheader("Data Komentar (preview):")
st.write(data.head())

# Pastikan kolom sentimen dan komentar tersedia
if 'sentimen' not in data.columns or 'komentar' not in data.columns:
    st.error("Dataset harus memiliki kolom 'komentar' dan 'sentimen'")
else:
    # Pilihan filter sentimen
    pilihan = st.radio("Pilih kategori sentimen untuk difilter:", ["Semua", "Positif", "Netral", "Negatif"])

    # Filter berdasarkan pilihan
    if pilihan == "Semua":
        hasil = data
    else:
        hasil = data[data['sentimen'].str.lower() == pilihan.lower()]

    # Tampilkan hasil
    st.subheader(f"Hasil Filter: {pilihan}")
    st.write(hasil[['komentar', 'sentimen']])
