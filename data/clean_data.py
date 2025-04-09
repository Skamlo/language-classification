import os
import re

def clean_text(text):
    """Cleans text by removing unnecessary spaces and ensuring max two consecutive new lines."""
    text = text.replace('\r', '')
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

for file in os.listdir("./data/files_without_metainformation"):
    with open(f"./data/files_without_metainformation/{file}", "r", encoding="utf-8") as f:
        text = f.read()

    text = clean_text(text)

    with open(f"./data/files_clean/{file}", "w", encoding="utf-8") as f:
        f.write(text)
