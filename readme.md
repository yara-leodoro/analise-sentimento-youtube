
# 🎯 Análise de Sentimento de Comentários do YouTube

Este projeto realiza **análise de sentimentos** em comentários de vídeos do YouTube utilizando a API oficial da plataforma. Os comentários são processados e classificados em **positivos**, **negativos** ou **neutros**, e os resultados são salvos em um arquivo `.csv`, além de serem exibidos em uma aplicação interativa com **Streamlit**.

---

## 🚀 Funcionalidades

- 🔗 Conexão com a API do YouTube
- 💬 Coleta de comentários de um vídeo específico
- 🧠 Classificação automática do sentimento com `nltk.sentiment`
- 🌍 Tradução dos comentários com `GoogleTranslator` (caso necessário)
- 📊 Exibição dos resultados com gráficos e tabelas em uma aplicação Streamlit
- 🧾 Exportação dos dados para um arquivo `CSV`

---

## 📦 Bibliotecas Utilizadas

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [nltk](https://www.nltk.org/)
- [deep-translator (GoogleTranslator)](https://pypi.org/project/deep-translator/)

---

## 🛠️ Instalação

Clone o repositório e instale as dependências com:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

---
## 🔐 Variáveis de Ambiente (.env)

Para configurar corretamente o projeto, crie um arquivo `.env` na raiz com o seguinte conteúdo:

---

```env
API_KEY=SUA_CHAVE_DE_API_YOUTUBE
VIDEO_ID=ID_DO_VIDEO
OUTPUT_PATH=data/comentarios_analisados.csv
```

## ▶️ Execução

Depois da instalação, execute a aplicação com:

```bash
streamlit run app.py
```


## 📌 Observações

- Você precisa de uma chave de API do YouTube para usar o sistema. Ela pode ser gerada pelo [Google Cloud Console](https://console.cloud.google.com/).
- A análise de sentimento é feita com base no VADER (`nltk.sentiment.vader`) e pode ser adaptada para outros idiomas com auxílio de tradução.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Sinta-se livre para usar, modificar e contribuir.
