class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """Add an element to the end of the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Add an element to the beginning of the list (O(1))."""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Insert an element at index idx."""
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        new_node = Node(value)

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        """Remove node at index idx."""
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        current.next = current.next.next
        self._size -= 1

    def get(self, idx):
        """Get value at index idx."""
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def search(self, value):
        """Search for value and return its index, or -1 if not found."""
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def clear(self):
        """Clear the entire list."""
        self.head = None
        self._size = 0

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

    def plotter(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)


# ========== ДЕМОНСТРАЦИЯ РАБОТЫ ==========
if __name__ == "__main__":

    lst = SinglyLinkedList()
    print(f"1. Создан пустой список: {lst}")
    print(f"   Визуализация: {lst.plotter()}")
    print(f"   Длина: {len(lst)}")

    # 2. Добавление в конец (append)
    print("\n2. Добавляем элементы в конец (append):")
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"   После append(10), append(20), append(30):")
    print(f"   {lst}")
    print(f"   Визуализация: {lst.plotter()}")
    print(f"   Длина: {len(lst)}")

    # 3. Добавление в начало (prepend)
    print("\n3. Добавляем элементы в начало (prepend):")
    lst.prepend(5)
    lst.prepend(1)
    print(f"   После prepend(5), prepend(1):")
    print(f"   {lst}")
    print(f"   Визуализация: {lst.plotter()}")
    print(f"   Длина: {len(lst)}")

    # 4. Вставка по индексу (insert)
    print("\n4. Вставка по индексу (insert):")
    lst.insert(2, 15)  # Вставка на позицию 2 (третий элемент)
    lst.insert(4, 25)  # Вставка на позицию 4
    print(f"   После insert(2, 15), insert(4, 25):")
    print(f"   {lst}")
    print(f"   Визуализация: {lst.plotter()}")

    # 5. Получение элементов (get)
    print("\n5. Получение элементов по индексу (get):")
    print(f"   lst.get(0) = {lst.get(0)}")
    print(f"   lst.get(2) = {lst.get(2)}")
    print(f"   lst.get({len(lst) - 1}) = {lst.get(len(lst) - 1)}")

    # 6. Поиск элементов (search)
    print("\n6. Поиск элементов (search):")
    print(f"   search(15) = индекс {lst.search(15)}")
    print(f"   search(99) = {lst.search(99)} (не найден)")

    # 7. Итерация по списку
    print("\n7. Итерация по списку (for loop):")
    print("   Элементы:", end=" ")
    for item in lst:
        print(item, end=" ")
    print()

    # 8. Удаление элементов
    print("\n8. Удаление элементов (remove_at):")
    print(f"   До удаления: {lst.plotter()}")
    lst.remove_at(2)  # Удаляем элемент с индексом 2 (15)
    print(f"   После remove_at(2): {lst.plotter()}")
    lst.remove_at(0)  # Удаляем первый элемент (1)
    print(f"   После remove_at(0): {lst.plotter()}")
    print(f"   Длина после удалений: {len(lst)}")

    # 9. Очистка списка
    print("\n9. Очистка списка (clear):")
    lst.clear()
    print(f"   После clear: {lst}")
    print(f"   Визуализация: {lst.plotter()}")
    print(f"   Длина: {len(lst)}")
