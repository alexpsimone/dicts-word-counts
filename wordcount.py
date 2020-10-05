def count_words(filename):

    lines = open(filename)
    counting_words = {}

    for line in lines:
        line = line.rstrip()
        line = line.split(" ")
        #line = [(words in that line, tokenized and put into this list)]
        for word in line:
            counting_words[word] = counting_words.get(word, 0) + 1
            #Check to see if a word is in the dictionary, using the get method.
            #2nd argument is the return value if the 1st argument is not found in the dictionary.
            #If the word is not in the dictionary, then return 0.
            #Will add 1 after the get method is evaluated.

    return counting_words
    
