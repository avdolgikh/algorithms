# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/6611309476708352


from linked_list import LinkedListNode, LinkedList, from_list


def reverse(head):
    prev_node = None
    node = head
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node


if __name__ == "__main__":
    values = [1, 2, 3]  # [], [1]

    linked_list = from_list(values)
    print(linked_list, end="")

    head = reverse(linked_list.head)
    reversed_linked_list = LinkedList()
    reversed_linked_list.head = head
    print("  ===>  ", reversed_linked_list)
