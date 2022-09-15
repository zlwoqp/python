mystr = 'X-DSPAM-Confidence:0.8475'

posat = mystr.find(':')

result = float(mystr[posat+1:])

print(result)