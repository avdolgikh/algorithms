# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/6183383740448768

from linked_list import LinkedListNode, LinkedList, from_list


def remove_nth_last_node(
    head: LinkedListNode,
    n: int,
) -> LinkedListNode:
    wrapper_list = LinkedListNode(0, head) # Create a dummy node pointing to head
    left, right = wrapper_list, head

    # Move right pointer n steps ahead
    for _ in range(n):
        right = right.next
    
    # Move both pointers until right reaches the end
    while right:
        left = left.next
        right = right.next

    # Remove the nth last node
    left.next = left.next.next

    return wrapper_list.next



if __name__ == "__main__":
    values = [1, -10, 5, 78]  # [], [0]
    k = len(values)
    
    for n in list(range(1, k+1)):
        print(f"k = {k}, n = {n}")

        linked_list = from_list(values)
        print(linked_list)

        head = remove_nth_last_node(linked_list.head, n)
        linked_list = LinkedList()
        linked_list.head = head
        print(linked_list)
        print("-"*10)
