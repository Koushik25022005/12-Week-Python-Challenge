from __future__ import annotations

from typing import Sequence, Optional, Sequence, Tuple, List

from ._types import Comparable, Item

"""List of all the algorithms used in array and matrix operations"""

def two_sum_sorted(num: Sequence[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices ``(i, j)``, ``i < j``, with sum equal to ``target``.

    ``nums`` must be sorted ascending. Time O(n), space O(1).
    """
    left, right = 0, len(num) - 1
    while left < right:
        target_sum = num[left] + num[right]
        if target_sum == target:
            return left, right
        elif target_sum < target:
            left += 1
        else:
            right -= 1
    return None

def remove_duplicate_sorted(nums: List[Item]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        nums[read] = nums[write-1]
        nums[write] = nums[read]
        write += 1
    return write

def merge_sorted(a: Sequence[Comparable], b: Sequence[Comparable]) -> List[Comparable]:
    out: List[Comparable] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if b[j] < a[i]:
            out.append(b[j])
            j += 1
        else:
            out.append(a[i])
            i += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out

def intersect_sorted(a: Sequence[Comparable], b: Sequence[Comparable]) -> List[Comparable]:
    out: List[Comparable] = []
    i = j = 0;
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            out.append(a[i])
            i += 1
            j += 1
    return out
    