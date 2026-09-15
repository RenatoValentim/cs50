from typing import Any, Generator


class _Node:
    def __init__(self, val: Any, next: _Node | None = None) -> None:
        self.val: Any = val
        self.next: _Node | None = next

    def __repr__(self) -> str:
        return f"Node(value: {self.val!r}, next: {self.next!r})"


class LinkedList:
    def __init__(self) -> None:
        self.__head: _Node | None = None
        self.__tail: _Node | None = None
        self.__length: int = 0

    def prepend(self, val: Any) -> None:
        node = _Node(val)
        if self.__head is None:
            self.__head = node
            self.__tail = node
            self.__length += 1
            return
        temp = self.__head
        self.__head = node
        self.__head.next = temp
        self.__length += 1

    def append(self, val: Any) -> None:
        node = _Node(val)
        if self.__head is None:
            self.__head = node
            self.__tail = node
            self.__length += 1
            return
        self.__tail.next = node
        self.__tail = node
        self.__length += 1

    def find(self, val: Any) -> _Node | None:
        current = self.__head
        while current is not None:
            if current.val == val:
                return current
            current = current.next
        return None

    def remove(self, val: Any) -> bool:
        if self.__head is None:
            return False
        if self.__head.val == val:
            if self.__head is self.__tail:
                self.__tail = self.__head.next
            self.__head = self.__head.next
            self.__length -= 1
            return True
        previous: _Node | None = None
        current: _Node | None = self.__head
        while current.next is not None:
            previous = current
            current = current.next
            if current.val == val:
                if current is self.__tail:
                    self.__tail = previous
                previous.next = current.next
                self.__length -= 1
                return True
        return False

    def get(self, index: int) -> _Node | None:
        current = self.__head
        i = 0
        while current is not None:
            if i == index:
                return current
            current = current.next
            i += 1
        return None

    def insert_after(self, target_val: Any, new_val: Any) -> bool:
        if self.__tail is None:
            return False
        if target_val == self.__tail.val:
            self.append(new_val)
            return True
        node = _Node(val=new_val)
        current = self.__head
        while current is not None:
            if current.val == target_val:
                temp = current.next
                current.next = node
                node.next = temp
                self.__length += 1
                return True
            current = current.next
        return False

    def reverse(self) -> None:
        previous: _Node | None = None
        current: _Node | None = self.__head

        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        temp = self.__head
        self.__head = self.__tail
        self.__tail = temp

    def __len__(self) -> int:
        return self.__length

    def __iter__(self) -> Generator[Any, Any, None]:
        current: _Node | None = self.__head
        while current is not None:
            yield current.val
            current = current.next

    def __repr__(self) -> str:
        if self.__head is None:
            return "LinkedList(head: None, tail: None)"
        return f"LinkedList(head: Node(value: {self.__head.val!r}, next: {self.__head.next!r}), tail: {self.__tail!r})"
