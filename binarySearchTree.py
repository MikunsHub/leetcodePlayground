import numbers
from xml.dom.minidom import Element


class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            #add to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        
        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

numbers = [13,4,1,5,23,34]
bin_srch_tree = build_tree(numbers)
print(bin_srch_tree.in_order_traversal())
print(bin_srch_tree.search(100))