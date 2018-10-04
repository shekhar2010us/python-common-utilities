import sys
sys.path.append('../')

from src.ds import linked_list

def main():
    sample = linked_list.SinglyLinkedList()

    sample.add(10)
    sample.add(12)
    sample.add(7)
    sample.add(3)

    print(sample.print_list())

    print(sample.search(7))
    print(sample.search(8))

    sample.reverse()
    print(sample.print_list())

    sample.remove_last()
    print(sample.print_list())

    sample.add(8)
    sample.add(23)
    sample.add(17)
    print(sample.print_list())

    sample.remove(8)
    print(sample.print_list())

    sample.remove(3)
    print(sample.print_list())

    sample.remove(17)
    print(sample.print_list())

    sample.remove(12)
    print(sample.print_list())

    sample.remove(7)
    print(sample.print_list())

    sample.remove(23)
    print(sample.print_list())


if __name__ == '__main__':
    main()