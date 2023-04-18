from linked_list import (
    LinkedList,
)

from remove_dups import (
    brute_force,
    optimized_single_loop,
)


def test_brute_force():
    simple_list = LinkedList("node_one")
    simple_list.add("node_two")
    simple_list.add("node_three")
    simple_list.add("node_one")

    brute_force(simple_list)
    assert simple_list.val == "node_one"
    simple_list = simple_list.next
    assert simple_list.val == "node_two"
    simple_list = simple_list.next
    assert simple_list.val == "node_three"
    simple_list = simple_list.next
    assert simple_list == None


def test_optimized_single_loop():
    simple_list = LinkedList("node_one")
    simple_list.add("node_two")
    simple_list.add("node_three")
    simple_list.add("node_one")

    optimized_single_loop(simple_list)
    assert simple_list.val == "node_one"
    simple_list = simple_list.next
    assert simple_list.val == "node_two"
    simple_list = simple_list.next
    assert simple_list.val == "node_three"
    simple_list = simple_list.next
    assert simple_list == None
