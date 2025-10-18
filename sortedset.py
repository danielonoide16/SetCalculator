import bisect

class SortedSet:

    def __init__(self, otherSortedSet = None):
        if otherSortedSet is not None:
            self.elements = otherSortedSet.elements.copy()
            return
        
        self.elements = []


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


    def is_proper_sub_set(self, other): #check if other is a proper subset of self
        return self.is_sub_set(other) and not self.equals(other)


    def __str__(self):
        return " ".join(str(x) for x in self.elements)



#example
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



#menu example
# sets = dict()

# while True:
#     print("\n==== SORTED SET MENU ====")
#     print("1. Create a New Set")
#     print("2. Add element to a set")
#     print("3. Remove an element from a set")
#     print("4. Perform an operation between two sets")
#     print("5. View a set")
#     print("6. Exit")

#     option = input("Select an option: ")

#     if option == "1":
#         name = input("Enter the set's name: ")
#         if name in sets:
#             print("Set already exists.")
#         else:
#             sets[name] = SortedSet()
#             print(f"Set '{name}' created successfully.")

#     elif option == "2":
#         name = input("Enter the set's name: ")
#         if name not in sets:
#             print("Unknown set.")
#         else:
#             element = input("Enter the element to add: ")
#             sets[name].add(element)
#             print("Element added successfully.")

#     elif option == "3":
#         name = input("Enter the set's name: ")
#         if name not in sets:
#             print("Unknown set.")
#         else:
#             element = input("Enter the element to remove: ")
#             try:
#                 sets[name].remove(element)
#                 print("Element removed successfully.")
#             except ValueError as e:
#                 print(e)

#     elif option == "4":
#         print("\nSelect the operation:")
#         print("1. Union")
#         print("2. Intersection")
#         print("3. Difference")
#         print("4. Symmetric Difference")
#         print("5. Check if A is subset of B")
#         print("6. Check if A is proper subset of B")

#         operation = input("Select operation: ")

#         a = input("Enter the first set name (A): ")
#         b = input("Enter the second set name (B): ")

#         if a not in sets or b not in sets:
#             print("One or both sets were not found.")
#             continue

#         A, B = sets[a], sets[b]

#         if operation == "1":
#             print("Union:", A.union(B))
#         elif operation == "2":
#             print("Intersection:", A.intersection(B))
#         elif operation == "3":
#             print("Difference (A - B):", A.difference(B))
#         elif operation == "4":
#             print("Symmetric Difference:", A.sym_difference(B))
#         elif operation == "5":
#             print("A is subset of B:", A.is_sub_set(B))
#         elif operation == "6":
#             print("A is proper subset of B:", A.is_proper_sub_set(B))
#         else:
#             print("Invalid option.")

#     elif option == "5":
#         name = input("Enter the set's name: ")
#         if name not in sets:
#             print("Unknown set.")
#         else:
#             print(f"{name} = {sets[name]}")

#     elif option == "6":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid option.")