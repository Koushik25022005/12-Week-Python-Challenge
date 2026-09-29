import pytest
from arrays import DynamicArray

def test_initialization() -> None:
    array = DynamicArray(initial_capacity=4)
    assert len(array) == 0
    assert array.capacity == 4
    assert repr(array) == "DynamicArray([])"
    
def test_invalid_initialization() -> None:
    with pytest.raises(ValueError):
        assert DynamicArray(initial_capacity=0)
        
def test_append_and_auto_resize() -> None:
    arr = DynamicArray(initial_capacity=2)
    assert arr.capacity == 2

    arr.append(10)
    arr.append(20)
    assert len(arr) == 2
    assert arr.capacity == 2

    # Triggers automatic doubling of capacity
    arr.append(30)
    assert len(arr) == 3
    assert arr.capacity == 4
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30


def test_indexing_and_setitem() -> None:
    arr = DynamicArray()
    arr.append("A")
    arr.append("B")
    arr.append("C")

    # Positive and negative index reading
    assert arr[0] == "A"
    assert arr[-1] == "C"
    assert arr[-2] == "B"

    # Index assignment
    arr[1] = "Z"
    assert arr[1] == "Z"


def test_index_out_of_bounds() -> None:
    arr = DynamicArray()
    arr.append(1)

    with pytest.raises(IndexError):
        _ = arr[5]

    with pytest.raises(IndexError):
        _ = arr[-5]


def test_pop_last() -> None:
    arr = DynamicArray(initial_capacity=4)
    for i in range(4):
        arr.append(i * 10)

    popped = arr.pop()
    assert popped == 30
    assert len(arr) == 3


def test_pop_intermediate_and_auto_shrink() -> None:
    arr = DynamicArray(initial_capacity=8)
    for i in range(8):
        arr.append(i)

    # Remove elements to force capacity reduction (down to 1/4 capacity)
    arr.pop(0)  # Removes 0
    arr.pop(0)  # Removes 1
    arr.pop(0)  # Removes 2
    arr.pop(0)  # Removes 3
    arr.pop(0)  # Removes 4
    arr.pop(0)  # Removes 5

    assert len(arr) == 2
    assert arr.capacity == 4  # Capacity halved from 8 to 4
    assert arr[0] == 6
    assert arr[1] == 7


def test_pop_empty() -> None:
    arr = DynamicArray()
    with pytest.raises(IndexError):
        arr.pop()


def test_insert() -> None:
    arr = DynamicArray()
    arr.append(1)
    arr.append(3)

    arr.insert(1, 2)  # Insert in the middle
    assert list(arr) == [1, 2, 3]

    arr.insert(0, 0)  # Insert at head
    assert list(arr) == [0, 1, 2, 3]

    arr.insert(10, 4)  # Insert out of upper bounds -> appends at tail
    assert list(arr) == [0, 1, 2, 3, 4]


def test_iteration() -> None:
    arr = DynamicArray()
    values = [100, 200, 300]
    for v in values:
        arr.append(v)

    assert [x for x in arr] == values