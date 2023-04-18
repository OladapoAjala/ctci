from linked_list import (
    LinkedList,
)


def test_linked_list():
    llist = LinkedList("node one")
    assert llist.val == "node one"
    llist = llist.next
    assert llist == None


def test_linked_list_add():
    llist = LinkedList(2)
    llist.add(2)
    llist.add("string node 3")

    assert llist.val == 2
    llist = llist.next
    assert llist.val == 2
    llist = llist.next
    assert llist.val == "string node 3"
    llist = llist.next
    assert llist == None


def test_linked_list_remove():
    llist = LinkedList("node_one")
    llist.add("node_two")
    llist.add("node_three")

    assert llist.val == "node_one"
    assert llist.next.val == "node_two"
    assert llist.next.next.val == "node_three"

    llist.remove("node_two")
    assert llist.val == "node_one"
    assert llist.next.val == "node_three"

    llist.remove("node_three")
    assert llist.val == "node_one"
    assert llist.next == None
