from collections import deque


class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __str__(self):
        return f"k: {self.k},v: {self.v}"


class MyDict:
    def __init__(self):
        self.lst = [None for _ in range(10)]
        self.size = 0
        if self.size/len(self.lst)*100>70:
            self.lst*=2
    def add(self, k, v):
        index: int = hash(k) % len(self.lst)
        if self.lst[index] is None:
            self.lst[index] = Node(k=k, v=v)
            self.size+=1
            return
        if isinstance(self.lst[index], deque):
            for item in self.lst[index]:
                if item.k == k:
                    item.v = v
                    self.size += 1
                    return
            self.lst[index].append(Node(k=k, v=v))
            self.size += 1
            return
        if self.lst[index].k == k:
            self.lst[index].v = v
            self.size += 1
            return
        temp_lst = deque()
        temp_lst.append(self.lst[index])
        temp_lst.append(Node(k=k, v=v))
        self.lst[index] = temp_lst
        self.size += 1

    def get(self, k):
        for item in self.lst:
            if isinstance(item, Node) and item.k == k:

                return item
        return False

    def pop(self, k):
        for item in self.lst:
            if isinstance(item, Node) and item.k == k:
                self.lst.remove(item)
                self.size -= 1

    def clear(self):
        self.lst = [None for _ in range(10)]
        self.size = 0

    def __str__(self):
        return str(self.lst)


d = MyDict()
d.add(1, 123)
d.add(3, '2221')
d.add(2, '1hjds')
d.add(10, 'rtree')
d.add('pyt', 'hello')
d.add(4, 'hello')
d.add('pyt', 'hello')
d.add(2, 123)
d.add(9, '2221')
d.add(10, '1hjds')
d.add(8, 'rtree')
d.add(7, 'hello')
d.add(6, 'hello')
d.add(5, 'hello')
d.pop(1)
d.pop(3)
d.pop(2)
print(d)
print(d.get(6))
d.clear()
print(d)

# d.get()
# d.pop()
# d.clear()
