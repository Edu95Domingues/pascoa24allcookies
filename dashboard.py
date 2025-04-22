import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title("🍬 Dashboard - Campanha de Páscoa 2024")
st.markdown("""
**Período da campanha:** 14 a 25 de março de 2024  
**Objetivo:** Engajamento com foco em conversas no WhatsApp e visualizações de vídeo  
**Investimento total:** R$ 128,12  
""")

# Dados da campanha
data = {
    'Conjunto': ['MIX DE PÚBLICOS', 'ENG WHATS', 'ENG VIDEO VIEW'],
    'Impressões': [4750, 7043, 14417],
    'Alcance': [2966, 3032, 9996],
    'Cliques no link': [23, 39, 8],
    'Cliques (todos)': [107, 172, 46],
    'Conversas iniciadas': [14, 12, 0],
    'Investimento (R$)': [39.24, 57.25, 31.63],
    'Custo por conversa (R$)': [2.80, 4.77, 0],
    'ThruPlays': [0, 0, 4255],
    'Custo por ThruPlay (R$)': [0, 0, 0.01],
    'Criativo de destaque': [
        'Reels ovo de cookie c/ Nutella',
        'Reels cookie c/ Nutella + Arte estática cookie tradicional',
        'Reels de 3 segundos'
    ]
}
df = pd.DataFrame(data)

# Exibir tabela
st.subheader("📊 Tabela Geral da Campanha")
st.dataframe(df.style.background_gradient(cmap='Greens'))

# Gráfico: Conversas por conjunto
st.subheader("🙌 Conversas Iniciadas por Conjunto")
fig1 = px.bar(df, x='Conjunto', y='Conversas iniciadas', color='Conjunto', text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico: Custo por conversa
st.subheader("💲 Custo por Conversa")
fig2 = px.bar(df[df['Conversas iniciadas'] > 0], x='Conjunto', y='Custo por conversa (R$)', color='Conjunto', text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

# Gráfico: Impressões e Alcance
st.subheader("📰 Impressões e Alcance")
df_long = df.melt(id_vars='Conjunto', value_vars=['Impressões', 'Alcance'], var_name='Métrica', value_name='Valor')
fig3 = px.bar(df_long, x='Conjunto', y='Valor', color='Métrica', barmode='group', text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

# Gráfico: ThruPlays
st.subheader("▶️ ThruPlays e Custo")
df_thru = df[df['ThruPlays'] > 0]
fig4 = px.bar(df_thru, x='Conjunto', y='ThruPlays', color='Conjunto', text_auto=True)
st.plotly_chart(fig4, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("Criado com 💚 por [Seu Nome ou Empresa]")
