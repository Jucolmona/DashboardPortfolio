import pandas as pd
import numpy as np
import streamlit as st

def header_creations():
    st.set_page_config(layout='centered', page_title='Talento Tech', page_icon=':smile:')

    t1, t2 = st.columns([0.3, 0.7])
    t1.image('/workspaces/DashboardPortfolio/images/talento-tech.jpg', width=150)
    t2.image('/workspaces/DashboardPortfolio/images/logo-udea.png')

    st.header('Talento Tech - Dashboard')
    st.subheader('**Tel:** 3015989619 | **email:** camilo.mona.lujan@gmail.com')

def tabs_creation()
    tabs_list = ['Informacion', 'Glosario Ambiental', 'Pestaña 4']
    tabs_tmp = st.tabs(tabs_list)
    return tabs_tmp

def tabs_definitions():
    tabs = tabs_creation()

    with tabs[0]:
        with open('/workspaces/Bootcamp-AnalisisDatosIntermedio/Dashboard/markdowns/pestaña_1.md', 'r', encoding='utf8') as md_1:
            markdown_content = md_1.read()
        st.markdown(markdown_content, unsafe_allow_html=True)

    with tabs[1]:
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
