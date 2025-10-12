word =  'test'

length = len(word)
if length % 2 == 1:
    mid = length // 2
    print(word[mid])
else:
    mid = length // 2
    print(word[mid-1:mid+1])
