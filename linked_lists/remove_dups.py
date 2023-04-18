"""
ASSUMPTIONS:
    1. Singly linked list.
    2. Values in nodes are unsorted.
    3. Each node contains ONLY integers.
    4. Only duplicates occur.

INSIGHTS:

BRUTE FORCE:
    1. Loop through linked list and put values in a hash map.
    2. Use each value as key and their frequency as value.
    3. Loop through hash map and use to find and eleminate dups.

OPTIMIZED SOLUTION:
    1. Loop through multiple times and sort in place
    2. Loop though the sorted linked-list and remove duplicates then.
"""

from linked_list import (
    LinkedList,
)


def brute_force(ll: LinkedList) -> None:
    hash = {}
    tmp = ll
    while tmp != None:
        hash[tmp.val] = hash.get(tmp.val, 0) + 1
        tmp = tmp.next

    for k, v in hash.items():
        if v <= 1:
            continue

        while ll and v != 1:
            if ll.next.val == k:
                ll.next = ll.next.next
                v -= 1
            ll = ll.next


# Study this and try to break it.
def optimized_single_loop(ll: LinkedList) -> None:
    hash_set = set()
    hash_set.add(ll.val)

    while ll:
        if ll.next.val in hash_set:
            ll.next = ll.next.next
        else:
            hash_set.add(ll.next.val)
        ll = ll.next
