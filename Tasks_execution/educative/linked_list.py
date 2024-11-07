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


MAX_LENGTH_TO_SHOW = 10


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

    def get_node(self, index: int) -> LinkedListNode:
        current = self.head
        for i in range(index):
            if not current:
                return None
            current = current.next
        return current

    def __repr__(self) -> str:
        values = []
        current = self.head
        count = 0
        while current and count <= MAX_LENGTH_TO_SHOW:
            values.append(repr(current))
            current = current.next
            count += 1
        return " -> ".join(values)


def from_list(list_: list) -> LinkedList:
    linked_list = LinkedList()
    for value in list_:
        linked_list.append(value)
    return linked_list


def cycled_from_list(list_: list, cycle_node_index: int) -> LinkedList:
    linked_list = from_list(list_)
    last_node = linked_list.get_node(len(list_) - 1)
    cycle_node = linked_list.get_node(cycle_node_index)
    last_node.next = cycle_node
    return linked_list
