import sys

current_word = None
current_count = 0
word = None

#input from stdin
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    #parse the input from the mapper
    word, count = line.split('\t', 1)
    #convert the count to an int
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(current_word, current_count)
        current_word = word
        current_count = count

if current_word:
    print(current_word, current_count)
    