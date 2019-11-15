from collections import defaultdict


class heapdict:

    def __init__(self, order):
        self.heap = []
        self.names = []
        self.sources = []
        self.into = dict()
        self.order = order #True - maxheap, False - minheap

    def is_valid(self, parent, child):
        if parent < len(self.heap) and child < len(self.heap):
            if self.order:
                return self.heap[parent] >= self.heap[child]
            else:
                return self.heap[parent] <= self.heap[child]


    def swap(self, i, j):
        print(i,j)
        # print(i, j)
        print('Names: {}'.format(len(self.names)))
        print('Heap: {}'.format(len(self.heap)))
        # print('Into: {}'.format(list(self.into.items())))
        # print('Distances: {}'.format(cum_dist))

        self.into[str(self.names[i])], self.into[str(self.names[j])] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.names[i], self.names[j] = self.names[j], self.names[i]
        self.sources[i], self.sources[j] = self.sources[j], self.sources[i]



    def shift_up(self, c_i):
        p_i = (c_i - 1) // 2
        if p_i == c_i:
            return
        while not self.is_valid(p_i, c_i) and c_i < len(self.heap):
            self.swap(p_i, c_i)
            c_i = p_i
            if c_i == 0:
                break
            p_i = (c_i - 1) // 2

        # l = 2 * p_i + 1
        # r = 2 * p_i + 2
        # if not self.is_valid(p_i, l) or not self.is_valid(p_i, r):
        #     self.shift_down(p_i)


    def shift_down(self, p_i):
        c_i = self.get_swap_child_ind(p_i)
        if p_i == c_i:
            return
        while c_i and not self.is_valid(p_i, c_i):
            self.swap(p_i, c_i)
            p_i = c_i
            c_i = self.get_swap_child_ind(p_i)

    def get_swap_child_ind(self, p_i):
        l_i = 2*p_i + 1
        r_i = 2*p_i + 2
        size = len(self.heap)

        if l_i >= size:
            return None
        elif r_i >= size:
            return l_i

        if self.order:
            return max(l_i, r_i, key=lambda x: self.heap[x])
        else:
            return min(l_i, r_i, key=lambda x: self.heap[x])


    def add_item(self, item):

        key, value, source = item
        if str(key) in self.into:
            self.delete(key)
        self.heap.append(value)
        self.names.append(str(key))
        self.sources.append(source)
        self.into[str(key)] = len(self.heap) - 1
        self.shift_up(len(self.heap) - 1)


    def __getitem__(self, key):
        try:
            return key, self.heap[self.into[str(key)]], self.sources[self.into[str(key)]]
        except KeyError:
            raise KeyError('No such name in heapdict')

    def delete(self, key):
        k_i = self.into[str(key)]
        self.swap(k_i, -1)
        removed_value = self.heap.pop()
        removed_name = self.names.pop()
        removed_src = self.sources.pop()
        if len(self.heap) != 0:
            p_i = (k_i - 1) // 2

            if self.is_valid(p_i, k_i):
                self.shift_down(k_i)
            else:
                self.shift_up(k_i)
        del self.into[str(key)]

        return int(removed_name), removed_value, removed_src

    def extract_root(self):
        if self.heap:
            self.swap(0, len(self.heap)-1)
            root_val = self.heap.pop()
            root_name = self.names.pop()
            root_src = self.sources.pop()
            del self.into[str(root_name)]
            if len(self.heap) > 1:
                self.shift_down(0)
            return int(root_name), root_val, root_src

    def get_root(self):
        if self.heap:
            return int(self.names[0]), self.heap[0], self.sources[0]

