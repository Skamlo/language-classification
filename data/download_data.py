import requests
import pandas as pd
from tqdm import tqdm

data = pd.read_csv("./data/sources.csv")
urls = data["txt_link"].to_list()
file_base_names = [language.replace(" ", "_").lower() for language in data["language"]]

for url, file_base_name in tqdm(zip(urls, file_base_names)):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"./data/files/{file_base_name}.txt", 'wb') as f:
            f.write(response.content)
    else:
        raise f"Failed to download {file_base_name}.txt from {url}"
