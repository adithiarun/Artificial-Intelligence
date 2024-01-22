## Build, Train, and Test Decision Tree Models

Decision Trees are a type of Supervised Machine Learning Model. In supervised learning, we feed a sample input and output, and the model learns a function that maps the input to the output. We then test the model against a test dataset that is different from the training set. A hypothesis generalizes well if it correctly predicts the y value. Decision trees take a vector of attribute values as input and return a decision. 

## DecisionNode Class

This class represents a single node in the decision tree. It is initialized with a left child node, a right child node, a decision function, and a class label.

Left points to values where the decision function returns a true, while right points to values where the decision function returns a false.

### Decide Function
The decide function is used to get a child node based on the decision function.

### Build Decision Tree
Helper function that builds the decision tree and returns the root node.

### Confusion Matrix
This function returns the confusion matrix as a list of lists ([[true positive, false negative], [false positive, true negative]]). The confusion matrix gives us a measure of the model's performance. 

True Positive: Number of outcomes where the model correctly predicts the positive class

False Negative: Number of outcomes where the model incorrectly predicts the negative class

True Negative: Number of outcomes where the model correctly predicts the negative class

False Positive: Number of outcomes where the model incorrectly predicts the positive class

### Other Performance Metrics
