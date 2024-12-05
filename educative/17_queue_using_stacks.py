# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/6464882096209920


from stack import Stack


class MyQueue(object):
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def _transfer_elements(self):
        while not self.push_stack.is_empty():
            self.pop_stack.push(self.push_stack.pop())

    def push(self, x):
        self.push_stack.push(x)

    def pop(self):
        if self.pop_stack.is_empty():
            self._transfer_elements()
        return (
            None if self.pop_stack.is_empty()
            else self.pop_stack.pop()
        )

    def peek(self):
        if self.pop_stack.is_empty():
            self._transfer_elements()
        return self.pop_stack.top()

    def empty(self):
        return self.push_stack.is_empty() and self.pop_stack.is_empty()


if __name__ == "__main__":
    q = MyQueue()
    print(q.push(1))
    print(q.push(2))
    print(q.push(3))
    print(q.pop())
    print(q.push(4))
    print(q.pop())
    print(q.peek())
    print(q.peek())
    print(q.empty())
    print(q.pop())
    print(q.pop())
    print(q.empty())
