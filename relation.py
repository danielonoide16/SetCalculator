from sorted_set import SortedSet

class Relation:

    def __init__(self, pairs, domain, codomain): #all sorted sets
        self.pairs = pairs
        self.domain = domain
        self.codomain = codomain


    #FUNCIONES
    def isfunction(self) -> bool:
        """
        Cada elemento del dominio tiene a lo mucho un valor asociado en el codominio
        """
        mapping = dict()
        for x, y in self.pairs.elements:
            if x in mapping and mapping[x] != y:
                return False
            mapping[x] = y

        if len(mapping) != self.domain.size(): #todos los elementos del dominio deben de usarse
            return False
        
        return True


    def isinjective(self) -> bool:
        """Una función es inyectiva si no hay dos elementos del dominio que tengan la misma imagen"""
        if not self.isfunction():
            return False
        
        images = {}
        for x, y in self.pairs.elements:
            if y in images:
                return False
            images[y] = x
        return True


    def issurjective(self) -> bool:
        """Una función es sobreyectiva si su imagen cubre todo el codominio"""
        if not self.isfunction():
            return False

        image = SortedSet()
        for x, y in self.pairs.elements:
            image.add(y)
        return image.equals(self.codomain)# or image.is_sub_set(self.codomain)


    def isbijective(self) -> bool:
        """Una función es biyectiva si es inyectiva y sobreyectiva"""
        return self.isinjective() and self.issurjective()
    

    #RELACIONEs

    def isreflexive(self) -> bool:
        """Una relación es reflexiva si todo elemento del dominio está relacionado consigo mismo"""
        for x in self.domain.elements:
            if not self.pairs.contains((x,x)):
                return False
        return True

    def issymmetric(self) -> bool:
        """Una relación es simétrica si (x,y) implica (y,x)"""
        for x, y in self.pairs.elements:
            if not self.pairs.contains((y,x)) :
                return False
        return True

    def istransitive(self) -> bool:
        """Una relación es transitiva si (x,y) y (y,z) implica (x,z)"""
        for x, y in self.pairs.elements:
            for a, z in self.pairs.elements:
                if a == y and not self.pairs.contains((x,z)):
                    return False
        return True