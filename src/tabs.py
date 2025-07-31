import pandas as pd
import numpy as np
import streamlit as st

def tabs_creation()
    tabs_list = ['Informacion', 'Glosario Ambiental', 'Pestaña 4']
    tabs_tmp = st.tabs(tabs_list)


with tab1:
    with open('/workspaces/Bootcamp-AnalisisDatosIntermedio/Dashboard/markdowns/pestaña_1.md', 'r', encoding='utf8') as md_1:
        markdown_content = md_1.read()
    st.markdown(markdown_content, unsafe_allow_html=True)

with tab2:
    data_frame_glosary = pd.read_csv("/workspaces/DashboardPortfolio/DataSets/GLOSARIO_AMBIENTAL_20250725.csv")
    seleccion = st.selectbox('Seleccione el termino', list(data_frame_glosary['TERMINO']))
    boton = st.button('Definir')
    if boton:
        filtrado = data_frame_glosary[data_frame_glosary['TERMINO']==seleccion]
        st.markdown(f"### Definción de {filtrado.iat[0, 0]}")
        st.markdown(f'{filtrado.iat[0, 1]}')
        if pd.isna(filtrado.iat[0, 2]) and pd.isna(filtrado.iat[0, 3]):
            st.markdown(f'*No especificado*')
        else:
            st.markdown(f'- *{filtrado.iat[0, 2]} - {filtrado.iat[0, 3]}*')
