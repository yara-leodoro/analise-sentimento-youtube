import os
from dotenv import load_dotenv
import pandas as pd
import streamlit as st

load_dotenv()
path = os.getenv("OUTPUT_PATH") + "/"
df = pd.read_csv(path + "comentarios_analisados.csv")

st.title("📊 Análise de Sentimentos - Comentários YouTube")
st.markdown(f"**🎥 Vídeo:** {df['Titulo do Vídeo'][0]}  \n**📡 Canal:** {df['Canal'][0]}")


sentimentos_validos = ["Positivo", "Negativo", "Neutro"]
df = df[df["Sentimento"].isin(sentimentos_validos)]

sentimentos = st.multiselect(
    "Filtrar por sentimento:",
    options=sentimentos_validos,
    default=sentimentos_validos
)

score_min = st.slider("Score mínimo:", min_value=0.0, max_value=1.0, value=0.0, step=0.05)

df_filtrado = df[(df["Sentimento"].isin(sentimentos)) & (df["Score"] >= score_min)]

ordenar = st.checkbox("🔼 Ordenar por score (decrescente)", value=True)
if ordenar:
    df_filtrado = df_filtrado.sort_values(by="Score", ascending=False)

for i, row in df_filtrado.iterrows():
    st.markdown(f"### 🗨️ {row['Comentário (pt)']}")
    st.markdown(f"**📊 Sentimento:** `{row['Sentimento']}` — Score: `{row['Score']:.4f}`")
    st.markdown("---")
