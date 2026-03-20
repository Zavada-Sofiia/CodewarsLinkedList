"""
Convert a linked list to a string
"""
def stringify(node):
    values = []
    current = node
    while current:
        values.append(str(current.data))
        current = current.next
        
    values.append(str(None))
    
    return " -> ".join(values)
