# get inputs
T = input().strip()
topic = []
for topic_i in range(int(T)):
    topic_t = str(input().strip())
    min_del = 0
    for i in range(1, len(topic_t)):
        if topic_t[i-1] == topic_t[i]:
            min_del = min_del + 1
    print(min_del)
    
"""
# alternative way
def find_min_del(input_string):
    min_del = 0
    current_char = ''
    for char in input_string:
        if char == current_char:
            min_del = min_del + 1
        else:
            current_char = char
    return min_del

for input_string in topic:
    print(find_min_del(input_string))
"""    