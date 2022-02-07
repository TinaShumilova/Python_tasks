str = 'ыбопграбв логреп абвмпр рррр'
print(str)
tr = str.split()
print(tr)
[tr.remove(word) for word in tr[:] if 'абв' in word]
print(tr)