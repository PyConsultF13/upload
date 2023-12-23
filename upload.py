import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module


def generate_excel_download_link(df):
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

st.set_page_config(
page_title='Importação Arquivos',
page_icon='$',
layout='wide',
initial_sidebar_state='collapsed'
)

st.title('Modulo Importação Arquivos 🌐')
st.subheader('📋 Lista Arquivos RadCom On-line')
st.write('🔄 Movimentação ➡ base_PROD | base_GDM | base_PDV | base_MOV | base_MOV_AA ')
st.write('🔄 Produtividade ➡ base_INE | base_ID | base_IAV | base_TEND ')

uploaded_files = st.file_uploader(':warning: IMPORTAR SOMENTE ARQUIVO COM EXTENSÃO .XLSX', accept_multiple_files=True)
for uploaded_file in uploaded_files:    
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.markdown('---')
    st.success('Arquivos Importado com Sucesso!')
    with st.expander('👁️‍🗨️Clique aqui para visualizar os dados do arquivo:'):
        df = df
        df    
