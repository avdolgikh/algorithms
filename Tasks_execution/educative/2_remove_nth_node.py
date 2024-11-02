# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/6183383740448768

from typing import Optional

class LinkedListNode:
    def __init__(
        self,
        value: int,
        next: Optional["LinkedListNode"] = None,
    ):
        self._value = value
        self.next = next

    def __repr__(self) -> str:
        return f"{self._value}"


class LinkedList:
    def __init__(self):
        self.head: Optional[LinkedListNode] = None

    def append(self, value: int) -> None:
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(repr(current))
            current = current.next
        return " -> ".join(values)



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

def from_list(list_: list) -> LinkedList:
    linked_list = LinkedList()
    for value in list_:
        linked_list.append(value)
    return linked_list


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
