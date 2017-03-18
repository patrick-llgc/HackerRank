from collections import Counter

def number_needed(a, b):    
    ctr_a = Counter(list(a))
    ctr_b = Counter(list(b))
    keys = set(list(ctr_a.keys()) + list(ctr_b.keys()))
    return sum(abs(ctr_a[key] - ctr_b[key]) for key in keys)
        

a = input().strip()
b = input().strip()

print(number_needed(a, b))
