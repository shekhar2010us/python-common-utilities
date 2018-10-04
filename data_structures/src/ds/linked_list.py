import sys
sys.path.append('../../')

from src.common import mynode

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def size(self) -> int:
        return self.count

    def __add_first(self, element) -> (object, int):
        try:
            assert(self.count == 0)
        except AssertionError:
            print("The list is not empty, use add_next() instead !!")
        else:
            node = mynode.Node(element)
            self.head = node
            self.count += 1
            return element, self.count

    def __add_next(self, element) -> (object, int):
        try:
            assert(self.count > 0)
        except AssertionError:
            print("List is empty, use add_first() instead !!")
        else:
            node = mynode.Node(element)
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            self.count += 1
            return element, self.count

    def add(self, element) -> (object, int):
        if self.head is None:
            res = self.__add_first(element)
        else:
            res = self.__add_next(element)
        return res

    def search(self, element) -> int:
        try:
            assert(self.count > 0)
        except AssertionError:
            print('can\\\'t search, the list is empty ')
        else:
            curr = self.head
            index = -1
            while curr is not None:
                index += 1
                if element is curr.value:
                    return index
                curr = curr.next
        return -1

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def remove_last(self):
        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        self.count = self.count - 1

    def remove(self, element):
        curr = self.head
        prev = None
        while curr is not None:
            if element is not curr.value:
                prev = curr
                curr = curr.next
            elif self.count == 1:
                self.count = 0
                self.head = None
                break
            elif prev is not None:
                prev.next = curr.next
                self.count = self.count - 1
                break
            elif prev is None:
                self.head = curr.next
                self.count = self.count - 1
                break

    def print_list(self) -> str:
        try:
            assert(self.count > 0)
        except AssertionError:
            print('List is empty !!')
        else:
            res = []
            curr = self.head
            while curr.next is not None:
                res.append(curr.value)
                curr = curr.next
            res.append(curr.value)
            return ' -- '.join(str(x) for x in res)
