def solution1():
    """Solution without dependencies"""
    N = int(input().strip())
    worddict = {}
    for _ in range(N):
        t_str = input().strip()
        if t_str in worddict:
            worddict[t_str] += 1
        else:
            worddict[t_str] = 1

    Q = int(input().strip())
    for _ in range(Q):
        t_str = input().strip()
        if t_str in worddict:
            print(worddict[t_str])
        else:
            print(0)
            
def solution2():
    """Solution using Counter()"""
    from collections import Counter
    ctr = Counter(input().strip() for _ in range(int(input().strip())))
    for _ in range(int(input().strip())):
        print ctr[input().strip()]

if __name__ == "__main__":
    solution2()