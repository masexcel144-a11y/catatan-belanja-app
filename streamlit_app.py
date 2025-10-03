import streamlit as st

st.title("📝 Catatan Belanja")

# Gunakan session_state agar data tetap tersimpan selama sesi aktif
if "belanja" not in st.session_state:
    st.session_state.belanja = []

# Form input
with st.form("tambah_barang", clear_on_submit=True):
    nama = st.text_input("Nama Barang")
    jumlah = st.text_input("Jumlah")
    submitted = st.form_submit_button("Tambah")
    if submitted and nama and jumlah:
        st.session_state.belanja.append(f"{nama} - {jumlah}")

# Tombol hapus semua
if st.button("Hapus Semua"):
    st.session_state.belanja.clear()

# Tampilkan riwayat
st.subheader("🧾 Riwayat Belanja")
if st.session_state.belanja:
    for item in st.session_state.belanja:
        st.write("- ", item)
else:
    st.write("Belum ada catatan belanja.")
