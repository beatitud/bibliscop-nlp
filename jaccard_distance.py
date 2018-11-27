# coding: utf-8

import json

with open('./bible.json', 'rb') as f:
    bible = json.load(f)

verse_ref = input("Pick a verse ref: ")
verse_ref = "psa_81_4"

verse = bible.get(verse_ref)
print(verse["text_bj"])