from typing import Any, Optional, Iterator
import ctypes


class DynamicArray(object):
    """Creates a dynaimc array using fixed size C arrays abstractly"""
    def __init__(self, initial_capacity: int = 1) -> None:
        if initial_capacity < 1:
            raise ValueError("Initial Capacity must be atleast 1")
        
        self._size: int = 0
        self._capacity: int = 1
        self._array: ctypes.Array = self._make_array(self._capacity)
        
    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, index: int) -> Any:
        index = self._validate_and_normalize_index(index)
        return self._array[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        index = self._validate_and_normalize_index(index)
        self._array[index] = value
        
    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self._array[i]
            
    def __repr__(self) -> str:
        elements =",".join(repr(self._array[i]) for i in range(self._size))
        return f"DynamicArray([{elements}])"
    
    @property
    # Capacity, pop, insert, append
    def capacity(self) -> int:
        return self._capacity
    
    def pop(self, index: Optional[int] = None) -> Any:
        if self._size == 0:
            raise IndexError("pop from empty DynamicError")
        
        if index is None:
            index = self._size-1
        else:
            index=self._validate_and_normalize_index(index)
            
        item = self._array[index]
        
        # Shift elements to left
        for i in range(self._size):
            self._array[i] = self._array[i+1]
            
        self._array[self._size-1] = None
        # Shrink capacity if array is 1/4 full to prevent thrashing
        if 0 < self._size <= self._capacity // 4 and self._capacity //2 >1:
            self._resize(self._capacity // 2)
            
        return item
    def insert(self, item: Any, index: int) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
            
        if index > self._size:
            index = self._size
        elif index < 0:
            index = max(0, self._size+index)
            
        # shift elements to the right
        for i in range(self._size):
            self._array[i] = self._array[i-1]
            
        self._array[index] = item
        self._size += 1
        
    def append(self, item: Any) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
            
        self._array[self._size] = item
        self._size += 1
        
    def _resize(self, new_capacity: int) -> None:
        new_array = self._make_array(new_capacity)
        for i in range(new_capacity):
            new_array[i] = self._array[i]
            
        self._capacity = new_capacity
        self._array = new_array
        
    def _make_array(self, capacity: int) -> ctypes.Array:
        return (capacity * ctypes.py_object)()
    
    def _validate_and_normalize_index(self, index: int) -> int:
        if index < 0:
            index += self._size
            
        if not (0<= index < self._size):
            raise IndexError("INdex out of bounds")

        return index        
            
        
                
        
        
        
            