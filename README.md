# Machine-Learning-AI




# Part 2: Decision Tree Learning for Chess End-Game Prediction

## Project Summary

This project involves implementing a decision tree learning algorithm, specifically designed for datasets with binary features and labels. The algorithm employs the maximum information gain heuristic as its splitting rule. Additionally, the implementation includes an extension to limit the depth of the tree, allowing for a more controlled and interpretable model.

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