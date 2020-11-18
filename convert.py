import os

with open("00_09_30_to_00_10_09.txt") as textFile:
    lines = []
    words = []
    i = 3422
    
    for line in textFile:
        lines.append(line)
        ind = 0
        for word in line.split():
                words.append(word)
                words[ind] = word
                ind = ind + 1
                # words[0] --> frame number
                # words[1] --> drone number
                # words[2+5k] --> x
                # words[3+5k] --> y
                # words[4+5k] --> width
                # words[5+5k] --> height
                # words[6+5k] --> class
                # words[7] --> x
                # words[8] --> y
                # ....  words [11]
        if words[1] == '0':
           i = i + 1
           continue
        with open(str(i) + '.txt', "w") as outFile:
            for m in range(0, int(words[1])):
                if words[6+5*m] == 'drone':
                    words[6+5*m] = '0'
                outFile.write(words[6+5*m] + " " + words[2+5*m] + " " + words[3+5*m] + " " + words[4+5*m] + " " + words[5+5*m] + '\n')
            
        words.clear()
        i=i+1
        
