def get_pswd(n):
    """Returns a password consisting of vowels and consonants in alternating order"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in vowels and chr(i) != 'y']

    pswd = vowels + consonants
    if n == 1:
        return pswd
    for i in range(2, n + 1):
        t_pswd = []
        for p in pswd:
            if p[-1] in vowels:
                newp = [p+c for c in consonants]
            else:
                newp = [p+c for c in vowels]
            t_pswd.extend(newp)
        pswd = t_pswd
    return pswd

print(len(get_pswd(4)))