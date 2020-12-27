#!pip install git+https://github.com/abenassi/Google-Search-API
from googlesearch import search 
import os
import pandas as pd
def get_link(news_id):
    url = ""
    if not news_id.isdigit():
        print("")
        pass
    else:
        try:
            query = "soha " + str(news_id)
            url = search(query, num=1).__next__()
        except:
            url = ""
    print(f"{news_id} ==>link: {url}")
    return url


for file in os.listdir("/content/news"):
    data = pd.read_csv(f"/content/news/{file}")
    all_item = list(set(data["itemId"]))
    links = pd.DataFrame({"item_id": all_item})
    links['link'] = links['item_id'].map(lambda f: get_link(f))

    links.to_csv(f"/content/links/{file}_links.csv")
