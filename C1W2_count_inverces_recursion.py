# a = eval(input())
text_file = open("Integer_array.txt", "r")
lines = list(map(int, text_file.read().split('\n')[:-1]))


lines[0]
print(lines)
a = [1, 5, 3, 2, 6, 0]

inverces = 0

def merge(a, b):
    global inverces
    i = 0
    j = 0
    temp = []
    while i < len(a) and j < len(b):
        if b[j] < a[i]:
            temp.append(b[j])
            inverces += len(a) - i
            j += 1
        else:
            temp.append(a[i])
            i += 1
    while i < len(a):
        temp.append(a[i])
        i += 1
    while j < len(b):
        temp.append(b[j])
        j += 1
    return temp

# print(merge([5], [3]))
# print(inverces)
def num_inv(a):
    n = len(a)
    if n == 1:
        return a
    else:
        mid = n // 2
        a_left = num_inv(a[:mid])
        a_right = num_inv(a[mid:])
        return merge(a_left, a_right)


num_inv(lines)
print(inverces)
