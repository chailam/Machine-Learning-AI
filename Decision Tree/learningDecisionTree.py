"""
Author: Chai Lam Loi
Date: 25/10/2019
Aim: Implement a learning decision tree as machine learning supervised classification.
The algorithm provided in "Artificial Intelligent: A Modern Approach", chapter 18.3., Learning Decision Tree

To run the file, the command must be
python learningDecisionTree.py <train_file> <depth> <test_file> <output_file>

"""
import math
import copy
import sys
import matplotlib.pyplot as plt 
import DecisionTree
import LeafNode

# ======================


def read_datafile(fname, attribute_data_type='integer'):
    inf = open(fname, 'r')
    lines = inf.readlines()
    inf.close()
    # --
    X = []
    Y = []
    for l in lines:
        ss = l.strip().split(',')
        temp = []
        for s in ss:
            if attribute_data_type == 'integer':
                temp.append(int(s))
            elif attribute_data_type == 'string':
                temp.append(s)
            else:
                print("Unknown data type")
                exit()
        X.append(temp[:-1])
        Y.append(int(temp[-1]))
    return X, Y


def majorityValue(a_list):
    """
    The function used to determine the majority value in the a list.
    return: (majority value, occurence of that value)
    """
    zeroCount = 0
    oneCount = 0
    for i in a_list:
        if i == 0:
            zeroCount += 1
        elif i == 1:
            oneCount += 1
    if zeroCount > oneCount:
        return (0, zeroCount)
    else:
        return (1, oneCount)


def checkSameClass(Y_train):
    """
    The function is to check whether the provided training set Y has all the same classification,
    if true, return the classification (0,1); if false, return None.
    """
    total = sum(Y_train)
    if total == 0:
        return 0
    elif total == len(Y_train):
        return 1
    else:
        return None


def calEntropy(Y_List):
    """
    Calculates the entropy of a given attributes.
    Entropy = -(N/Total)*log2(N/Total) - (P/Total)*log2(P/Total)
    """
    total = len(Y_List)
    if total > 0:
        tmp = majorityValue(Y_List)
        count = tmp[1]
        count2 = total - count
        if (count == 0) or (count2 == 0):
           entropy = 0
        else:
            entropy = -((count/total)*math.log(count/total, 2)) - ((count2/total)*math.log(count2/total, 2))
    else:
        entropy = 0
    return entropy
      


def calInfoGain(X_List, Y_List):
    """
    Calculates the information gain.
    Gain(S,A) = Entropy(S) - summation(Sv/S) Entropy(Sv)
    """
    if (len(X_List) > 0) & (len(Y_List) > 0):
      entropyS = calEntropy(Y_List)
      zeroYList = []  # when x is zero, the value of y is recorded in this list
      oneYList = []  # when x is one, the value of y is recorded in this list
      count1 = 0
      count0 = 0
      for v in range(len(X_List)):
         if X_List[v] == 0:
            count0 += 1
            zeroYList.append(Y_List[v])
         elif X_List[v] == 1:
            count1 += 1
            oneYList.append(Y_List[v])

      entropyOne = calEntropy(oneYList)
      entropyZero = calEntropy(zeroYList)
         
      total = len(X_List)
      gain = entropyS - (count0/total)*entropyZero - (count1/total)*entropyOne
      return gain
    else:
      print("Total is less than 0 in InfoGain. Error.")
      raise Exception


def chooseAttr(attributes, X_List, Y_List):
   """
   Calculate Information Gain for all the attributes in examples, and return the maximum
   return: (the index of maximum gain in attributes matrix, the maximum value of gain)
   """
   currMaxIndex = -1
   currMax = -1
   tmpGain = -100
   for index in range(len(attributes)):
      if len(attributes[index]) > 0:
         tmpGain = calInfoGain(attributes[index], Y_List)
      if tmpGain > currMax:
         currMax = tmpGain
         currMaxIndex = index
   return (currMaxIndex,currMax)


def restructureArg(X_List, Y_List, attributes, chosenIndex, curValue):
   """
   Restructure the list with the chosen attribute
   """
   newXList = []
   newY_List = []
   newAttributes = copy.deepcopy(attributes)
   chosenAttribute = attributes[chosenIndex]
   # Structure X and Y List
   for c in range(len(chosenAttribute)):
      if chosenAttribute[c] == curValue:
         newXList.append(X_List[c])
         newY_List.append(Y_List[c])

   # Structure attribute list
   for c in range(len(chosenAttribute)-1,-1,-1):
      for k in range(len(newAttributes)):
         if len(newAttributes[k]) > 0:
            if chosenAttribute[c] != curValue:
               newAttributes[k].pop(c)

   newAttributes[chosenIndex] = [] # remove the used attributes
   return newXList, newY_List, newAttributes


def formatAttributesList(X_List):
   """
   Format the attributes list from X list before entering the learning tree algorithm.
   """
   attributes = []
   tmp = []
   for i in range(len(X_List[0])):
      for j in range(len(X_List)):
         tmp.append(X_List[j][i])
      attributes.append(tmp)
      tmp = []
   return attributes


def attributesEmpty(attributes):
   """
   Check if the attributes list is empty.
   The list is empty when there is no content in every single sublist.
   """
   empty = True
   for i in attributes:
      if len(i) > 0:
         empty = False
   return empty


def decisionTreeLearning(X_train, Y_train, attributes, defaultV, depth, curDepth):
    """
    The decision Tree learning algorithm using train set..
    The algorithm is provided in "Artificial Intelligent: A Modern Approach", chapter 18.3
    attributes: list of list contain attiribute [1,1,0,1,0].
    """
    # If depth = 0, just return majority vote
    if depth == 0:
       return LeafNode.LeafNode(majorityValue(Y_train)[0])

    # if the currentdepth is larger than depth, then just return the leafnode.
    if curDepth >= depth:
       return LeafNode.LeafNode(majorityValue(Y_train)[0])
    
    if len(X_train) == 0:
        return LeafNode.LeafNode(defaultV)
    elif checkSameClass(Y_train) != None:
        return LeafNode.LeafNode(checkSameClass(Y_train))
    elif attributesEmpty(attributes) == True: 
        return LeafNode.LeafNode(majorityValue(Y_train)[0])
    else:
        chosenIndex = chooseAttr(attributes, X_train, Y_train)[0]
        tree = DecisionTree.DecisionTree(chosenIndex)
        m = majorityValue(Y_train)[0]
        for value in range(2): # since the it's only binary value and label.
          # Restructure attributes, X_train and Y_train
          newX_train, newY_train, newAttributes = restructureArg(X_train, Y_train, attributes, chosenIndex, value)
          # Recursive for the decision tree
          subtree = decisionTreeLearning(newX_train, newY_train, newAttributes, m, depth, curDepth+1) 
          tree.add(value,subtree)

        return tree
      

def predict(tree, x):
   """
   Predict the value using the tree created.
   Return the predicted result.
   """
   node = tree
   while type(node) != LeafNode.LeafNode:
      nodeValue = node.attribute # the attribute value in tree
      xValue = x[nodeValue] # the x value of that attribute
      branches = node.branches
      for b in branches:
         attrValue = b[0]
         if attrValue == xValue:
            node = b[1]
   # Reach the leaf node
   predicted = node.attribute
   return predicted
            
      
def compute_accuracy(dt_classifier, X_test, Y_test):
   """
   Compute the accuracy of the tree using test data.
   """
   numRight = 0
   for i in range(len(Y_test)):
      x = X_test[i]
      y = Y_test[i]
      if y == predict(dt_classifier,x):
         numRight += 1
   return (numRight*1.0)/len(Y_test)


def writeToFile(filename,accuracy):
   """
   Function to write the accuracy to filename
   """
   f = open(filename,"a+")
   f.write(accuracy)
   f.write("\n")
   f.close()


def plotGraph(depthList, testAccuracy, trainAccuracy):
   """
   Use matplotlib to plot the accuracy vs depth (0 - 30).
   There are 2 accuracy lists: test accuracy and train accuracy
   """
   # plotting the points  
   plt.plot(depthList, testAccuracy, label = "Test Accuracy") 
   plt.plot(depthList, trainAccuracy, label = "Train Accuracy") 
   # naming the x & y axis 
   plt.xlabel('Depth') 
   plt.ylabel('Accuracy')  
   # show a legend on the plot & give title
   plt.legend() 
   plt.title('Accuracy vs Depth') 
   # show the plot 
   plt.show() 


def graphForReport():
   """
   A graph plotted from depth 0 to 30 vs training accuracy and test accuracy.
   For Report Summary use.
   """
   X_train, Y_train = read_datafile('train.txt')
   X_test, Y_test = read_datafile('test.txt')
   attributes = formatAttributesList(X_train)
   defaultV = 1
   curDepth = 0

   depthList = []
   accuracyTest = []
   accuracyTrain = []
   for i in range(30):
      depthList.append(i)
      # Build the tree
      tree = decisionTreeLearning(X_train, Y_train, attributes, defaultV, i, curDepth)
      # Compute accuracy for test set
      accuracy = compute_accuracy(tree, X_test, Y_test)
      accuracyTest.append(accuracy)
      # Compute accuracy for training set
      accuracy = compute_accuracy(tree, X_train, Y_train)
      accuracyTrain.append(accuracy)

   plotGraph(depthList, accuracyTest, accuracyTrain)
   

#==========================================================================#

if __name__ == "__main__":   
   if len(sys.argv) != 5:
      raise Exception("Please enter correct command.")
   
   # Command from argument
   trainFile = sys.argv[1]
   depth = int(sys.argv[2])
   testFile = sys.argv[3]
   outputFile = sys.argv[4]

   # Read the file for train and test data 
   X_train, Y_train = read_datafile(trainFile)
   X_test, Y_test = read_datafile(testFile)

   # Initiate the variable and run the tree learning
   defaultV = 1
   curDepth = 0
   attributes = formatAttributesList(X_train)

   tree = decisionTreeLearning(X_train, Y_train, attributes, defaultV, depth, curDepth)
   #print(tree)

   # Calculate the accuracy
   accuracy = compute_accuracy(tree, X_test, Y_test)
   print("Accuracy: " + str(accuracy))

   # Write the accuracy to file
   writeToFile(outputFile,str(accuracy))
   
   #============================= Report Graph ====================================#
   #graphForReport()    

   #===============================================================================#
   

 
