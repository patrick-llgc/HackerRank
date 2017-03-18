def ransom_note(magazine, ransom):
    vocab = {}
    for word in magazine:
        if word in vocab:
            vocab[word] += 1
        else:
            vocab[word] = 1
    for word in ransom:
        if word not in vocab or vocab[word] < 1:
            return False
        elif word in vocab:
            vocab[word] -= 1
    return True

def ransom_note2(magazine, ransom):
    from collections import Counter
    return Counter(ransom) - Counter(magazine) == {}

def ransom_note3(magazine, ransom):
    from collections import defaultdict
    vocab = defaultdict(int)
    for word in magazine:
        vocab[word] += 1
    for word in ransom:
        if vocab[word] == 0:
            return False
        vocab[word] -= 1
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note3(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
