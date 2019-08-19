a = [1, 100, 3]
# print(eval(a))

# a = list(input())


n = len(a)

def find_max(a, n):
    if n == 2:
        return max(a)
    else:
        mid = n//2
        if a[mid + 1] > a[mid]:
            return find_max(a[mid+1:], n//2)
        else:
            return find_max(a[:mid+1], n//2 + 1)
print(find_max(a, n))