
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        

    def insert_at_begining(self, data):
            node = Node(data, self.head)
            self.head = node 

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next

        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    
    def insert_values(self,data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head =self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
        
    def search_list(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return count
            itr = itr.next
            count += 1
        return count

    def insert_after_value(self,data_after,data_to_insert):
        data_after_index = self.search_list(data_after)
        self.insert_at(data_after_index+1,data_to_insert)
    
    def remove_by_value(self,data):
        data_index = self.search_list(data)
        self.remove_at(data_index)

    def reverse_ll(self):
        prev,curr = None, self.head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # print(curr.data,prev.data)
        return prev.data
ll = LinkedList()
ll.insert_values(["banana","oat","chocolate","avocado"])
ll.print()

print("Length = ",ll.get_length())

ll.remove_at(2)
ll.print()

ll.insert_at(1,"grapes")
ll.insert_at(2,"strawberry")
ll.print()

print(ll.search_list("strawberry"))

ll.insert_after_value("strawberry","youghurt")
ll.print()

ll.remove_by_value("strawberry")
ll.print()
        
print('stop')    
ll.reverse_ll()
ll.print()
