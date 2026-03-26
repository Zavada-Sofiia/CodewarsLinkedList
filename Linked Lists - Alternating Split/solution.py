class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):

    first = head
    second = head.next

    first_first = first
    second_second = second
    
    if not head:
        raise ValueError
    if not head.next:
        raise ValueError

    while second and second.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next

    first.next = None

    return Context(first_first, second_second)
