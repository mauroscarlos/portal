import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar a tela toda
st.set_page_config(page_title="MSCGYM - Portal de Sistemas", layout="wide", initial_sidebar_state="expanded")

# --- CSS PARA MENU ESTILIZADO E TELA CHEIA ---
st.markdown("""
<style>
    /* Remove as bolinhas do menu */
    div[role="radiogroup"] span[data-baseweb="radio"] { display: none !important; }
    
    /* Botões do menu lateral */
    div[role="radiogroup"] label {
        background-color: #f1f3f5 !important;
        border-radius: 10px !important;
        padding: 15px 20px !important;
        margin-bottom: 10px !important;
        border: 1px solid #d1d3d4 !important;
        display: block !important;
        width: 100% !important;
        cursor: pointer !important;
    }

    /* Item selecionado */
    div[role="radiogroup"] input:checked + label {
        background-color: #007BFF !important;
        color: white !important;
        font-weight: bold !important;
    }

    /* Ajuste para o IFrame ocupar a altura máxima */
    iframe {
        width: 100%;
        height: 90vh;
        border: none;
    }
    
    /* Remove padding excessivo do Streamlit */
    .main .block-container { padding: 0rem; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🚀 MSCGYM HUB")

# --- DEFINA OS LINKS DOS SEUS 3 APPS AQUI ---
# Importante: adicione '?embed=true' ao final de cada URL para esconder o menu original deles
apps = {
    "⌚ Controle de Ponto": "https://mscgym-ponto.streamlit.app/?embed=true",
    "📊 Gestão Financeira": "https://mscgym-financeiro.streamlit.app/?embed=true",
    "👤 Cadastro de Alunos": "https://mscgym-alunos.streamlit.app/?embed=true"
}

escolha = st.sidebar.radio("Navegação entre Sistemas", list(apps.keys()))

st.sidebar.divider()
st.sidebar.caption("Logado como Administrador")

# --- EXIBIÇÃO DO APP SELECIONADO ---
url_selecionada = apps[escolha]
components.iframe(url_selecionada, scrolling=True)
