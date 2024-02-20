import json

in_file = "../Re-DocRED/data/train_revised.json"
out_file = "../input/train.json"

with open(in_file, 'r') as file:
    data_dict = json.load(file)

def get_doc(sents):
    doc = ""
    for sent in sents:
        for word in sent:
            doc += (word + " ")
    return doc

def get_entity(e):
    

def get_corref(c):


def get_rel(r):
    