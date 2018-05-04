from difflib import get_close_matches
import json
import os


def findMedicineName(text_list):

    close_match = []

    with open('medicine_list.json', encoding='utf-8') as json_data:
        medicine_list = json.load(json_data)['medicineList']

    for i in text_list:
        close_matches = get_close_matches(i, medicine_list, cutoff=0.8)
        if close_matches:
            for i in close_matches:
                close_match.append(i)

    return list(set(close_match)) if close_match else -1
