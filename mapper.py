import sys

#input comes from STDIN (standard input)
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    #split the line into words
    words = line.split()
    #increase counters
    for word in words:
        #write the result in stdout
        #what we output here will be tr input for the reducer
        print(word, 1)
