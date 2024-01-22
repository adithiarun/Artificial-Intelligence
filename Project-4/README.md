## Build, Train, and Test Decision Tree Models

Decision Trees are a type of Supervised Machine Learning Model. In supervised learning, we feed a sample input and output, and the model learns a function that maps the input to the output. We then test the model against a test dataset that is different from the training set. A hypothesis generalizes well if it correctly predicts the y value. Decision trees take a vector of attribute values as input and return a decision. 

## DecisionNode Class

This class represents a single node in the decision tree. It is initialized with a left child node, a right child node, a decision function, and a class label.

Left points to values where the decision function returns a true, while right points to values where the decision function returns a false.

### Decide Function
The decide function is used to get either the left child or the right child node based on the return value of the decision function.

### Build Decision Tree
Helper function that builds the decision tree and returns the root node.

### Confusion Matrix
This function returns the confusion matrix as a list of lists ([[true positive, false negative], [false positive, true negative]]). The confusion matrix gives us a measure of the model's performance. 

True Positive: Number of outcomes where the model correctly predicts the positive class

False Negative: Number of outcomes where the model incorrectly predicts the negative class

True Negative: Number of outcomes where the model correctly predicts the negative class

False Positive: Number of outcomes where the model incorrectly predicts the positive class

### Other Performance Metrics

#### Precision = True Positive / (True Positive + False Positive)
Precision gives us a measure of what portion of outcomes were correctly identified as being positive divided by the number of correctly identified positives plus the incorrectly identified positives.

#### Recall = True Positive / (True Positive + False Negative)
Recall is the number of outcomes that were correctly identified as being positive divided by the total number of actual positives.

#### Accuracy = (True Positive + True Negative) / (True Positive + False Positive + True Negative + False Negative)
Accuracy is the total number of correct predictions divided by the total number of predictions

There can be instances where the precision and recall are low but accuracy is high. Hence, it is important to pay attention to precision and recall, so that we take false positives and false negatives into account.

#### Gini Impurity 
