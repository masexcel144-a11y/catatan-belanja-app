import streamlit as st

st.title("📝 Catatan Belanja dengan Total Harga")

# Gunakan session_state agar data tersimpan selama sesi aktif
if "belanja" not in st.session_state:
    st.session_state.belanja = []  # Menyimpan list belanja

# Form untuk menambah barang
with st.form("tambah_barang", clear_on_submit=True):
    nama = st.text_input("Nama Barang")
    jumlah = st.number_input("Jumlah", min_value=1, step=1)
    harga_satuan = st.number_input("Harga per Item (Rp)", min_value=0, step=100)
    submitted = st.form_submit_button("Tambah Barang")

    if submitted and nama and harga_satuan > 0:
        total_item = jumlah * harga_satuan
        st.session_state.belanja.append({
            "nama": nama,
            "jumlah": jumlah,
            "harga_satuan": harga_satuan,
            "total_item": total_item
        })

# Tombol hapus semua
if st.button("🧹 Hapus Semua"):
    st.session_state.belanja.clear()

# Tampilkan tabel belanja
st.subheader("🧾 Daftar Belanja")
if st.session_state.belanja:
    st.table(st.session_state.belanja)

    # Hitung total semua belanja
    total_semua = sum(item["total_item"] for item in st.session_state.belanja)
    st.markdown(f"### 💰 **Total Belanja: Rp {total_semua:,.0f}**")
else:
    st.info("Belum ada barang yang ditambahkan.")
