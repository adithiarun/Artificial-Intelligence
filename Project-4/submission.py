import numpy as np
from collections import Counter
import time

from numpy.core.defchararray import split


class DecisionNode:
    """Class to represent a single node in a decision tree."""

    def __init__(self, left, right, decision_function, class_label=None):
        """Create a decision function to select between left and right nodes.
        Note: In this representation 'True' values for a decision take us to
        the left. This is arbitrary but is important for this assignment.
        Args:
            left (DecisionNode): left child node.
            right (DecisionNode): right child node.
            decision_function (func): function to decide left or right node.
            class_label (int): label for leaf node. Default is None.
        """

        self.left = left
        self.right = right
        self.decision_function = decision_function
        self.class_label = class_label

    def decide(self, feature):
        """Get a child node based on the decision function.
        Args:
            feature (list(int)): vector for feature.
        Return:
            Class label if a leaf node, otherwise a child node.
        """

        if self.class_label is not None:
            return self.class_label

        elif self.decision_function(feature):
            return self.left.decide(feature)

        else:
            return self.right.decide(feature)


def load_csv(data_file_path, class_index=-1):
    """Load csv data in a numpy array.
    Args:
        data_file_path (str): path to data file.
        class_index (int): slice output by index.
    Returns:
        features, classes as numpy arrays if class_index is specified,
            otherwise all as nump array.
    """

    handle = open(data_file_path, 'r')
    contents = handle.read()
    handle.close()
    rows = contents.split('\n')
    out = np.array([[float(i) for i in r.split(',')] for r in rows if r])

    if(class_index == -1):
        classes= out[:,class_index]
        features = out[:,:class_index]
        return features, classes
    elif(class_index == 0):
        classes= out[:, class_index]
        features = out[:, 1:]
        return features, classes

    else:
        return out


def build_decision_tree():
    """Create a decision tree capable of handling the sample data.
    Tree is built fully starting from the root.
    Returns:
        The root node of the decision tree.
    """

    decision_tree_a1 = DecisionNode(None, None, lambda a: a[0] == 0)
    decision_tree_a2 = DecisionNode(None, None, lambda a: a[1] == 0)
    decision_tree_a3 = DecisionNode(None, None, lambda a: a[2] == 0)
    decision_tree_a4 = DecisionNode(None, None, lambda a: a[3] == 0)
    
    decision_tree_a1.left = DecisionNode(None, None, None, 0)
    decision_tree_a1.right = DecisionNode(None, None, None, 1)

    decision_tree_a4.left = decision_tree_a3
    decision_tree_a4.right = decision_tree_a2

    decision_tree_a3.left = DecisionNode(None, None, None, 1)
    decision_tree_a3.right = DecisionNode(None, None, None, 0)

    decision_tree_a2.left = DecisionNode(None, None, None, 1)
    decision_tree_a2.right = decision_tree_a1

    return decision_tree_a4


def confusion_matrix(classifier_output, true_labels):
    """Create a confusion matrix to measure classifier performance.
    Output will in the format:
        [[true_positive, false_negative],
         [false_positive, true_negative]]
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
    Returns:
        A two dimensional array representing the confusion matrix.
    """

    true_positive = np.count_nonzero(np.logical_and((np.array(classifier_output) == 1), (np.array(true_labels) == 1)))
    true_negative = np.count_nonzero(np.logical_and((np.array(classifier_output) == 0), (np.array(true_labels) == 0)))
    false_positive = np.count_nonzero(np.logical_and((np.array(classifier_output) == 1), (np.array(true_labels) == 0)))
    false_negative = np.count_nonzero(np.logical_and((np.array(classifier_output) == 0), (np.array(true_labels) == 1)))

    return [[true_positive, false_negative], [false_positive, true_negative]]



def precision(classifier_output, true_labels):
    """Get the precision of a classifier compared to the correct values.
    Precision is measured as:
        true_positive/ (true_positive + false_positive)
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
    Returns:
        The precision of the classifier output.
    """

    c_matrix = confusion_matrix(classifier_output, true_labels)
    return c_matrix[0][0]/(c_matrix[0][0] + c_matrix[1][0])


def recall(classifier_output, true_labels):
    """Get the recall of a classifier compared to the correct values.
    Recall is measured as:
        true_positive/ (true_positive + false_negative)
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
    Returns:
        The recall of the classifier output.
    """

    c_matrix = confusion_matrix(classifier_output, true_labels)
    return c_matrix[0][0]/(c_matrix[0][0] + c_matrix[0][1])


def accuracy(classifier_output, true_labels):
    """Get the accuracy of a classifier compared to the correct values.
    Accuracy is measured as:
        correct_classifications / total_number_examples
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
    Returns:
        The accuracy of the classifier output.
    """

    c_matrix = confusion_matrix(classifier_output, true_labels)
    return (c_matrix[0][0] + c_matrix[1][1])/np.sum(c_matrix)


def gini_impurity(class_vector):
    """Compute the gini impurity for a list of classes.
    This is a measure of how often a randomly chosen element
    drawn from the class_vector would be incorrectly labeled
    if it was randomly labeled according to the distribution
    of the labels in the class_vector.
    It reaches its minimum at zero when all elements of class_vector
    belong to the same class.
    Args:
        class_vector (list(int)): Vector of classes given as 0 or 1.
    Returns:
        Floating point number representing the gini impurity.
    """

    if(len(class_vector) > 0):
        p_i = class_vector.count(1)/len(class_vector)
    else:
        p_i = 0
    p_not_i = 1 - p_i
    gini_i = 1-(p_i*p_i + p_not_i*p_not_i)

    return gini_i


def gini_gain(previous_classes, current_classes):
    """Compute the gini impurity gain between the previous and current classes.
    Args:
        previous_classes (list(int)): Vector of classes given as 0 or 1.
        current_classes (list(list(int): A list of lists where each list has
            0 and 1 values).
    Returns:
        Floating point number representing the information gain.
    """
    
    previous_entropy = gini_impurity(previous_classes)
    sum = 0
    length = 0
    for each in current_classes:
        sum += gini_impurity(each)*len(each)
        length += len(each)
    gini_g = previous_entropy - sum/length
    return gini_g

class DecisionTree:
    """Class for automatic tree-building and classification."""

    def __init__(self, depth_limit=float('inf')):
        """Create a decision tree with a set depth limit.
        Starts with an empty root.
        Args:
            depth_limit (float): The maximum depth to build the tree.
        """

        self.root = None
        self.depth_limit = depth_limit

    def fit(self, features, classes):
        """Build the tree from root using __build_tree__().
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
        """

        self.root = self.__build_tree__(features, classes)

    def __build_tree__(self, features, classes, depth=0):
        """Build tree that automatically finds the decision functions.
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
            depth (int): depth to build tree to.
        Returns:
            Root node of decision tree.
        """
        # base cases are correct
        value, counts = np.unique(classes, return_counts=True)
        d = dict(zip(value, counts))
        if len(d) == 0:
            return DecisionNode(None, None, None, None)
        if len(d) == 1:
            x = list(d.keys())[0]
            return DecisionNode(None, None, None, x)
        elif depth == self.depth_limit:
            return DecisionNode(None, None, None, max(d.keys()))
        # mean of each is th
        # get split
        shape = np.shape(features)
        means = features.mean(axis=0)
        gini_gains = []
        split = []
        f_1 = []
        f_2 = []
        # don't convert between np array and list
        for i in range(shape[1]):
            split1 = []
            split2 = []
            features1 = []
            features2 = []
            for j in range(shape[0]):
                if features[j][i] >= means[i]:
                    split1.append(classes[j])
                    features1.append(list(features[j,:]))
                else:
                    split2.append(classes[j])
                    features2.append(list(features[j,:]))
            split.append(split1)
            split.append(split2)
            f_1.append(features1)
            f_2.append(features2)
            gini_gains.append(gini_gain(list(classes), [split1, split2]))
        alpha_best_idx = gini_gains.index(max(gini_gains))
        # create decision node that splits on alpha best
        # recursion on left and right to build tree
        node = DecisionNode(None, None, lambda features: features[alpha_best_idx] >= means[alpha_best_idx])
        node.left = self.__build_tree__(np.array(f_1[alpha_best_idx]), np.array(split[2*alpha_best_idx]), depth+1)
        node.right = self.__build_tree__(np.array(f_2[alpha_best_idx]), np.array(split[2*alpha_best_idx+1]), depth+1)
        return node


    def classify(self, features):
        """Use the fitted tree to classify a list of example features.
        Args:
            features (m x n): m examples with n features.
        Return:
            A list of class labels.
        """

        class_labels = []
        # feed features into decision tree and get class_labels
        for each in features:
            class_labels.append(self.root.decide(each))
        return class_labels


def generate_k_folds(dataset, k):
    """Split dataset into folds.
    Randomly split data into k equal subsets.
    Fold is a tuple (training_set, test_set).
    Set is a tuple (features, classes).
    Args:
        dataset: dataset to be split.
        k (int): number of subsections to create.
    Returns:
        List of folds.
        => Each fold is a tuple of sets.
        => Each Set is a tuple of numpy arrays.
    """
    data = np.hstack((dataset[0], (dataset[1]).reshape((len(dataset[1]), 1))))
    
    length = len(dataset[1])
    num = int(length/k)
    folds = []
    for i in range(k):
        d = data
        np.random.shuffle(d)
        test = d[:num]
        train = d[num:]
        test_0 = test[:,0:3]
        test_1 = test[:, 4]
        test_1.reshape((num,))
        train_0 = train[:,0:3]
        train_1 = train[:, 4]
        train_1.reshape((length-num,))
        tr = (train_0, train_1)
        te = (test_0, test_1)
        folds.append((tr, te))

    return folds


class RandomForest:
    """Random forest classification."""

    def __init__(self, num_trees=5, depth_limit=5, example_subsample_rate=0.5,
                 attr_subsample_rate=0.5):
        """Create a random forest.
         Args:
             num_trees (int): fixed number of trees.
             depth_limit (int): max depth limit of tree.
             example_subsample_rate (float): percentage of example samples.
             attr_subsample_rate (float): percentage of attribute samples.
        """

        self.trees = []
        self.num_trees = num_trees
        self.depth_limit = depth_limit
        self.example_subsample_rate = example_subsample_rate
        self.attr_subsample_rate = attr_subsample_rate

    def fit(self, features, classes):
        """Build a random forest of decision trees using Bootstrap Aggregation.
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
        """

        data_shuffle = np.hstack((features, classes.reshape(len(classes), 1)))
        # np.random.shuffle(data_shuffle)
        for i in range(15):
            train = []
            data_indices = np.random.choice(range(0, len(features)), int(self.example_subsample_rate*len(features)), replace=True)
            attribute_indices = np.sort(np.random.choice(range(0, len(features[0])), int(0.75*len(features[0])), replace=False))
            for each in data_indices:
                x = []
                for a in attribute_indices:
                    x.append(data_shuffle[each][a])
                x.append(data_shuffle[each][len(data_shuffle[0])-1])
                train.append(x)
            tree = DecisionTree(self.depth_limit)
            t = np.array(train)
            tree.fit(t[:, :-1], t[:, -1])
            self.trees.append(tree)

    def classify(self, features):
        """Classify a list of features based on the trained random forest.
        Args:
            features (m x n): m examples with n features.
        """
        labels = []
        counts = []
        max_votes = []
        for tree in self.trees:
            labels.append(list(tree.classify(features)))
        l = np.array([np.array(label) for label in labels])
        s = l.shape
        # print(len(l))
        for i in range(s[1]):
            classification, count = np.unique(l[:,i], return_counts=True)
            d = dict(zip(classification, count))
            counts.append(d)
        # print(len(counts))
        for each in counts:
            if 0 in each.keys() and 1 in each.keys():
                if each[0] > each[1]:
                    max_votes.append(0)
                else:
                    max_votes.append(1)
            elif 0 in each.keys() and 1 not in each.keys():
                max_votes.append(0)
            else:
                max_votes.append(1)
        mv = np.array(max_votes)
        # print(len(max_votes))
        return mv


class ChallengeClassifier:
    """Challenge Classifier used on Challenge Training Data."""

    def __init__(self, depth_limit=10):
        """Create a decision tree with a set depth limit.
        Starts with an empty root.
        Args:
            depth_limit (float): The maximum depth to build the tree.
        """

        self.root = None
        self.depth_limit = depth_limit

    def fit(self, features, classes):
        """Build the tree from root using __build_tree__().
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
        """

        self.root = self.__build_tree__(features, classes)

    def __build_tree__(self, features, classes, depth=0):
        """Build tree that automatically finds the decision functions.
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
            depth (int): depth to build tree to.
        Returns:
            Root node of decision tree.
        """
        # base cases are correct
        value, counts = np.unique(classes, return_counts=True)
        d = dict(zip(value, counts))
        if len(d) == 0:
            return DecisionNode(None, None, None, None)
        if len(d) == 1:
            x = list(d.keys())[0]
            return DecisionNode(None, None, None, x)
        elif depth == self.depth_limit:
            return DecisionNode(None, None, None, max(d.keys()))
        # mean of each is th
        # get split
        shape = np.shape(features)
        means = features.mean(axis=0)
        gini_gains = []
        split = []
        f_1 = []
        f_2 = []
        # don't convert between np array and list
        for i in range(shape[1]):
            split1 = []
            split2 = []
            features1 = []
            features2 = []
            for j in range(shape[0]):
                if features[j][i] >= means[i]:
                    split1.append(classes[j])
                    features1.append(list(features[j,:]))
                else:
                    split2.append(classes[j])
                    features2.append(list(features[j,:]))
            split.append(split1)
            split.append(split2)
            f_1.append(features1)
            f_2.append(features2)
            gini_gains.append(gini_gain(list(classes), [split1, split2]))
        alpha_best_idx = gini_gains.index(max(gini_gains))
        # create decision node that splits on alpha best
        # recursion on left and right to build tree
        node = DecisionNode(None, None, lambda features: features[alpha_best_idx] >= means[alpha_best_idx])
        node.left = self.__build_tree__(np.array(f_1[alpha_best_idx]), np.array(split[2*alpha_best_idx]), depth+1)
        node.right = self.__build_tree__(np.array(f_2[alpha_best_idx]), np.array(split[2*alpha_best_idx+1]), depth+1)
        return node


    def classify(self, features):
        """Use the fitted tree to classify a list of example features.
        Args:
            features (m x n): m examples with n features.
        Return:
            A list of class labels.
        """

        class_labels = []
        # feed features into decision tree and get class_labels
        for each in features:
            class_labels.append(self.root.decide(each))
        return class_labels
        


class Vectorization:
    """Vectorization preparation for Assignment 5."""

    def __init__(self):
        pass

    def non_vectorized_loops(self, data):
        """Element wise array arithmetic with loops.
        This function takes one matrix, multiplies by itself and then adds to
        itself.
        Args:
            data: data to be added to array.
        Returns:
            Numpy array of data.
        """

        non_vectorized = np.zeros(data.shape)
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                non_vectorized[row][col] = (data[row][col] * data[row][col] +
                                            data[row][col])
        return non_vectorized

    def vectorized_loops(self, data):
        """Element wise array arithmetic using vectorization.
        This function takes one matrix, multiplies by itself and then adds to
        itself.
        Args:
            data: data to be sliced and summed.
        Returns:
            Numpy array of data.
        """

        vectorized = np.multiply(data, data) + data
        return vectorized
        raise NotImplemented()

    def non_vectorized_slice(self, data):
        """Find row with max sum using loops.
        This function searches through the first 100 rows, looking for the row
        with the max sum. (ie, add all the values in that row together).
        Args:
            data: data to be added to array.
        Returns:
            Tuple (Max row sum, index of row with max sum)
        """

        max_sum = 0
        max_sum_index = 0
        for row in range(100):
            temp_sum = 0
            for col in range(data.shape[1]):
                temp_sum += data[row][col]

            if temp_sum > max_sum:
                max_sum = temp_sum
                max_sum_index = row

        return max_sum, max_sum_index

    def vectorized_slice(self, data):
        """Find row with max sum using vectorization.
        This function searches through the first 100 rows, looking for the row
        with the max sum. (ie, add all the values in that row together).
        Args:
            data: data to be sliced and summed.
        Returns:
            Tuple (Max row sum, index of row with max sum)
        """
        row_sums = np.sum(data[0:100, :], axis=1)
        max_sum_index = np.argmax(row_sums)
        return row_sums[max_sum_index], max_sum_index
        raise NotImplemented()

    def non_vectorized_flatten(self, data):
        """Display occurrences of positive numbers using loops.
         Flattens down data into a 1d array, then creates a dictionary of how
         often a positive number appears in the data and displays that value.
         ie, [(1203,3)] = integer 1203 appeared 3 times in data.
         Args:
            data: data to be added to array.
        Returns:
            List of occurrences [(integer, number of occurrences), ...]
        """

        unique_dict = {}
        flattened = np.hstack(data)
        for item in range(len(flattened)):
            if flattened[item] > 0:
                if flattened[item] in unique_dict:
                    unique_dict[flattened[item]] += 1
                else:
                    unique_dict[flattened[item]] = 1

        return unique_dict.items()

    def vectorized_flatten(self, data):
        """Display occurrences of positive numbers using vectorization.
         Flattens down data into a 1d array, then creates a dictionary of how
         often a positive number appears in the data and displays that value.
         ie, [(1203,3)] = integer 1203 appeared 3 times in data.
         Args:
            data: data to be added to array.
        Returns:
            List of occurrences [(integer, number of occurrences), ...]
        """
        unique_dict, counts = np.unique(data, return_counts=True)
        final_dict = zip(unique_dict, counts)
        new_dict = []
        for each in final_dict:
            if each[0] > 0:
                new_dict.append((each[0], each[1]))
        return new_dict
        raise NotImplemented()

def return_your_name():
    return "Adithi Minnasandran"
    raise NotImplemented()
