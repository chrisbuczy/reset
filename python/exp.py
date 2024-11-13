input1 = 'forloops'
input2 = 'frlpz'
list1 = []
list2 = []

for let in input1:
    list1.append(let)

for let in input2:
    list2.append(let)



def identifysilent(word1, word2):
    if len(word1) == len(word2):
        silent = '-'
        return silent, identifysilly(word1, word2)
    for char in word1:
        if char in word2:
            continue
        else:
            copy1 = [i for i in word1 if i != char]
            print(copy1)
            if len(copy1) == len(word2):
                silent = char
                break
    return silent, identifysilly(copy1, word2)

                
    
def identifysilly(word1, word2):
    for let in word1:
        x = word1.index(let)
        if word1[x] != word2[x]:
            return word1[x], word2[x]

print(identifysilent(list1, list2))
