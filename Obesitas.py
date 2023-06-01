import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Obesitas.sav','rb'))

st.title('Prediksi Terkena Penyakit Obesitas')
col = st.columns

with col:
   ID = st.number_input('Nomor ID')
   Age	= st.number_input('Umur ')
   Gender = st.number_input('Jenis Kelamin Pasien')
   Height = st.number_input('Tinggi badan pasien')
   Weight = st.number_input('Berat badan pasien')
   BMI = st.number_input('Masa tumbuh individu')
   


predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[ID, Age,Gender, Height, Weight, BMI]])

    if(predik[0] == 1):
        predik = 'Kemungkinan Pasien yang terkena Penyakit Obesitas'
    else:
        predik = 'Kemungkinan Pasien yang tidak terkena Penyakit Obesitas'
st.success(predik)