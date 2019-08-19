a = eval(input())
low = 0
high = len(a) - 1


def find_same(a, low, high):
    if low == high:
        if a[low] == low:
            return True
        else:
            return False
    else:
        mid = low + ((high - low) // 2)

        if a[mid] > mid:
            return find_same(a, low, mid)
        elif a[mid] < mid:
            return find_same(a, mid+1, high)
        else:
            return True


print(find_same(a, low, high))
