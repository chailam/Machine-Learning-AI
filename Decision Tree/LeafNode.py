"""
Author: Chai Lam Loi
Date: 25/10/2019
Aim: Implement a Learning Decision Tree. This is the decision node with only attribute value (0/1).
"""

class LeafNode:
    """
    A decision node with only attribute value (0/1).
    """

    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        string = "Result: " + str(self.attribute) + "  "
        return string

        
if __name__ == "__main__":
    pass