class Redact(object):

    def __init__(self, sentence):
        # need this so the program knows what to highlight for the user
        self.sentence = arrange_grams(sentence)
        self.redacted_terms = list()

    # TODO: def arrange_grams(sentence):
    #   find a library to split into n-grams UNLESS that messes up SpaCy, which would be frustrating.
    #   this MIGHT BE unnecessary if SpaCy splits a sentence automatically
    #   pass

    # TODO: def redact(sentence):
    #   self.redacted_terms.append(redact_method_one(sentence)

    # TODO: def nerf_orgs(sentence):
    #   whatever process to find organizations, probably SpaCy


