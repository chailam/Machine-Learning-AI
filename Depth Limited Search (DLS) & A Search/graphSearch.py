"""
author: Loi Chai Lam  (28136179)
modified date: 27/8/2019
"""

from node import *
import copy
import math

class graphSearch:
    """
    Implement graph search algorithm for DLS and A/A*.
    """
    # Declaring class variable
    isPath = "R"
    noPath = "X"
    goal = "G"
    start = "S"
    formalCost = 2
    diagCost = 1


    def __init__(self, mapSize, theMap, flag, algo):
        self.algo = algo # The algorithm selected: A or DLS, option: A, D
        self.mapSize = int(mapSize)
        self.theMap = theMap
        self.flag = flag
        self.orderExpansion = 1
        self.closed = []
        self.open = [] # FOR A, the list OPEN is sorted in descending order of merit f
        self.graph = []
        self.nodeCount = 0; # For node identifier purpose
        self.flagCounter = 0
        self.startNode = self.findStartNode()
        



    def findStartNode(self):
        """
        To find the start point in the map.
        """
        for i in range(len(self.theMap)):
            for j in range(len(self.theMap[i])):
                if self.theMap[i][j] == graphSearch.start:
                    if self.algo == "D":
                        newNode = Node(("N"+str(self.nodeCount)), "S", 0, 0, 0, 0, None, None, i, j)
                    elif self.algo == "A":
                        hValue = self.hFunction(i,j)
                        newNode = Node(("N"+str(self.nodeCount)), "S", 0, 0, hValue, 0+hValue, None, None, i, j)
                    self.nodeCount += 1
                    return newNode



    def findGoalPoint(self):
        """
        Find the x and y position of the goal point. 
        Used for H function calculation.
        """
        for i in range(len(self.theMap)):
            for j in range(len(self.theMap[i])):
                if self.theMap[i][j] == graphSearch.goal:
                    return (i,j)

        
    
    def checkValid(self, posX, posY):
        """
        To check to validity of a point in map.
        """
        if (posX >= 0) & (posX < self.mapSize) & (posY >= 0) & (posY < self.mapSize): 
            return True
        return False


    
    def expandChild(self,curPosX, curPosY, parentNode):
        """
        Check for available move from current position.
        The sequence of move is Left, Right, Up, Down, LeftUp, LeftDown, RightUp, RightDown.
        Notes: Since the map is a matrix,
        Left= x, y-1; Right= x, y+1; Up= x-1, y; Down=x+1, y;
        LeftUp= x-1, y-1; LeftDown= x+1 ,y-1; RightUp= x-1, y+1; RightDown= x+1, y+1
        """
        posibleDirection = [] # consider put in list or create a node
        # Check the availability of direction
        flagL = True
        flagR = True
        flagU = True
        flagD = True

        # Check for Left Child
        if self.checkValid(curPosX, curPosY-1):  
            if self.theMap[curPosX][curPosY-1] == graphSearch.noPath:
                flagL = False
            else:
                self.nodeGenerateDecision((parentNode.operator+"-L"), parentNode, curPosX, ((curPosY-1)), graphSearch.formalCost)
                posibleDirection.append("L-")


        # Check for Right Child
        if self.checkValid(curPosX, curPosY+1):    
            if self.theMap[curPosX][curPosY+1] == graphSearch.noPath:
                flagR = False
            else:
                self.nodeGenerateDecision((parentNode.operator+"-R"), parentNode, curPosX, ((curPosY+1)), graphSearch.formalCost)
                posibleDirection.append("R-")

        # Check for Up Child
        if self.checkValid(curPosX-1, curPosY):    
            if self.theMap[curPosX-1][curPosY] == graphSearch.noPath:
                flagU = False
            else:
                self.nodeGenerateDecision((parentNode.operator+"-U"), parentNode, (curPosX-1), curPosY, graphSearch.formalCost)
                posibleDirection.append("U-")

        # Check for Down Child
        if self.checkValid(curPosX+1, curPosY):     
            if self.theMap[curPosX+1][curPosY] == graphSearch.noPath:
                flagD = False
            else:
                self.nodeGenerateDecision((parentNode.operator+"-D"), parentNode, (curPosX+1), curPosY, graphSearch.formalCost)
                posibleDirection.append("D-")

        # Check for LeftUp Child
        if self.checkValid(curPosX-1, curPosY-1):     
            if flagL == False or flagU == False or (self.theMap[curPosX-1][curPosY-1] == graphSearch.noPath):
                pass
            else:
                self.nodeGenerateDecision((parentNode.operator+"-LU"), parentNode, (curPosX-1), (curPosY-1), graphSearch.diagCost)
                posibleDirection.append("LU-")

        # Check for LeftDown Child
        if self.checkValid(curPosX+1, curPosY-1):    
            if flagL == False or flagD == False or (self.theMap[curPosX+1][curPosY-1] == graphSearch.noPath):
                pass
            else:
                self.nodeGenerateDecision((parentNode.operator+"-LD"), parentNode, (curPosX+1), (curPosY-1), graphSearch.diagCost)
                posibleDirection.append("LD-")

        # Check for RightUp Child
        if self.checkValid(curPosX-1, curPosY+1):     
            if flagR == False or flagU == False or (self.theMap[curPosX-1][curPosY+1] == graphSearch.noPath):
                pass
            else:
                self.nodeGenerateDecision((parentNode.operator+"-RU"), parentNode, (curPosX-1), (curPosY+1), graphSearch.diagCost)
                posibleDirection.append("RU-")

        # Check for RightDown Child
        if self.checkValid(curPosX+1, curPosY+1):     
            if flagR == False or flagD == False or (self.theMap[curPosX+1][curPosY+1] == graphSearch.noPath):
                pass
            else:
                self.nodeGenerateDecision((parentNode.operator+"-RD"), parentNode, (curPosX+1), (curPosY+1), graphSearch.diagCost)
                posibleDirection.append("RD-")
        
        # Diagnostic Mode
        self.diagnosticMode(parentNode)
        
        return posibleDirection



    def diagnosticMode(self,parentNode):
        """
        The diagnostic mode to output the solution.
        """
        if self.flagCounter < self.flag:
            print(parentNode.id + ":" + self.theMap[parentNode.posX][parentNode.posY] + "\t" + str(parentNode.orderExpansion) + " " + str(parentNode.g) + " " + str(parentNode.h) + " " + str(parentNode.f))
            print("Children: " )
            for p in parentNode.child:
                print(p.id + ":"+p.operator + "\t")

            print("Open: " )
            for p in self.open:
                if p.parent != None:
                    pID = p.parent.id # parent id
                else:
                    pID = None
                print(p.id + ":"+p.operator + " " + str(p.g) + " " + str(p.h) + " " + str(p.f) + " parentID: " + str(pID) + "\t")

            print("Closed: " )
            for p in self.closed:
                if p.parent != None:
                    pID = p.parent.id # parent id
                else:
                    pID = None
                print(p.id + ":"+p.operator + " " + str(p.orderExpansion) + " " + str(p.g) + " " + str(p.h) + " " + str(p.f) + " parentID: " + str(pID)+ "\t")
            print("------------------------------------------------------------------------------------------------------------------------")

            self.flagCounter += 1     
        


    def checkAncestor(self, posX, posY):
        """
        Search whether the node is generated before, by searching all nodes in open and closed.
        Since position in map is unique, it is used to check the generation of node.
        """
        for aNode in self.open:
            if (aNode.posX == posX) and (aNode.posY == posY):
                return ("inOpen", aNode)
        for aNode in self.closed:
            if (aNode.posX == posX) and (aNode.posY == posY):
                return ("inClosed", aNode)
        return ("notGenerated", None)



    def nodeGenerateDecision(self, operation, parentNode, curPosX, curPosY, cost):
        """
        Decide whether generate a new node or redirect the existing pointer.
        If node not ancestors of n, it will generate new node;
        if it is ancestor, it will redirect the pointer depends on situation.
        """
        goalX, goalY = self.findGoalPoint()
        newNode = None
        result = self.checkAncestor(curPosX,curPosY)
        if (result[0] == "notGenerated") & (self.algo == "D"):
            # Node generation for DLS
            # For DLS, h = 0, g = cost + previous g, f = g + h 

            # if it is goal node
            if ((curPosX == goalX) & (curPosY == goalY)):
                 newNode = Node("G", operation, 0, cost+parentNode.g, 0, cost+parentNode.g+0, None, parentNode, curPosX, curPosY)
            else:
                newNode = Node(("N"+str(self.nodeCount)), operation, 0, cost+parentNode.g, 0, cost+parentNode.g+0, None, parentNode, curPosX, curPosY)
            parentNode.setChild(newNode)
            self.nodeCount += 1
            self.graph.append(newNode)
            self.open.append(newNode)

        elif (result[0] == "notGenerated") & (self.algo == "A"):
            # Node generation for A / A*
            hValue = self.hFunction(curPosX, curPosY)
            # if it is goal node
            if ((curPosX == goalX) & (curPosY == goalY)):
                newNode = Node("G", operation, 0, cost+parentNode.g, hValue, hValue+cost+parentNode.g, None, parentNode, curPosX, curPosY)
            else:
                newNode = Node(("N"+str(self.nodeCount)), operation, 0, cost+parentNode.g, hValue, hValue+cost+parentNode.g, None, parentNode, curPosX, curPosY)
            parentNode.setChild(newNode)
            self.nodeCount += 1
            self.graph.append(newNode)
            self.open.append(newNode)

            self.reOrderList()

        elif (result[0] == "inOpen") & (self.algo == "A"):
            existNode = result[1]
            hValue = self.hFunction(curPosX, curPosY)
            gValue = cost+parentNode.g
            fValue = hValue + gValue
            # If the new F is lower, update the value and redirect the parent
            if int(existNode.f) > int(fValue):
                existNode.setParent(parentNode)
                existNode.setF(fValue)

                self.reOrderList()

        elif result[0] =="inClosed":
            pass #do nothing 



    def reOrderList(self):
        """
        For A algorithm,
        Reorder the OPEN list, since we use pop function, the list OPEN is sorted in descending order of merit f.
        Using Insertion sort, as it is stable.
        Hence, the tie braking rule is LIFO for same f.
        """
        for m in range(1,len(self.open)):
            #insert aList[index] in aList[0:index] in sorted order
            position = m
            while self.open[position-1].f < self.open[position].f and position>0:
                # Swap element
                temp = self.open[position-1]
                self.open[position-1] = self.open[position]
                self.open[position] = temp
                position = position-1



    def outputPath(self,n):
        """
        Trace and output the path from start to goal.
        """
        goalNode = n
        string = ""
        tmpList = []
        # List out the node path from goal to start in tmpList
        while (n != None):
            tmpList.append(n)
            n = n.parent
        tmpList.reverse()
        
        for i in tmpList:
            tmpMap = copy.deepcopy(self.theMap)
            tmpMap[i.posX][i.posY] = "*"
            string = string + self.reformatMap(tmpMap) + "\n"
            string = string + i.operator + " " + str(i.f) + "\n"
        return string

            

    def reformatMap(self,theMap):
        """
        Reformat the map to more readable format.
        """
        newMap = ""
        for x in range(len(theMap)):
            for y in range(len(theMap[x])):
                newMap = newMap + theMap[x][y]
            newMap = newMap + "\n"
        return newMap



    def hFunction(self, posX, posY):
        """
        The heuristic function for A/A* algprithm. 
        The heuristic funtion used Euclidean Distance Algorithm.
        h = sqrt ( (curPosX – goalPosX)^2 + (curPosY – goalPosY)^2 ) 
        """
        goalPosX, goalPosY = self.findGoalPoint()
        h = math.sqrt((posX - goalPosX)**2 + (posY - goalPosY)**2)
        return h
        


    def graphBasicAlgorithm(self):
        """
        The basic graph algorithm for DLS and A/A*.
        Algorithm based on pg38 Search Algorithm Lecture Slides.
        """
        depth = 0
        limit = self.mapSize ** 2 # The steps not more than total size of map
        self.graph.append(self.startNode) #Create a search graph consisting only start node s
        self.open.append(self.startNode)
        while len(self.open) > 0:
            # Check the depth limit for DLS
            if (self.algo == "D"):
                if depth > limit:
                    return "NO-PATH"
            n = self.open.pop()
            self.closed.append(n)
            if self.theMap[n.posX][n.posY] == graphSearch.goal:
                n.operator = n.operator + "-G"
                string = self.outputPath(n) # trace the path from start to goal
                return string

            n.orderExpansion = self.orderExpansion
            self.orderExpansion += 1
            self.expandChild(n.posX, n.posY, n)

            depth += 1 # For DLS
        return "NO-PATH"

    

if __name__ == "__main__":
    print("Graph Search Test")

