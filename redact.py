import spacy
nlp = spacy.load('en_core_web_lg')


class ClauseRedactor(object):

    def __init__(self, redactors=None):
        # self._redactors is a list of redaction methods
        self._redactors = list()
        if redactors is not None:
            self._redactors += redactors

    def redact(self, clause):
        for redactor in self._redactors:
            # NOTE, if you want the redactors to return more things like the actual terms, that needs to be another list
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


def gpe_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'GPE':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def fac_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'FAC':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


def woa_redactor(string):
    doc = nlp(string)
    new_string = string
    for ent in reversed(doc.ents):
        if ent.label_ == 'WORK_OF_ART':
            start = ent.start_char
            end = start + len(ent.text)
            new_string = new_string[:start] + "REDACTED" + new_string[end:]
    return new_string


clause_redactor = ClauseRedactor([organization_redactor,
                                  date_redactor,
                                  person_redactor,
                                  gpe_redactor,
                                  fac_redactor,
                                  woa_redactor])

example_clause = 'THIS MASTER SERVICES AGREEMENT (the "Agreement") is made and entered into as of October 16, 2017 (the ' \
                 '“Effective  Date”)  between  Allens  Operations  Pty  Ltd  (ABN:  87  004  992  607),  with  its  office  at  Level  28, ' \
                 'Deutsche Bank Place, 126 Philip Street, Sydney, NSW 2000 (the "Company") and Elevate Services Australia, ' \
                 'Pty. Ltd., Level 3, 44 Martin Place, Sydney, NSW 2000 (“Elevate”).'

redacted_clause = clause_redactor.redact(example_clause)
print(redacted_clause)


