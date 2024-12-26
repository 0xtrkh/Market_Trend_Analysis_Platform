import streamlit as st
from data import DataProcessor
from websocket import start_streaming
from dotenv import load_dotenv

def main():
    load_dotenv(dotenv_path=".env")
    st.set_page_config(page_title='Market Trend Analysis Platform', layout='wide')
    
    st.title('Plateforme d\'Analyse des Tendances du Marché')
    
    # Sidebar configuration with ETHUSDT as default
    symbol = "ethusdt"
    interval = st.sidebar.selectbox("Interval:", ['1m', '5m', '15m', '30m', '1h', '1d'])
    alert_threshold = st.sidebar.number_input("Alerte Seuil (%):", min_value=0.01, value=1.0)
    
    st.sidebar.header("Données collectées")
    chart_placeholder = st.empty()
    alert_placeholder = st.sidebar.empty()
    
    start_streaming(symbol, interval, alert_threshold, chart_placeholder, alert_placeholder)

if __name__ == "__main__":
    main()