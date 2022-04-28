# # Reverse the linked list

# class Node:
#     def __init__(self, value, next_node):
#         self.value = value
#         self.next_node = next_node

# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None

#     def add_node(self, value):
#         # Adding initial node
#         if self.head == None:
#             node = Node(value, None)
#             self.head = node
#             self.tail = node
#         else:
#             node = Node(value, self.head)
#             self.head = node
        


#     def traverse(self):
#         if self.head is not None:
#             next = self.head
#             while next:
#                 print(next.value, end = " ")
#                 next = next.next_node

#     def reverse_traverse(self):
#         if self.head is not None:
#             next = self.head
#             while next:
#                 print(next.value, end = " ")
#                 next = next.next_node

# ll = LinkedList()
# ll.add_node(5)
# ll.add_node(7)
# ll.add_node(8)
# ll.add_node(9)
# ll.traverse()

a = [1,2,3,4,5]
k = 6

# mid element
# mid element > k -->left
# mid element < k -->right

def binary_search(a, k):
    len_a = len(a)
    if len_a == 0:
        return "Not Present"
    mid = int(len_a/2)
    mid_term = a[mid]
    if mid_term == k:
        return "Present"
    elif mid_term > k:
        return binary_search(a[0: int(len_a/2)], k)
    elif mid_term < k:
        return binary_search(a[int(len_a/2): len_a], k)

print(binary_search(a, k))


