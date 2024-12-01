# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/5831027173621760


from linked_list import LinkedListNode, LinkedList, from_list


def reverse_even_length_groups(head):
    dummy = LinkedListNode(0, head)  # Create a dummy node for easier management of head
    prev = dummy
    cur = head
    group_index = 1  # Start with group size of 1

    while cur:
        # Find the size of the current group
        group_start = cur
        count = 0
        while count < group_index and cur:
            cur = cur.next
            count += 1

        # Check if the group size is even
        if count % 2 == 0:
            # Reverse the group
            prev.next = reverse_group(group_start, count)
            prev = group_start  # group_start is now the tail after reversal
        else:
            prev = group_start
            for _ in range(count - 1):
                prev = prev.next

        # Increment the group size
        group_index += 1

    return dummy.next


def reverse_group(start, count):
    prev = None
    cur = start
    while count > 0:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
        count -= 1
    start.next = cur  # Connect the reversed group to the next group
    return prev


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8]  # Test case

    linked_list = from_list(values)
    print(linked_list, end="")

    head = reverse_even_length_groups(linked_list.head)
    linked_list = LinkedList()
    linked_list.head = head
    print("  ===>  ", linked_list)


