from typing import Any, Optional, Iterator
import ctypes


class DynamicArray(object):
    """Creates a dynaimc array using fixed size C arrays abstractly"""
    def __init__(self, initial_capacity: int = 1) -> None:
        if initial_capacity < 1:
            raise ValueError("Initial Capacity must be atleast 1")
        
        self._size: int = 0
        self._capacity: int = 1
        self._ctypes: ctypes.Array = self._make_array(self._capacity)
        
    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, index: int) -> Any:
        index = self._validate_and_normalize_index(index)
        return self._array(index)
    
    def __setitem__(self, index: int, value: Any) -> None:
        index = self._validate_and_normalize_index(index)
        self._array(index) = value
        
    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self._array[i]
            
    def __repr__(self) -> str:
        elements =",".join(repr(self._array[i])) for i in range(self._size)
        return f"DynamicArray([{elements}])"
    
    @property
    # Capacity, pop, insert, append, _resize, _make_array, _validate_and_normalize_index
    def capacity(self) -> int:
        return self._capacity
    
    def pop(self, index: Optional[int] = None) -> Any:
        
        
        
            