import unittest

from BinaryNode import BinaryNode


class BinaryNodeTests(unittest.TestCase):
    def test_foo(self):
        tree = BinaryNode(
            10,
            left=BinaryNode(
                5,
                left=BinaryNode(2),
                right=BinaryNode(
                    6,
                    right=BinaryNode(7))),
            right=BinaryNode(
                15, left=BinaryNode(11)
            )
        )

        self.assertEqual(
            tree.left.right.right.value,
            7)
        self.assertEqual(tree[0], 2)
        self.assertEqual(tree[1], 5)
        self.assertIn(11, tree)
        self.assertNotIn(17, tree)
        self.assertEqual(len(tree), 7)
        self.assertEqual(tree.count(2), 1)
        self.assertEqual(tree.index(2), 0)


if __name__ == '__main__':
    unittest.main()
