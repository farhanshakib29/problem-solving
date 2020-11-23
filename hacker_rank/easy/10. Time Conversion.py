import re

times = input()

timeRegex = re.compile(r'''
                           (\d{2})
                           :
                           (\d{2})
                           :
                           (\d{2})
                           (AM|PM)
                                   ''', re.VERBOSE)

output = timeRegex.search(times)
output = list(output.groups())

if output[3] == 'PM':
    if output[0] != '12':
        output[0] = str(int(output[0])+12)
        
elif output[3] == 'AM' and output[0] == '12':
    output[0] = '00'

ftime = output[0] + ':' + output[1] + ':' + output[2]
print(ftime)
