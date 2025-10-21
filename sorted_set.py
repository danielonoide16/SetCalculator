import bisect

#clase que define un set ordenado (los elementos no se repiten)
class SortedSet:

    def __init__(self, iterable = None):
        self.elements = []

        if iterable is None:
            return
        
        if isinstance(iterable, SortedSet):
            self.elements = iterable.elements.copy()
            return
        
        for item in iterable:
            self.add(item)
        

    def add(self, element):
        pos = bisect.bisect_left(self.elements, element)

        if pos == len(self.elements) or self.elements[pos] != element:
            self.elements.insert(pos, element)
        
    
    def contains(self, element):
        return element in self.elements
    

    def remove(self, element):
        self.elements.remove(element)
        

    def union(self, hs):

        lists = self.elements + hs.elements
        res = SortedSet()

        for i in lists:
            res.add(i)

        return res
    
    def intersection(self, other):
        result = SortedSet()
        result.elements = [x for x in self.elements if x in other.elements]
        return result
    

    def difference(self, other):
        result = SortedSet()
        result.elements = [x for x in self.elements if x not in other.elements]

        return result
    
    def sym_difference(self, other):
        inter = self.intersection(other)
        result = SortedSet()
        result.elements = [x for x in self.union(other).elements if x not in inter.elements]

        return result
    
    def complement(self, universe):
        return universe.difference(self)


    def is_sub_set(self, other): #check if self is a subset of other
        for x in self.elements:
            if x not in other.elements:
                return False
            
        return True

    def equals(self, other):
        return self.elements == other.elements


    def is_proper_sub_set(self, other): #check if self is a proper subset of other
        return self.is_sub_set(other) and not self.equals(other)
    
    def size(self) -> int:
        return len(self.elements)

    def __str__(self): #convierte a string
        result = "{"
        result += ", ".join(str(x) for x in self.elements)
        result += "}"
        return result



#use example
if __name__ == "__main__":
    setA = SortedSet()
    setA.add(1)
    setA.add(2)
    setA.add(3)
    setA.add(4)

    setB = SortedSet()
    setB.add(3)
    setB.add(4)
    setB.add(5)
    setB.add(6)
    setB.add(7)

    universe = setA.union(setB)

    print("Set A: ", setA)
    print("Set B: ", setB)
    print("Universe: ", universe)

    print("Union: ", setA.union(setB))
    print("Intersection: ", setA.intersection(setB))
    print("A - B: ", setA.difference(setB))
    print("B - A: ", setB.difference(setA))
    print("A Δ B: ", setA.sym_difference(setB))
    print("is A a subset of B? ", setA.is_sub_set(setB))
    print("is A a proper subset of B? ", setA.is_proper_sub_set(setB))
    print("is B a subset of A? ", setB.is_sub_set(setA))
    print("is B a proper subset of A? ", setB.is_proper_sub_set(setA))
    print("A's complement: ", setA.complement(universe))
    print("B's complement: ", setB.complement(universe))

