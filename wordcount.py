def count_words(filename):

    lines = open(filename)
    count_words = {}

    for line in lines:
        line = line.rstrip()
        line = line.split(" ")
        #line = [(words in that line, tokenized and put into this list)]
        # for word in lines
        print(line)
    
