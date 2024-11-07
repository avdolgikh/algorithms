# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/4614588014002176

from linked_list import LinkedListNode, LinkedList, from_list, cycled_from_list


def detect_cycle(head):
    slow = head
    fast = head

    while fast:
        slow = slow.next
        
        fast = fast.next
        if fast:
            fast = fast.next

        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    values = [1, 2, 3]  # [], [1]

    linked_list = from_list(values)
    print(linked_list, detect_cycle(linked_list.head))

    linked_list = cycled_from_list(values, 1)
    print(linked_list, detect_cycle(linked_list.head))
