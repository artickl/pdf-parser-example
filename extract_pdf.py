#!/usr/bin/python3

import pymupdf
import json
import datetime
from sorcery import dict_of #pip install sorcery
import glob
import pandas as pd


def get_value_by_key(json: str, block:int, line:int, span:int) -> str:
    try:
        return json["blocks"][block]["lines"][line]["spans"][span]["text"].replace('\xa0', ' ').strip()
    except:
        return ""

def extracts_info_from_pdf(file) -> dict:
    out={}

    doc = pymupdf.open(file) 
    jpage = json.loads(doc[0].get_text("json"))

    is_wiki="yes" if get_value_by_key(jpage,8,0,0) == "Welcome to Wikipedia" else "no"
    count_of_articles=get_value_by_key(jpage,10,0,0).split()[0].replace(',', '') #6,864,026 articles in English
    date_of_extract=datetime.datetime.strptime(get_value_by_key(jpage,17,0,0), "%B %d").replace(year=2024)  #"August 7"

    out.update(dict_of(is_wiki, 
                       count_of_articles, 
                       date_of_extract))

    ## adding file description at the end for reference
    out.update(dict_of(file))

    return out    

if __name__ == "__main__":
    path = "*.pdf"
    extracts=[] 
    for file in glob.glob(path, recursive=True):
        extracts.append(extracts_info_from_pdf(file))

    df_extracts = pd.DataFrame(extracts)
    print(df_extracts)
    df_extracts.to_csv("extracts.csv")