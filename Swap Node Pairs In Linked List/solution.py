from preloaded import Node

def swap_pairs(head):

    if not head:
        return head
    if not head.next:
        return head

    first = head
    second = head.next

    first.next = swap_pairs(second.next)

    second.next = first

    return second
