import streamlit as st
import pandas as pd

st.title("Aplikasi Filter Komentar Berdasarkan Sentimen")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("processed_jumbo.csv")
    return df

data = load_data()

# Cek keberadaan kolom label
if 'label' not in data.columns:
    st.error("Dataset harus memiliki kolom 'label'")
else:
    # Deteksi kolom komentar secara otomatis (selain 'label')
    komentar_cols = [col for col in data.columns if col.lower() != 'label']
    
    if not komentar_cols:
        st.error("Tidak ditemukan kolom komentar (selain 'label')")
    else:
        komentar_col = komentar_cols[0]  # Ambil kolom komentar pertama

        # Tampilkan preview
        st.subheader("Data Komentar (preview):")
        st.write(data[[komentar_col, 'label']].head())

        # Pilihan filter
        pilihan = st.radio("Pilih kategori sentimen:", ["Semua", "Positif", "Netral", "Negatif"])

        if pilihan == "Semua":
            hasil = data
        else:
            hasil = data[data['label'].str.lower() == pilihan.lower()]

        # Tampilkan hasil
        st.subheader(f"Hasil Filter: {pilihan}")
        st.write(hasil[[komentar_col, 'label']])
