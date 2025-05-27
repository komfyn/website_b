import streamlit as st

st.title("KABOOOOOOOMMM")
st.write("Mengecek nilai genap/ganjil")
num = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (num % 2) == 0:
   st.write(f"{num} adalah bilangan genap")
else:
   st.write(f"{num} adalah bilangan ganjil")
