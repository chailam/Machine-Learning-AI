"""
author: Loi Chai Lam  (28136179)
modified date: 27/8/2019
"""


class Node:
    """
    Node stated the properties of a Node, which include 
    identifier,  the operator that generated it, order of expansion (if in CLOSED) otherwise 0,  the cost g of reaching that node,  a heuristic value h (0 for DLS),
    a value f, where f = g + h, a pointer to its children and a pointer to its parent (if you implement Treesearch, and your action sequence is included in a node identifier, then this pointer is not necessary)
    """
    def __init__(self, id, operator, orderExpansion, g, h, f, child, parent, posX, posY):
        self.id = id
        self.operator = operator
        self.orderExpansion = orderExpansion
        self.g = g
        self.h = h
        self.f = f
        self.child = []
        self.parent = parent
        self.posX = posX
        self.posY = posY


# All Setter Method
    def setChild(self,childNode):
        self.child.append(childNode)

    def setOrderExpansion(self,order):
        self.orderExpansion = order

    def setG(self,g):
        self.g = g

    def setH(self,h):
        self.h = h

    def setF(self,f):
        self.f = f

    def setParent(self,parentNode):
        self.parent = parentNode



if __name__ == "__main__":
    print("Node Test")
