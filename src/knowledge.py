import json


KNOWLEDGE_FILE = "knowledge/diseases.json"


def load_knowledge():

    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def get_disease_knowledge(disease):

    knowledge = load_knowledge()

    return knowledge.get(disease)