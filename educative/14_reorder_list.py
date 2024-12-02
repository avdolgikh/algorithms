# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/4680969711517696


from linked_list import LinkedListNode, LinkedList, from_list


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


def reverse(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


def reorder_list(head):
    first = head
    middle_node = get_middle_node(first)
    second = reverse(middle_node)
    
    # merge 2 lists (`first` and `second`)
    while first:
        f_next = first.next
        if second:
            s_next = second.next
        first.next = second
        first = f_next        
        if second:
            second.next = f_next
            second = s_next
        
    return head


if __name__ == "__main__":
    for values in [
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
    ]:
        linked_list = from_list(values)
        print(linked_list, end="")

        head = reorder_list(linked_list.head)
        linked_list = LinkedList()
        linked_list.head = head
        print("  ===>  ", linked_list)

