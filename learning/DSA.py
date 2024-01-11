class TreeAnalyzer:
    def __init__(self, root=None):
        self.root = root

    def max_depth(self):
        """Returns the maximum depth of the tree."""
        if self.root is None:
            return 0
        else:
            left_depth = self.max_depth(self.root.left)
            right_depth = self.max_depth(self.root.right)
            return max(left_depth, right_depth) + 1

    def average_leaf_value(self):
        """Calculates the average value of leaf nodes."""
        sum_of_leaf_values = 0
        num_leaf_nodes = 0

        def traverse(node):
            nonlocal sum_of_leaf_values, num_leaf_nodes
            if node is None:
                return
            if not node.left and not node.right:  # Leaf node
                if isinstance(node.value, (int, float)):
                    sum_of_leaf_values += node.value
                    num_leaf_nodes += 1
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return sum_of_leaf_values / num_leaf_nodes if num_leaf_nodes > 0 else 0

analyzer = TreeAnalyzer(initial_tree_root)
max_depth_result = analyzer.max_depth()
print(f"Average Leaf Value: {analyzer.average_leaf_value():.2f}")
