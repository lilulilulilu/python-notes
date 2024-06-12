# encoding: utf-8
# a = input("please input a number:")
class Node:
    def __init__(self):
        self.v = 0 #value
        self.e = set() #元素集合
        self.pre = None
        self.next = None

class MinMaxDict:
    def __init__(self):
        self.d = {}
        self.root = None
        self.tail = None

    def increase(self, key):
        if key not in self.d:
            node = Node()
            node.v += 1
            node.e.add(key)
            self.d[key] = node
            if self.root == None:
                self.root = node
            else:
                p = self.root.next
                node.next = p
                node.pre = self.root
                self.root.next = node
            if self.tail == None:
                self.tail = node     
        else:
            node = self.d[key]
            node.v += 1
            value = node.v
            if  node.next:
                if value == node.next.value:
                    node.e.remove(key)
                    node.next.e.add(key) 
                else:
                    n = Node()
                    n.v = value
                    n.e.add(key)
                    n.pre = node
                    n.next = node.next
                    node.next.pre = n
                    node.next = n
                    self.d[key] = n
                  
        
    def decrease(self, key):
        if key in self.d:
            node = self.d[key] 
            node.v -= 1
            if node.v == 0:
                if node == self.root:
                    self.root = node.next
                else:
                    node.pre.next = node.next
                    if node.next:
                        node.next.pre = node.pre
                del self.d[key]

    def get_max(self):
        if len(self.d) == 0:
            return None
        v = self.tail.e.pop()
        self.tail.e.add(v)
        return v

    def get_min(self):
        if len(self.d) == 0:
            return None
        v = self.root.e.pop()
        self.root.e.add(v)
        return v







