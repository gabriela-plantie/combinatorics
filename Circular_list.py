from itertools import combinations, permutations
import math
from collections import deque #“double-ended queue”)

#receives a list of elements and creates diferent circular lists 
#if shifting the object the same configuration is obtained, then it is considered the same circular list

class Circular_list:
    
    __instances = 0
    
    def __init__(self, data):
        self.data = list(data)
        self.__class__.__instances += 1
        
    def __eq__(self, other):
        if not isinstance(other, Circular_list):
            return False

        if self.data == other.data:
            return True
        else:
            shift = deque(self.data)
            for i in range(len(self.data)):
                shift.rotate(1)
                if list(shift) == other.data:
                    return True    
            return False
    
    def __hash__(self):
        return len(self.data)
    
    def __repr__(self):
        return self.data.__repr__()
    
    def __str__(self):
        return self.data.__str__()
    
    
    @classmethod
    def create_distincts_circular_lists(cls, data):
        perms = set(permutations(data))
        distincts = set() 
        for i in perms:
            distincts.add(cls(i))
        return distincts
    
    
