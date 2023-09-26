import string, re, numpy as np


# tokenizer
def tokenizer(text):
    # print("tokenizer", text)
    if isinstance(text, bytes):
        text = text.decode(encoding="utf-8")
    if any(isinstance(text, t) for t in (list, tuple, np.ndarray)):
        return [tokenizer(t) for t in text]

    # Create a regular expression pattern to match tokens within angle brackets
    angle_bracket_pattern = r"<[^>]+>"

    # Updated pattern to include new lines and tabs as separate tokens
    token_pattern = angle_bracket_pattern + r"|[\w\-']+|[^\w\s]|\n|\t"

    # Split by whitespace, punctuation marks, new lines, and tabs while preserving tokens within angle brackets
    tokens = re.findall(token_pattern, text, re.UNICODE)
    # return [token.upper() if token[0] == "<" else token for token in tokens]
    newtokens = []
    for token in tokens:
        if token.startswith("<SPECIAL:"):
            newtokens.append(token.upper())
        elif token[0] in string.ascii_uppercase:
            newtokens.append("<SPECIAL:CAPITAL>")
            newtokens.append(token.lower())
        else:
            newtokens.append(token.lower())

    return newtokens


def detokenizer(tokens):
    # if iterable
    if any(isinstance(tokens, t) for t in (list, tuple, np.ndarray)) and not isinstance(tokens[0], str):
        return [detokenizer(token) for token in tokens]
    if isinstance(tokens, str):
        raise TypeError("detokenizer: tokens must be a list of strings")
    text = " "
    capitalize_next = True
    no_space_before = True
    for token in tokens:
        if token in ".,!?;]):'\"\n":
            no_space_before = True
        if token == "<SPECIAL:CAPITAL>":
            capitalize_next = True
            continue
        if capitalize_next:
            token = token.capitalize()
            capitalize_next = False

        if no_space_before:
            text += token
            no_space_before = False
        else:
            text += " " + token
        if token in "([<\n":
            no_space_before = True
    # return text.strip()

    # only strip spaces, not newlines
    return text.strip(" ")
