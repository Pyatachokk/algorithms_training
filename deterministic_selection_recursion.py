import random
import argparse
import sys  #

# Don't work
comp = 0
def ToCommandLine():

    parser = argparse.ArgumentParser(description= 'Quicksort algorythm with first entry as pivot.')
    parser.add_argument('--infile', metavar = 'Input', nargs = 1, type = str, default = sys.stdin, help = 'Input txt file. If not specified, stdin.')
    parser.add_argument('--outfile', metavar = 'Output', nargs = 1, type = str, default=sys.stdout, help = 'Output txt file. If not specified, stdout.')
    parser.add_argument('target', metavar = 'Target', nargs = 1, type = int, help = 'Target ordinal statistics')
    args = parser.parse_args()

    sorting_fun(args.infile, args.outfile, args.target)

def sorting_fun(infile, outfile, target):
    try:
        text_file = open(infile[0], "r")
        lines = list(map(int, text_file.read().split('\n')[:-1]))
    except:
        lines = list(map(int, input().split()))

    found = rand_sel(lines, target[0], 0, len(lines) - 1)

    try:
        writing_file = open(outfile[0], "w")
        writing_file.write('found\n')
    except:
        print(str(target[0]) + '`th order statistic: ' + str(found))

def middle_index(x):
    if len(x) % 2 == 0:
        return len(x) // 2 - 1
    else:
        return len(x) // 2

def lol(x,k):
    """ Function to divide a list into a list of lists of size k each. """
    return [x[i:i+k] for i in range(0,len(x),k)]

def ChoosePivot(x):
    """ Function to choose pivot element of an unsorted array using 'Median of Medians' method. """
    if len(x) <= 5:
        return sort(x, 0, len(x) - 1)[middle_index(x)]
    else:
        lst = lol(x,5)
        lst = [sort(el, 0, len(el) - 1) for el in lst]
        C = [el[middle_index(el)] for el in lst]
        return ChoosePivot(C)


def rand_sel(a, target, low, high):
    if low == high:
        return a[low]

    pivot = ChoosePivot(a)
    buffer = None
    buffer = a[pivot]
    a[pivot] = a[low]
    a[low] = buffer
    pivot = low

    marker = False
    i = low + 1
    j = low + 1

    while j <= high:
        if a[j] < a[pivot]:
            buffer = a[i]
            a[i] = a[j]
            a[j] = buffer
            i += 1
            j += 1
            marker = True
        else:
            j += 1

    if marker:
        # print(pivot)
        # print(i)
        # print(low, high)
        # print(a)
        buffer = a[pivot]
        a[pivot] = a[i-1]
        a[i-1] = buffer

        if i-1 == target:
            return a[i-1]
        elif i - 1  < target:
            return rand_sel(a, target, i, high)
        else:
            return rand_sel(a, target, low, i-2)
    else:
        if pivot == target:
            return a[pivot]
        else:
            return rand_sel(a, target, i, high)

def sort(a, low, high):
    if low >= high:
        return
    pivot = low
    pivot_val = a[pivot]
    buffer = None
    global comp
    i = low + 1
    j = low + 1
    marker = False
    while j <= high:
        if a[j] < a[pivot]:
            buffer = a[i]
            a[i] = a[j]
            a[j] = buffer
            i += 1
            j += 1
            marker = True
        else:
            j += 1
    if marker:
        buffer = a[pivot]
        a[pivot] = a[i-1]
        a[i-1] = buffer
    # else:
    #     buffer = a[pivot]
    #     a[pivot] = a[i]
    #     a[i] = buffer

    del buffer
    comp += len(a) - 1
    sort(a, low, i - 2)
    sort(a, i, high)

    return a



if __name__ == '__main__':
    ToCommandLine()