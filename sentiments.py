import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from deep_translator import GoogleTranslator

analyzer = SentimentIntensityAnalyzer()

emoji_sentimentos = {
    "😂": "Positivo",
    "🤣": "Positivo",
    "😊": "Positivo",
    "😍": "Positivo",
    "❤️": "Positivo",
    "👍": "Positivo",
    "😎": "Positivo",
    "💔": "Negativo",
    "😢": "Negativo",
    "😭": "Negativo",
    "😡": "Negativo",
    "👎": "Negativo",
    "😐": "Neutro",
    "😶": "Neutro",
    "🤔": "Neutro",
}

def classificar_sentimento_emoji(comments):
    for char in comments:
        if char in emoji_sentimentos:
            return emoji_sentimentos[char]
    return None

def classificar_sentimento(comments):
    resultados = []

    for c in comments:
        try:
            if not c or not isinstance(c, str) or c.strip() == "" or c.strip().lower() == "nan":
                continue
            sentimentos_emoji = classificar_sentimento_emoji(c)

            traducao = GoogleTranslator(source='pt', target='en').translate(c)
            score_dict = analyzer.polarity_scores(traducao)
            score = score_dict['compound']

            if score >= 0.05:
                sentimento = 'Positivo'
            elif score <= -0.05:
                sentimento = 'Negativo'
            else:
                if sentimentos_emoji:
                    sentimento = max(set(sentimentos_emoji), key=sentimentos_emoji.count)
                else:
                    sentimento = 'Neutro'

        except Exception as e:
            traducao = "Erro na tradução"
            sentimento = "Erro"
            score = 0.0
            print(f"Erro ao traduzir/analisar: {str(c)[:40]}... -> {e}")

        resultados.append({
            'Comentário (pt)': c,
            'Sentimento': sentimento,
            'Score': score
        })

    return resultados