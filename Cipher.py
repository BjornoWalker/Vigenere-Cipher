alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

# The decoder


def vigenere_decoder(coded_message, keyword):
    keyword_repeated = ''
    while len(keyword_repeated) < len(coded_message):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(coded_message)]
    translated_message = ''
    for i in range(0, len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - \
                alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

# The encoder


def vigenere_coder(message, keyword):
    keyword_repeated = ''
    while len(keyword_repeated) < len(message):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(message)]
    translated_message = ''
    for i in range(0, len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message


# An example of how to use the funtion with a message and a key
(print(vigenere_coder("I love you Paige", "love")))
(print(vigenere_decoder("k gsgs czi dlwbi", "love")))
