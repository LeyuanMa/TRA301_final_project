import pandas as pd
import re

def remove_repeated_tokens(text):
    if not isinstance(text, str):
        return text
    
    # Remove space/comma/hyphen-separated word repetition (3+)
    text = re.sub(r'\b(\w+)(?:[\s,\-]+\1\b){3,}', r'\1', text, flags=re.IGNORECASE)

    # Remove slash-separated repetition (e.g., it/it/it///)
    text = re.sub(r'\b(\w+)(?:/+\1\b){3,}', r'\1', text, flags=re.IGNORECASE)

    # Remove repeated tokens like "a) a) a)" or "item: item: item:"
    text = re.sub(r'\b(\w+[^\w\s])(?:\s*\1){3,}', r'\1', text, flags=re.IGNORECASE)

    # Remove excessive repeated punctuation
    text = re.sub(r'([.,!?/"*#-^•♪¶])(?:\s*\1){10,}', r'\1', text)

    # Remove overly long sequences of a single word or punctuation (e.g., "no no no no no")
    text = re.sub(r'\b(\w+)(?:[\s,.\-\\/]+\1\b){3,}', r'\1', text, flags=re.IGNORECASE)

    # Remove consecutive single characters (10+)
    text = re.sub(r'\b\w*(\w)\1{10,}\w*\b', '', text)

    # Remove hashtags
    text = re.sub(r'(#[\w\d]+)(?:\s+\1){3,}', r'\1', text, flags=re.IGNORECASE)

    # Remove hashtags seperated by commas
    text = re.sub(r'(?i)(#\w+)(\s*,\s*\1){3,}', r'\1', text)

    # Remove repeated phrase-like patterns (e.g., "I'm... I'm... I'm...")
    text = re.sub(r'\b(\w+[\']?\w*\.*)(?:\s*\1){3,}', r'\1', text, flags=re.IGNORECASE)

    # Remove repeated two-word phrases
    text = re.sub(r'\b(\w+\s+\w+)(?:[\s,]*\1\b){2,}', r'\1', text, flags=re.IGNORECASE)

    # Remove repeated two-word phrases containing apostrophes
    text = re.sub(r"\b(\w+'?\w*\s+\w+'?\w*)(?:[\s,]*\1\b){2,}", r'\1', text, flags=re.IGNORECASE)

    return text.strip()

def clean_file(language):
    file_path = f"{language}_processed.csv"
    df = pd.read_csv(file_path)

    df["Cleaned_Literal_Translation"] = df["Literal_Translation"].apply(remove_repeated_tokens)
    df["Cleaned_Fluent_Translation"] = df["Fluent_Translation"].apply(remove_repeated_tokens)

    output_path = f"{language}_cleaned.csv"
    df.to_csv(output_path, index=False)

languages = ["french", "german", "italian", "spanish", "arabic"]
for lang in languages:
    clean_file(lang)