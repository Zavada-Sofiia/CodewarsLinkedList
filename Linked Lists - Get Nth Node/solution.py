from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    i = 0
    while node and i < index:
        node = node.next
        i += 1
        
    if i < index:
        raise IndexError
        
    if index < 0:
        raise IndexError
        
    if node == None:
        raise IndexError
        
    return node
  
