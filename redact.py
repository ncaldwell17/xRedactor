import spacy
from nltk import word_tokenize
nlp = spacy.load('en_core_web_lg')


class ClauseRedactor(object):

    def __init__(self, redactors=None):
        # self._redactors is a list of redaction methods
        self._redactors = list()

        if redactors is not None:
            self._redactors += redactors

    def redact(self, clause):
        for redactor in self._redactors:
            clause = redactor(clause)
        return clause


def organization_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'ORG':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def date_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'DATE':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def person_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'PERSON':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def location_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'GPE':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def faculty_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'FAC':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def art_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'WORK_OF_ART':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + f"REDACTED_{ent.label}" + new_string[end:]
    return new_string


redactor_dict = {'Redact Orgs': organization_redactor,
                 'Redact Dates': date_redactor,
                 'Redact People': person_redactor,
                 'Redact Addresses': location_redactor,
                 }


