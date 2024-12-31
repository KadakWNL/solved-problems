#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence: str) -> str:
    words = sentence.split()
    result = []
    for word in words:
        new_word = word[0]
        for i in range(1,len(word)):
            if ord(word[i-1].lower()) < ord(word[i].lower()):
                new_word += word[i].upper()
            elif ord(word[i-1].lower()) > ord(word[i].lower()):
                new_word += word[i].lower()
            else:
                new_word += word[i]
        result.append(new_word)
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()