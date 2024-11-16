# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/5650650786168832

from linked_list import from_list


def get_middle_node(head):
    slow = head
    fast = head

    while fast:
        fast = fast.next
        if not fast:
            break
        fast = fast.next
        slow = slow.next
        
    return slow


if __name__ == "__main__":
    for values in [
        [1],
        [1, 2,],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
    ]:
        linked_list = from_list(values)
        print(linked_list, "   =>    ", get_middle_node(linked_list.head)._value)
