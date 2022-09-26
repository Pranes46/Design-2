class MyHashMap:
    
    class Listnode:
        def __init__(self,key,val):
            self.key = key   #assigning for key in hashmap
            self.val = val   #assigning for val in hashmap
            self.next = None  # assigning the next node as none
                
                

    def __init__(self):
        self.hashmap=[None]*10000
        
    def hashindex(self,key):
        return key%10000   #to find the index to store the key and val
    
    def findnode (self,head,key):
        
        curr = head  # setting the current as head 
        prev = None  #setting none
        while curr!=None and curr.key !=key:  #if the current is not equal to none and current.key is not equal to key
            prev = curr   #prev is the current node
            curr = curr.next  # current is the next node
            
        return prev #returning prev
        
    def put(self, key: int, value: int) -> None:
        
        hash_index = self.hashindex(key)
        if self.hashmap[hash_index] == None:
            self.hashmap[hash_index] = self.Listnode(-1,-1) # creating a dummy node
        prev = self.findnode(self.hashmap[hash_index],key)
        
        if prev.next == None:
            prev.next = self.Listnode(key,value)
        else:
            prev.next.val = value
            

    def get(self, key: int) -> int:
        hash_index = self.hashindex(key)
        prev = self.findnode(self.hashmap[hash_index],key)
        if self.hashmap[hash_index] == None:
            return -1
        else:
            if prev.next == None:
                return -1
            
            else:
                return prev.next.val
    

    def remove(self, key: int) -> None:
        hash_index = self.hashindex(key)
       
        if self.hashmap[hash_index] == None:
            return None
        
        prev = self.findnode(self.hashmap[hash_index],key)
            
        if prev.next == None:
            return -1
            
        else:
            prev.next =  prev.next.next
        
        
        
        
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)