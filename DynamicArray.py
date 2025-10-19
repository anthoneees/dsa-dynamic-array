import ctypes   

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if index >= 0 and  index < self._n:
            return self._array[index]
        else: 
            raise IndexError("index out of bounds")

    def append(self, element):
        if self._n == self._capacity:
            self._resize(self._capacity * 2)

        self._array[self._n] = element

        self._n += 1

    def _resize(self, new_capacity):
        temp = self._make_array(new_capacity)
        for i in range(len(self._array)):
            temp[i] = self[i]

        self._array = temp
        self._capacity = new_capacity

    def insert(self, index, value):
        if index < 0 or  index >self._n:
            raise IndexError('index out of bounds')

        if self._n == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._n ,index, -1):
            self._array[i] = self._array[i-1]

        self._array[index] = value
        self._n += 1

    def delete(self, index):
        if index < 0 or  index >=self._n:
            raise IndexError('index out of bounds')

        for i in range(index, self._n-1):
            self._array[i] = self._array[i + 1]
        self._n -= 1

    def remove(self):
        self._array[self._n -1] = None
        self._n -= 1

    def __setitem__(self, index, value):
        if index < 0 or  index >=self._n:
            raise IndexError('index out of bounds')
        self._array[index] = value
