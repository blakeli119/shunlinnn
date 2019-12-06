from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def MD5(self, key): 
        h = MD5.new()
        h.update(key.encode('utf-8'))
        return int(h.hexdigest(), 16)
    
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        md5_num = self.MD5(key)
        num = md5_num % self.capacity
        
        if self.data[num] == None:
            self.data[num] = key
        else:
            if type(self.data[num]) == list:
                self.data[num].append(key)
            else:
                self.data[num] = [self.data[num], key]
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        md5_num = self.MD5(key)
        num = md5_num % self.capacity
        
        if self.data[num] != None:
            if type(self.data[num]) == list:
                i = self.data[num].index(key)
                self.data[num][i] = None
            else:
                self.data[num] = None
        else:
            KeyError()
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        md5_num = self.MD5(key)
        num = md5_num % self.capacity
        
        if type(self.data[num]) == list:
            find = key in self.data[num]
        else:
            find = self.data[num] == key
        return find
