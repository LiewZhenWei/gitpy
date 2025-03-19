def get_word(word_type):
    if word_type.lower()=='adjective':
        a_or_an=an
    else:
        a_or_an=a
    return input("Enter a word that is {0} {1} :".format(a_or_an,word_type))



