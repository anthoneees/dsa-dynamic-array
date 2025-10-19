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

arr = DynamicArray()
print("Initial length:", len(arr))
print("Initial capacity:", arr._capacity)

# --- Append test ---
print("\nAppending elements 0–9:")
for i in range(10):
    arr.append(i)
    print(f"Appended {i}, length={len(arr)}, capacity={arr._capacity}")
print("Contents:", [arr[i] for i in range(len(arr))])

# --- Insert test ---
print("\nInserting 99 at index 5:")
arr.insert(5, 99)
print("Length:", len(arr))
print("Contents:", [arr[i] for i in range(len(arr))])

print("\nInserting 77 at index 0 (front):")
arr.insert(0, 77)
print("Length:", len(arr))
print("Contents:", [arr[i] for i in range(len(arr))])

print("\nInserting 123 at the end (index len-1):")
arr.insert(len(arr), 123)
print("Length:", len(arr))
print("Contents:", [arr[i] for i in range(len(arr))])

# --- Setitem test ---
print("\nSetting index 3 to 555:")
arr[3] = 555
print("Contents:", [arr[i] for i in range(len(arr))])

# --- Delete test ---
print("\nDeleting index 5:")
arr.delete(5)
print("Length:", len(arr))
print("Contents:", [arr[i] for i in range(len(arr))])

# --- Remove (pop last) test ---
print("\nRemoving last element:")
arr.remove()
print("Length:", len(arr))
print("Contents:", [arr[i] for i in range(len(arr))])

# --- Resize test ---
print("\nAppending more elements to force resizes:")
for i in range(10, 50):
    arr.append(i)
print("Length:", len(arr))
print("Capacity:", arr._capacity)
print("Last 10 elements:", [arr[i] for i in range(len(arr)-10, len(arr))])

# --- Out of bounds tests ---
print("\nTesting out-of-bounds operations:")
try:
    arr.insert(-1, 5)
except IndexError as e:
    print("Insert error caught:", e)

try:
    arr.delete(999)
except IndexError as e:
    print("Delete error caught:", e)

try:
    arr[999]
except IndexError as e:
    print("Get item error caught:", e)
