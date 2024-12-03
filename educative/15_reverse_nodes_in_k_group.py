# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/5526437354012672


from linked_list import LinkedListNode, LinkedList, from_list


def reverse_group(start, count):
    prev = None
    cur = start
    while count > 0:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        count -= 1
    start.next = cur  # Connect the reversed group to the next group
    return prev


def reverse_k_groups(head, k):
    dummy = LinkedListNode(0, head)  # Create a dummy node for easier management of head
    prev = dummy
    cur = head

    while cur:
        # Find the size of the current group
        group_start = cur
        count = 0
        while count < k and cur:
            cur = cur.next
            count += 1

        # Check if the group size is k
        if count == k:  
            # Reverse the group
            prev.next = reverse_group(group_start, k)
            prev = group_start  # group_start is now the tail after reversal

    return dummy.next


if __name__ == "__main__":
    for values, k in [
        ([1], 1),
        ([1, 2, 3, 4], 1),
        ([1, 2, 3, 4], 4),
        ([1, 2, 3, 4, 5, 6, 7], 2),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
    ]:
        linked_list = from_list(values)
        print(linked_list, end="")

        head = reverse_k_groups(linked_list.head, k)
        linked_list = LinkedList()
        linked_list.head = head
        print(f", k={k}  ===>  {linked_list}")


