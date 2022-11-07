import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    # empty tree
    def test_empty_str_inorder(self):
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_empty_str_tolist(self):
        self.assertEqual([], self.__tree.to_list())

    def test_empty_str_preorder(self):
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_empty_str_postorder(self):
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_empty_str_height(self):
        self.assertEqual(0, self.__tree.get_height())

    # insert elements into an empty tree
    def test_empty_ins_inorder(self):
        self.__tree.insert_element(20)
        self.assertEqual('[ 20 ]', self.__tree.in_order())

    def test_empty_ins_tolist(self):
        self.__tree.insert_element(20)
        self.assertEqual([20], self.__tree.to_list())

    def test_empty_ins_preorder(self):
        self.__tree.insert_element(20)
        self.assertEqual('[ 20 ]', self.__tree.pre_order())

    def test_empty_ins_postorder(self):
        self.__tree.insert_element(20)
        self.assertEqual('[ 20 ]', self.__tree.post_order())

    def test_empty_ins_height(self):
        self.__tree.insert_element(20)
        self.assertEqual(1, self.__tree.get_height())

    # insert elements into a tree with a height of one
    def test_one_perfect_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_one_perfect_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual([15, 20, 25], self.__tree.to_list())

    def test_one_perfect_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_one_perfect_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_one_perfect_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual(2, self.__tree.get_height())

    def test_one_ins_l_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 15, 20 ]', self.__tree.in_order())

    def test_one_ins_l_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual([15,20], self.__tree.to_list())

    def test_one_ins_l_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 20, 15 ]', self.__tree.pre_order())

    def test_one_ins_l_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 15, 20 ]', self.__tree.post_order())
    
    def test_one_ins_l_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual(2, self.__tree.get_height())
        
    def test_one_ins_r_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.assertEqual('[ 20, 25 ]', self.__tree.in_order())

    def test_one_ins_r_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.assertEqual([20, 25], self.__tree.to_list())

    def test_one_ins_r_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.assertEqual('[ 20, 25 ]', self.__tree.pre_order())

    def test_one_ins_r_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.assertEqual('[ 25, 20 ]', self.__tree.post_order())

    def test_one_ins_r_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.assertEqual(2, self.__tree.get_height())

    # Exception cases:
    # When the value already exists in the tree, raise an exception
    # and doesn't modify height
    def test_one_ins_exception_inorder(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(20)
        self.assertEqual('[ 20 ]', self.__tree.in_order())

    def test_one_ins_exception_tolist(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(20)
        self.assertEqual([20], self.__tree.to_list())

    def test_one_ins_exception_preorder(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(20)
        self.assertEqual('[ 20 ]', self.__tree.pre_order())

    def test_one_ins_exception_postorder(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(20)
        self.assertEqual('[ 20 ]', self.__tree.post_order())

    def test_one_ins_exception_height(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(20)
        self.assertEqual(1, self.__tree.get_height())

    # Insert into a tree with a height of 2
    # Insert into two, form a single line, single rotation
    # (Left-left case)
    def test_three_perfect_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 15, 17, 20, 22, 25, 27 ]', self.__tree.in_order())

    def test_three_perfect_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.assertEqual([10, 15, 17, 20, 22, 25, 27], self.__tree.to_list())

    def test_three_perfect_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.assertEqual('[ 20, 15, 10, 17, 25, 22, 27 ]', self.__tree.pre_order())

    def test_three_perfect_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 17, 15, 22, 27, 25, 20 ]', self.__tree.post_order())

    def test_three_perfect_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.assertEqual(3, self.__tree.get_height())

    def test_one_ins_two_inorder(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_one_ins_two_tolist(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual([15, 20, 25], self.__tree.to_list())

    def test_one_ins_two_preorder(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_one_ins_two_postorder(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_one_ins_two_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual(2, self.__tree.get_height())

    # Left-right case, double rotation
    def test_two_ins_lr_inorder(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_two_ins_lr_tolist(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.assertEqual([15, 20, 25], self.__tree.to_list())

    def test_two_ins_lr_preorder(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_two_ins_lr_postorder(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_lr_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.assertEqual(2, self.__tree.get_height())
    
    # Right-left case, no rotation
    def test_two_ins_nr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual('[ 15, 20, 22, 25 ]', self.__tree.in_order())

    def test_two_ins_nr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual([15, 20, 22, 25], self.__tree.to_list())

    def test_two_ins_nr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual('[ 20, 15, 25, 22 ]', self.__tree.pre_order())

    def test_two_ins_nr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual('[ 15, 22, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_nr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.assertEqual(3, self.__tree.get_height())

    # Right-right case, no rotation
    def test_two_ins_nr2_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual('[ 15, 20, 25, 30 ]', self.__tree.in_order())

    def test_two_ins_nr2_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual([15, 20, 25, 30], self.__tree.to_list())

    def test_two_ins_nr2_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual('[ 20, 15, 25, 30 ]', self.__tree.pre_order())

    def test_two_ins_nr2_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual('[ 15, 30, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_nr2_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual(3, self.__tree.get_height())
    
    # Exception cases
    def test_two_ins_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(15)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_two_ins_exception_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(15)
        self.assertEqual([15, 20, 25], self.__tree.to_list())

    def test_two_ins_exception_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(15)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_two_ins_exception_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(15)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_exception_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(15)
        self.assertEqual(2, self.__tree.get_height())

    # Insert into a tree with a height of three
    # Right-left case, double rotation
    def test_three_ins_rl_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(21)
        self.assertEqual('[ 15, 20, 21, 22, 25, 30 ]', self.__tree.in_order())

    def test_three_ins_rl_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(21)
        self.assertEqual([15, 20, 21, 22, 25, 30], self.__tree.to_list())

    def test_three_ins_rl_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(21)
        self.assertEqual('[ 22, 20, 15, 21, 25, 30 ]', self.__tree.pre_order())

    def test_three_ins_rl_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(21)
        self.assertEqual('[ 15, 21, 20, 30, 25, 22 ]', self.__tree.post_order())    

    def test_three_ins_rl_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(21)
        self.assertEqual(3, self.__tree.get_height())

    # Right-right case, single rotation
    def test_three_ins_rr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(27)
        self.assertEqual('[ 15, 20, 22, 25, 27, 30 ]', self.__tree.in_order())

    def test_three_ins_rr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(27)
        self.assertEqual([15, 20, 22, 25, 27, 30], self.__tree.to_list())

    def test_three_ins_rr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(27)
        self.assertEqual('[ 25, 20, 15, 22, 30, 27 ]', self.__tree.pre_order())

    def test_three_ins_rr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(27)
        self.assertEqual('[ 15, 22, 20, 27, 30, 25 ]', self.__tree.post_order())

    def test_three_ins_rr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(27)
        self.assertEqual(3, self.__tree.get_height())
    
    # left-right case, double rotation
    def test_three_ins_lr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.__tree.insert_element(18)
        self.assertEqual('[ 10, 15, 16, 18, 20, 25 ]', self.__tree.in_order())

    def test_three_ins_lr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.__tree.insert_element(18)
        self.assertEqual([10, 15, 16, 18, 20, 25], self.__tree.to_list())

    def test_three_ins_lr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.__tree.insert_element(18)
        self.assertEqual('[ 16, 15, 10, 20, 18, 25 ]', self.__tree.pre_order())

    def test_three_ins_lr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.__tree.insert_element(18)
        self.assertEqual('[ 10, 15, 18, 25, 20, 16 ]', self.__tree.post_order())

    def test_three_ins_lr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.__tree.insert_element(18)
        self.assertEqual(3, self.__tree.get_height())

    # Left-left case, single rotation
    def test_three_ins_ll_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(7)
        self.assertEqual('[ 7, 10, 15, 17, 20, 25 ]', self.__tree.in_order())

    def test_three_ins_ll_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(7)
        self.assertEqual([7, 10, 15, 17, 20, 25], self.__tree.to_list())

    def test_three_ins_ll_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(7)
        self.assertEqual('[ 15, 10, 7, 20, 17, 25 ]', self.__tree.pre_order())

    def test_three_ins_ll_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(7)
        self.assertEqual('[ 7, 10, 17, 25, 20, 15 ]', self.__tree.post_order())

    def test_three_ins_ll_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(7)
        self.assertEqual(3, self.__tree.get_height())

    # No rotation case
    def test_three_ins_nr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(24)
        self.assertEqual('[ 10, 15, 20, 22, 24, 25, 27 ]', self.__tree.in_order())

    def test_three_ins_nr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(24)
        self.assertEqual([10, 15, 20, 22, 24, 25, 27], self.__tree.to_list())

    def test_three_ins_nr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(24)
        self.assertEqual('[ 20, 15, 10, 25, 22, 24, 27 ]', self.__tree.pre_order())

    def test_three_ins_nr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(24)
        self.assertEqual('[ 10, 15, 24, 22, 27, 25, 20 ]', self.__tree.post_order())

    # Exception cases
    def test_three_ins_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(22)
        self.assertEqual('[ 10, 15, 17, 20, 22, 25, 30 ]', self.__tree.in_order())

    def test_three_ins_exception_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(22)
        self.assertEqual([10, 15, 17, 20, 22, 25, 30], self.__tree.to_list())

    def test_three_ins_exception_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(22)
        self.assertEqual('[ 20, 15, 10, 17, 25, 22, 30 ]', self.__tree.pre_order())

    def test_three_ins_exception_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(22)
        self.assertEqual('[ 10, 17, 15, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_three_ins_exception_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(22)
        self.assertEqual(3, self.__tree.get_height())


    # Below are tests for remove_element(value)

    # Remove a value from an empty tree
    def test_empty_rem_inorder(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_empty_rem_tolist(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
        self.assertEqual([], self.__tree.to_list())

    def test_empty_rem_preorder(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.pre_order())

    def test_empty_rem_postorder(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.post_order())

    def test_empty_rem_height(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
        self.assertEqual(0, self.__tree.get_height())

    # Remove a value from a tree with a height of one
    def test_one_rem_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_one_rem_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual([], self.__tree.to_list())

    def test_one_rem_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_one_rem_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_one_rem_height(self):
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual(0, self.__tree.get_height())

    # Exception cases for removing an element from a tree with a height of one
    def test_one_rem_exception_inorder(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(21)
        self.assertEqual('[ 20 ]', self.__tree.in_order())

    def test_one_rem_exception_tolist(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(21)
        self.assertEqual([20], self.__tree.to_list())

    def test_one_rem_exception_preorder(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(21)
        self.assertEqual('[ 20 ]', self.__tree.pre_order())

    def test_one_rem_exception_postorder(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(21)
        self.assertEqual('[ 20 ]', self.__tree.post_order())

    def test_one_rem_exception_height(self):
        self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(21)
        self.assertEqual(1, self.__tree.get_height())

    # Remove an element from a tree with a height of two and updates height
    def test_two_imperfect_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15 ]', self.__tree.in_order())

    def test_two_imperfect_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(20)
        self.assertEqual([15], self.__tree.to_list())

    def test_two_imperfect_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15 ]', self.__tree.pre_order())

    def test_two_imperfect_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15 ]', self.__tree.post_order())

    def test_two_imperfect_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(15)
        self.assertEqual(1, self.__tree.get_height())

    # Remove an element from a tree with a height of two, height remains unchanged
    # Remove root, no rotation
    def test_two_rem_root_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 25 ]', self.__tree.in_order())

    def test_two_rem_root_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(20)
        self.assertEqual([15, 25], self.__tree.to_list())

    def test_two_rem_root_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(20)
        self.assertEqual('[ 25, 15 ]', self.__tree.pre_order())

    def test_two_rem_root_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 25 ]', self.__tree.post_order())

    def test_two_rem_root_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(20)
        self.assertEqual(2, self.__tree.get_height())

    # Remove leaf, no rotation
    def test_two_rem_leaf_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('[ 15, 20 ]', self.__tree.in_order())

    def test_two_rem_leaf_tolist(self):
            self.__tree.insert_element(20)
            self.__tree.insert_element(15)
            self.__tree.insert_element(25)
            self.__tree.remove_element(25)
            self.assertEqual([15, 20], self.__tree.to_list())

    def test_two_rem_leaf_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('[ 20, 15 ]', self.__tree.pre_order())

    def test_two_rem_leaf_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('[ 15, 20 ]', self.__tree.post_order())

    def test_two_rem_leaf_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual(2, self.__tree.get_height())

    # Exception cases for removing an element from a tree with a height of two
    def test_two_rem_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_two_rem_exception_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual([15, 20, 25], self.__tree.to_list())

    def test_two_rem_exception_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_two_rem_exception_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_two_rem_exception_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual(2, self.__tree.get_height())

    # Remove an element from a tree with a height of three
    def test_three_rem_nr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_three_rem_nr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual([15, 20, 25], self.__tree.to_list())

    def test_three_rem_nr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_three_rem_nr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_three_rem_nr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual(2, self.__tree.get_height())

    # Left-left case, single rotation
    def test_three_rem_leaf_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 15, 25 ]', self.__tree.in_order())

    def test_three_rem_leaf_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual([10, 15, 25], self.__tree.to_list())

    def test_three_rem_leaf_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 10, 25 ]', self.__tree.pre_order())

    def test_three_rem_leaf_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 25, 15 ]', self.__tree.post_order())

    def test_three_rem_leaf_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual(2, self.__tree.get_height())

    # Left-right double rotation
    def test_three_rem_root_lr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 17, 25 ]', self.__tree.in_order())

    def test_three_rem_root_lr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.remove_element(20)
        self.assertEqual([15, 17, 25], self.__tree.to_list())

    def test_three_rem_root_lr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.remove_element(20)
        self.assertEqual('[ 17, 15, 25 ]', self.__tree.pre_order())

    def test_three_rem_root_lr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 25, 17 ]', self.__tree.post_order())

    def test_three_rem_root_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.remove_element(20)
        self.assertEqual(2, self.__tree.get_height())

    # Right-right single rotation
    def test_three_rem_rr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(15)
        self.assertEqual('[ 20, 22, 25, 27 ]', self.__tree.in_order())

    def test_three_rem_rr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(15)
        self.assertEqual([20, 22, 25, 27], self.__tree.to_list())

    def test_three_rem_rr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(15)
        self.assertEqual('[ 25, 20, 22, 27 ]', self.__tree.pre_order())

    def test_three_rem_rr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(15)
        self.assertEqual('[ 22, 20, 27, 25 ]', self.__tree.post_order())

    def test_three_rem_rr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(15)
        self.assertEqual(3, self.__tree.get_height())

    # No rotation case
    def test_three_rem_root_nr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 22, 25, 27 ]', self.__tree.in_order())

    def test_three_rem_root_nr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(20)
        self.assertEqual([15, 22, 25, 27], self.__tree.to_list())

    def test_three_rem_root_nr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(20)
        self.assertEqual('[ 22, 15, 25, 27 ]', self.__tree.pre_order())

    def test_three_rem_root_nr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 27, 25, 22 ]', self.__tree.post_order())

    def test_three_rem_root_nr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.remove_element(20)
        self.assertEqual(3, self.__tree.get_height())

    # Exception cases for removing an element from a tree with a height of three
    def test_three_rem_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 10, 15, 17, 20, 22, 25 ]', self.__tree.in_order())

    def test_three_rem_exception_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual([10, 15, 17, 20, 22, 25], self.__tree.to_list())

    def test_three_rem_exception_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 20, 15, 10, 17, 25, 22 ]', self.__tree.pre_order())

    def test_three_rem_exception_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 10, 17, 15, 22, 25, 20 ]', self.__tree.post_order())

    def test_three_rem_exception_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual(3, self.__tree.get_height())

    # Remove an element from a tree with a height of four
    def test_four_rem_root_r_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 15, 22, 25, 26, 27, 30 ]', self.__tree.in_order())

    def test_four_rem_root_r_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(20)
        self.assertEqual([10, 15, 22, 25, 26, 27, 30], self.__tree.to_list())

    def test_four_rem_root_r_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(20)
        self.assertEqual('[ 22, 15, 10, 27, 25, 26, 30 ]', self.__tree.pre_order())

    def test_four_rem_root_r_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 15, 26, 25, 30, 27, 22 ]', self.__tree.post_order())

    def test_four_rem_root_r_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(20)
        self.assertEqual(4, self.__tree.get_height())

    # Right-right case, single rotation
    def test_four_rem_rr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(10)
        self.assertEqual('[ 15, 20, 22, 25, 26, 27, 30 ]', self.__tree.in_order())

    def test_four_rem_rr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(10)
        self.assertEqual([15, 20, 22, 25, 26, 27, 30], self.__tree.to_list())

    def test_four_rem_rr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(10)
        self.assertEqual('[ 25, 20, 15, 22, 27, 26, 30 ]', self.__tree.pre_order())

    def test_four_rem_rr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(10)
        self.assertEqual('[ 15, 22, 20, 26, 30, 27, 25 ]', self.__tree.post_order())

    def test_four_rem_rr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(10)
        self.assertEqual(3, self.__tree.get_height())

    # No rotation case
    def test_four_rem_nr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(25)
        self.assertEqual('[ 10, 15, 20, 22, 26, 27, 30 ]', self.__tree.in_order())

    def test_four_rem_nr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(25)
        self.assertEqual([10, 15, 20, 22, 26, 27, 30], self.__tree.to_list())

    def test_four_rem_nr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(25)
        self.assertEqual('[ 20, 15, 10, 26, 22, 27, 30 ]', self.__tree.pre_order())

    def test_four_rem_nr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(25)
        self.assertEqual('[ 10, 15, 22, 30, 27, 26, 20 ]', self.__tree.post_order())

    def test_four_rem_nr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(25)
        self.assertEqual(4, self.__tree.get_height())

    # Remove leaf, right-right case, single rotation
    def test_four_rem_leaf_rr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(22)
        self.assertEqual('[ 10, 15, 20, 25, 26, 27, 30 ]', self.__tree.in_order())

    def test_four_rem_leaf_rr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(22)
        self.assertEqual([10, 15, 20, 25, 26, 27, 30], self.__tree.to_list())

    def test_four_rem_leaf_rr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(22)
        self.assertEqual('[ 20, 15, 10, 27, 25, 26, 30 ]', self.__tree.pre_order())

    def test_four_rem_leaf_rr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(22)
        self.assertEqual('[ 10, 15, 26, 25, 30, 27, 20 ]', self.__tree.post_order())

    def test_four_rem_leaf_rr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(26)
        self.__tree.insert_element(30)
        self.__tree.remove_element(22)
        self.assertEqual(4, self.__tree.get_height())
    
    # Right-left case, double rotation
    def test_four_rem_inner_rr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(21)
        self.__tree.insert_element(24)
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 20, 21, 22, 24, 25, 27 ]', self.__tree.in_order())

    def test_four_rem_inner_rr_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(21)
        self.__tree.insert_element(24)
        self.__tree.remove_element(15)
        self.assertEqual([10, 20, 21, 22, 24, 25, 27], self.__tree.to_list())

    def test_four_rem_inner_rr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(21)
        self.__tree.insert_element(24)
        self.__tree.remove_element(15)
        self.assertEqual('[ 22, 20, 10, 21, 25, 24, 27 ]', self.__tree.pre_order())

    def test_four_rem_inner_rr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(21)
        self.__tree.insert_element(24)
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 21, 20, 24, 27, 25, 22 ]', self.__tree.post_order())

    def test_four_rem_inner_rr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(22)
        self.__tree.insert_element(27)
        self.__tree.insert_element(21)
        self.__tree.insert_element(24)
        self.__tree.remove_element(15)
        self.assertEqual(3, self.__tree.get_height())

    # Exception cases for removing from a tree with a height of four
    def test_four_rem_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(12)
        self.__tree.insert_element(24)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(35)
        self.assertEqual('[ -1, 10, 12, 15, 17, 20, 22, 24, 25, 30 ]', self.__tree.in_order())

    def test_four_rem_exception_tolist(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(12)
        self.__tree.insert_element(24)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(35)
        self.assertEqual([-1, 10, 12, 15, 17, 20, 22, 24, 25, 30], self.__tree.to_list())

    def test_four_rem_exception_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(12)
        self.__tree.insert_element(24)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(35)
        self.assertEqual('[ 20, 15, 10, -1, 12, 17, 25, 22, 24, 30 ]', self.__tree.pre_order())

    def test_four_rem_exception_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(12)
        self.__tree.insert_element(24)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(35)
        self.assertEqual('[ -1, 12, 10, 17, 15, 24, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_four_rem_exception_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(12)
        self.__tree.insert_element(24)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(35)
        self.assertEqual(4, self.__tree.get_height())

    # Inserting and removing mixed together
    # def test_rem_ins_mix1_inorder(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.insert_element(22)
    #     self.__tree.insert_element(21)
    #     self.assertEqual('[ 15, 17, 20, 21, 22 ]', self.__tree.in_order())

    # def test_rem_ins_mix1_preorder(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.insert_element(22)
    #     self.__tree.insert_element(21)
    #     self.assertEqual('[ 20, 15, 17, 22, 21 ]', self.__tree.pre_order())

    # def test_rem_ins_mix1_postorder(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.insert_element(22)
    #     self.__tree.insert_element(21)
    #     self.assertEqual('[ 17, 15, 21, 22, 20 ]', self.__tree.post_order())

    # def test_rem_ins_mix1_height(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.insert_element(22)
    #     self.__tree.insert_element(21)
    #     self.assertEqual(3, self.__tree.get_height())

    # def test_rem_ins_mix2_inorder(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(17)
    #     self.__tree.insert_element(22)
    #     self.__tree.remove_element(20)
    #     self.__tree.remove_element(15)
    #     self.__tree.remove_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.remove_element(22)
    #     self.assertEqual('[ ]', self.__tree.in_order())

    # def test_rem_ins_mix2_preorder(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(17)
    #     self.__tree.insert_element(22)
    #     self.__tree.remove_element(20)
    #     self.__tree.remove_element(15)
    #     self.__tree.remove_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.remove_element(22)
    #     self.assertEqual('[ ]', self.__tree.pre_order())

    # def test_rem_ins_mix2_postorder(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(17)
    #     self.__tree.insert_element(22)
    #     self.__tree.remove_element(20)
    #     self.__tree.remove_element(15)
    #     self.__tree.remove_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.remove_element(22)
    #     self.assertEqual('[ ]', self.__tree.post_order())

    # def test_rem_ins_mix2_height(self):
    #     self.__tree.insert_element(20)
    #     self.__tree.insert_element(15)
    #     self.__tree.insert_element(25)
    #     self.__tree.insert_element(17)
    #     self.__tree.insert_element(22)
    #     self.__tree.remove_element(20)
    #     self.__tree.remove_element(15)
    #     self.__tree.remove_element(17)
    #     self.__tree.remove_element(25)
    #     self.__tree.remove_element(22)
    #     self.assertEqual(0, self.__tree.get_height())


if __name__ == '__main__':
  unittest.main()


