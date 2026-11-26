init python:

    # ============================================================
    # NÓ UTILIZADO PELA FILA E PILHA
    # ============================================================

    class Phase02Node:
        def __init__(self, data):
            self.data = data
            self.next = None


    # ============================================================
    # QUEUE - FILA (FIFO)
    # First In, First Out
    # ============================================================

    class Phase02Queue:

        def __init__(self):
            self.front = None
            self.rear = None
            self.size = 0

        def enqueue(self, data):
            new_node = Phase02Node(data)

            if self.is_empty():
                self.front = new_node
                self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node

            self.size += 1

        def dequeue(self):
            if self.is_empty():
                return None

            data = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            self.size -= 1
            return data

        def peek(self):
            if self.is_empty():
                return None

            return self.front.data

        def is_empty(self):
            return self.front is None

        def get_size(self):
            return self.size

        def to_list(self):
            result = []
            current = self.front

            while current is not None:
                result.append(current.data)
                current = current.next

            return result

        def clear(self):
            self.front = None
            self.rear = None
            self.size = 0


    # ============================================================
    # STACK - PILHA (LIFO)
    # Last In, First Out
    # ============================================================

    class Phase02Stack:

        def __init__(self):
            self.top = None
            self.size = 0

        def push(self, data):
            new_node = Phase02Node(data)
            new_node.next = self.top
            self.top = new_node
            self.size += 1

        def pop(self):
            if self.is_empty():
                return None

            data = self.top.data
            self.top = self.top.next
            self.size -= 1

            return data

        def peek(self):
            if self.is_empty():
                return None

            return self.top.data

        def is_empty(self):
            return self.top is None

        def get_size(self):
            return self.size

        def to_list(self):
            result = []
            current = self.top

            while current is not None:
                result.append(current.data)
                current = current.next

            return result

        def clear(self):
            self.top = None
            self.size = 0


    # ============================================================
    # LINKED LIST - LISTA LIGADA SIMPLES
    # ============================================================

    class Phase02LinkedList:

        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

        def append(self, data):
            new_node = Phase02Node(data)

            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.size += 1

        def insert_at(self, index, data):
            if index < 0 or index > self.size:
                return False

            new_node = Phase02Node(data)

            if index == 0:
                new_node.next = self.head
                self.head = new_node

                if self.tail is None:
                    self.tail = new_node

            elif index == self.size:
                self.tail.next = new_node
                self.tail = new_node

            else:
                current = self.head

                for _ in range(index - 1):
                    current = current.next

                new_node.next = current.next
                current.next = new_node

            self.size += 1
            return True

        def remove_at(self, index):
            if index < 0 or index >= self.size:
                return None

            if index == 0:
                removed = self.head
                self.head = self.head.next

                if self.head is None:
                    self.tail = None

            else:
                previous = self.head

                for _ in range(index - 1):
                    previous = previous.next

                removed = previous.next
                previous.next = removed.next

                if removed == self.tail:
                    self.tail = previous

            self.size -= 1
            return removed.data

        def get_at(self, index):
            if index < 0 or index >= self.size:
                return None

            current = self.head

            for _ in range(index):
                current = current.next

            return current.data

        def find(self, data):
            current = self.head
            index = 0

            while current is not None:
                if current.data == data:
                    return index

                current = current.next
                index += 1

            return -1

        def is_empty(self):
            return self.head is None

        def get_size(self):
            return self.size

        def to_list(self):
            result = []
            current = self.head

            while current is not None:
                result.append(current.data)
                current = current.next

            return result

        def clear(self):
            self.head = None
            self.tail = None
            self.size = 0