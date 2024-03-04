# Machine-Learning-AI
This repo includes the study learnt from Machine Learning unit in Monash University.
It includes
- [Part 1: Depth Limited Search(DLS) and A/A* Search](#part-1-depth-limited-searchdls-and-aa-search)
- [Part 2: Decision Tree Learning for Chess End-Game Prediction](#part-2-decision-tree-learning-for-chess-end-game-prediction)

# Part 1: Depth Limited Search(DLS) and A/A* Search
Robotic Path Planning on Topographic Maps

## Project Summary

This project involves implementing a Python 3 program, named "planpath," to plan a path for ROBBIE the robot through a topographic map. The map consists of normal and mountainous terrain tiles, and ROBBIE aims to navigate from a starting position to a goal position. Two search algorithms, Depth-Limited Search (DLS) and A* (A or A*), are implemented within a single Graph/Treesearch procedure, allowing for different search strategies using various ordering functions.

The code is in folder `Depth Limited Search (DLS) & A Search`.

### Implementation Details

1. **Transition Rules:**
   - ROBBIE can move to one of the eight surrounding tiles but cannot traverse mountainous tiles.
   - Diagonal moves are restricted if one of the diagonal directions contains a mountainous tile.

2. **Path Cost:**
   - Diagonal moves have a cost of 1, while other moves have a cost of 2.

3. **Implemented Algorithms:**
   - Depth-Limited Search (DLS)
   - A* (A or A*) with a proposed heuristic function.

4. **Heuristic Function:**
   - A heuristic function is implemented for A* to guide the search process.
   - Admissibility and monotonicity of the heuristic function are determined and explained.

5. **Tie-Breaking Rules:**
   - Tie-breaking rules are implemented to handle cases where multiple options have equal merit.

6. **Input Format:**
- The first line specifies the number of rows and columns in the map.
- Subsequent lines contain the map, with values for normal, mountainous, start, and goal tiles.

7. **Output Format:**
- The program produces a sequence of moves, accumulated costs, and ROBBIE's position after each move.
- If no path is found, the output states "NO-PATH."



### Command-Line Execution

The program can be executed using the following command:
Please note that A is A/A* Algorithm while D is the DLS algorithm

```bash
python planpath.py INPUT\inputi.txt OUTPUT\outputi.txt Flag Algorithm
```

For example

```bash
python planpath.py INPUT\input1.txt OUTPUT\output1.txt 5 D
python planpath.py INPUT\input1.txt OUTPUT\output1.txt 5 A
```

<br>
<br>


# Part 2: Decision Tree Learning for Chess End-Game Prediction

## Project Summary

This project involves implementing a decision tree learning algorithm, specifically designed for datasets with binary features and labels. The algorithm employs the maximum information gain heuristic as its splitting rule. Additionally, the implementation includes an extension to limit the depth of the tree, allowing for a more controlled and interpretable model.

The code is in folder `Decision Tree`.

## Implementation Details

### 1. Decision Tree Learning Procedure

- Based on the recursive training procedure outlined in as described in Section 18.3: ’Learning Decision
Trees’ 
- Takes a "depth" parameter to control the maximum height of the tree.
- If depth is 0, the resulting tree is a single node. If depth is 1, the tree is a decision stump, and so on.
- Ensures there are at most "n" non-leaf nodes along any path from the root to a leaf node.

### 2. Prediction Procedure

- Given an unlabeled test example, predicts the label using the learned decision tree.

### 3. Dataset

- Utilizes a chess end-game dataset with binary features derived from chess positions and binary labels indicating whether white can win (1) or not (0).
- The dataset includes training and test sets in CSV format.

### 4. Command-Line Execution

The program can be executed using the following command:

```bash
python learningDecisionTree.py <train_file> <depth> <test_file> <output_file>
```

For example

```bash
python learningDecisionTree.py train.txt 5 test.txt output.txt
```
