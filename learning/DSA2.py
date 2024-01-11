class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeAnalyzer:
    def __init__(self, root=None):
        self.root = root

    def max_depth(self):
        def max_depth_helper(node):
            if not node:
                return 0
            return 1 + max(max_depth_helper(node.left), max_depth_helper(node.right))

        return max_depth_helper(self.root)

    def average_leaf_value(self):
        def average_leaf_value_helper(node, depth, leaf_values, leaf_depths):
            if not node:
                return
            if not node.left and not node.right:
                leaf_values.append(node.value)
                leaf_depths.append(depth)
            average_leaf_value_helper(node.left, depth + 1, leaf_values, leaf_depths)
            average_leaf_value_helper(node.right, depth + 1, leaf_values, leaf_depths)

        leaf_values = []
        leaf_depths = []
        average_leaf_value_helper(self.root, 0, leaf_values, leaf_depths)

        if not leaf_values:
            return 0

        numeric_leaf_values = [value for value in leaf_values if isinstance(value, (int, float))]
        return sum(numeric_leaf_values) / len(numeric_leaf_values)

# Driver code:
initial_tree_root = TreeNode(30)
initial_tree_root.left = TreeNode("CAT")
initial_tree_root.right = TreeNode(9)
initial_tree_root.left.left = TreeNode(31)
initial_tree_root.left.right = TreeNode(25)
initial_tree_root.right.left = TreeNode(27)
initial_tree_root.right.right = TreeNode("DOG")

analyzer = TreeAnalyzer(initial_tree_root)

# Dynamic updates (you can add/remove nodes here)
initial_tree_root.left.left.left = TreeNode(42)  # Adding a node
initial_tree_root.right = None  # Removing a subtree

max_depth_result = analyzer.max_depth()
average_leaf_value_result = analyzer.average_leaf_value()

# Output the results after dynamic updates
print(f"Max Depth: {max_depth_result}")
print(f"Average Leaf Value: {average_leaf_value_result:.2f}")