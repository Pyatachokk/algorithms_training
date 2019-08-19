import argparse
import sys
comp = 0

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

    sorted_list = sort(lines, 0, len(lines) - 1)

    try:
        writing_file = open(outfile[0], "w")
        writing_file.write("\n".join(list(map(str, sorted_list))))
    except:
        print("\n" + "Sorted array: " + " ".join(list(map(str, sorted_list))))
    print("Number of comparisons: " + str(comp))

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

# # print(sort(a, 0, len(a) - 1))
#
# lines = sort(lines, 0, len(lines) - 1)
# for i in range(1, len(lines)):
#     if lines[i] < lines[i-1]:
#         print('FUCK')
#         break
# print(comp)
# sort(lines, 0, len(lines) - 1)
# print(sort(lines, 0, len(lines) - 1))