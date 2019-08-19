a = eval(input())

n = len(a)


def sec_max(a, n):
    max_ = None
    s_max_ = None

    if n == 2:
        if a[0] > a[1]:
            max_, s_max_ = a[0], a[1]
        else:
            max_, s_max_ = a[1], a[0]
        return max_, s_max_

    else:
        max_l, s_max_l = sec_max(a[:n // 2], n // 2)
        max_r, s_max_r = sec_max(a[n // 2:], n // 2)

        return max(max_l, max_r), max(min(max_l, max_r), s_max_l, s_max_r)


print("Second maximum:", sec_max(a, n)[1])