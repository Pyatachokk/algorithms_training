import argparse
import sys
count = 0

def ToCommandLine():

    parser = argparse.ArgumentParser(description= 'Quicksort algorythm with first entry as pivot.')
    parser.add_argument('--infile', metavar = 'Input', nargs = 1, type = str, default = sys.stdin, help = 'Input txt file. If not specified, stdin.')
    parser.add_argument('--outfile', metavar = 'Output', nargs = 1, type = str, default=sys.stdout, help = 'Output txt file. If not specified, stdout.')
    args = parser.parse_args()

    sorting_fun(args.infile, args.outfile)

def sorting_fun(infile, outfile):
    try:
        text_file = open(infile[0], "r")
        lines = list(map(int, text_file.read().split('\n')[:-1]))
    except:
        lines = list(map(int, input().split()))

    sorted_list = sort_median(lines, 0, len(lines) - 1)

    try:
        writing_file = open(outfile[0], "w")
        writing_file.write("\n".join(list(map(str, sorted_list))))
    except:
        print("\n" + "Sorted array: " + " ".join(list(map(str, sorted_list))))
    print("Number of comparisons: " + str(count))

def sort_median(a, low, high):
    if low >= high:
        return
    buffer = None

    if high - low == 1:
        pivot = low
    else:

        middle = (low + high) // 2

        first = low
        last = high

        if a[first] > a[middle]:
            buffer = first
            first = middle
            middle = buffer
        if a[middle] > a[last]:
            buffer = middle
            middle = last
            last = buffer
        if a[first] > a[middle]:
            buffer = first
            first = middle
            middle = buffer
        pivot = middle

        buffer = a[pivot]
        a[pivot] = a[low]
        a[low] = buffer

        pivot = low

    global count
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
    count += (high - low)
    sort_median(a, low, i - 2)
    sort_median(a, i , high)

    return a

if __name__ == '__main__':
    ToCommandLine()

