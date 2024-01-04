#!/usr/bin/env python3

dictionary = {}
testWords = []

def parseFirstLine(line):
    words = line.split(" | ")
    for word in words:
        result = word.split(": ")
        if result[0] in dictionary:
            dictionary[result[0]].append(result[1])
        else:
            dictionary[result[0]] = [ result[1], ]
        #endif
    #endfor
#enddef

def parseSecondLine(line):
    global testWords
    testWords = line.split(" | ")
#enddef

parseFirstLine(input())
parseSecondLine(input())

line3 = input()

if line3 == "Test":
    for i in testWords:
        if i in dictionary:
            print(f"{i}:")
            for f in dictionary[i]:
                print(f" -{f}")
        #endif
    #endfor
elif line3 == "Hand Over":
    for val in dictionary.keys():
        print(val, end=' ')
    #endfor
#endif