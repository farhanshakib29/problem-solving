# https://www.hackerrank.com/challenges/the-time-in-words/problem

words = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
    'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five',
    'twenty six', 'twenty seven', 'twenty eight', 'twenty nine',
]

hour = int(input())
minute = int(input())

if minute <= 30:
    if minute == 00:
        time = words[hour-1] + ' o\' clock'
    elif minute == 15:
        time = 'quarter past ' + words[hour-1]
    elif minute == 30:
        time = 'half past ' + words[hour-1]
    else:
        if minute == 1:
            time = 'one minute past ' + words[hour-1]
        else:
            time = words[minute-1] + ' minutes past ' + words[hour-1]
else:
    minute = 60 - minute
    if minute == 15:
        time = 'quarter to ' + words[hour]
    else:
        if minute == 1:
            time = 'one minute to ' + words[hour]
        else:
            time = words[minute-1] + ' minutes to ' + words[hour]
print(time)
    