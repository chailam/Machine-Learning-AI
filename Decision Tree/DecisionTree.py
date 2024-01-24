"""
Author: Chai Lam Loi
Date: 25/10/2019
Aim: Implement a Learning Decision Tree. This is the base decision tree
"""

class DecisionTree:
    """
    A decision Tree which hold the attribute and list of branches.
    """

    def __init__(self, attribute):
        self.branches = []
        self.attribute = attribute  # Since the data provided without the attributes name,
        # I will use attribute index in the attributes matrix as name

    def add(self, valueToBranch, subtree):
        """
        Add the node to the tree with the decision value to the branch and the subtree.
        """
        self.branches.append((valueToBranch,subtree))

    def __str__(self):
       """
       Modify str function to print the DecisionTree.
       """
       branchV = ""
       for j in range(len(self.branches)):
          branchV += "<attrAttached " + str(self.attribute) + "; LabelBranch: " + str(self.branches[j][0]) + ">, subtree: " + str(self.branches[j][1])
       string = "(Attr: " + str(self.attribute) + ", Branches: " + branchV + " ) "
       return string

if __name__ == "__main__":
    pass

