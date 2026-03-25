from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    
    values = list_repr.split(" -> ")
    
    head = None
    
    for value in reversed(values[:-1]):
        head = Node(int(value), head)
    
    return head
