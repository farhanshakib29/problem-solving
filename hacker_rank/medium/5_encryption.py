# https://www.hackerrank.com/challenges/encryption/problem

import math

def clean(text):
    # remove spaces
    text = ''.join(text.split(' '))
    size = len(text)
    # not floor, bacause 3.8 needs to make 4, not 3
    rows = round(math.sqrt(size))
    cols = math.ceil(math.sqrt(size))

    # append whitespaces to handle things easier
    # ex - chilloutmyboy
    # chil
    # lout
    # mybo
    # y___
    # we need to make - clmy hoy iub lto
    # without these spaces, processing is complex
    spaces_needed = rows*cols-size
    if spaces_needed > 0:
        for i in range(spaces_needed):
            text += ' '
    return text, size+spaces_needed, rows, cols

def encrypt(text, size, rows, cols):
    splits = []
    
    rest = size
    for i in range(rows):
        rest -= cols
        start = i*cols
        if rest < 0:
            end = size
        else:
            end = start + cols
        
        splits.append(text[start:end])
    return splits, rows, cols

def print_enc(splits, rows, cols):
    enc_msg = []
    print(rows, cols)
    for col in range(cols):
        msg = ''
        for row in range(rows):
            msg += splits[row][col]
        enc_msg.append(msg.strip())
    
    print(' '.join(enc_msg))

print_enc(*encrypt(*clean(input())))