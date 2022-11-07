import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    # empty tree
    def test_empty_str_inorder(self):
        self.assertEqual('[ ]', self.__tree.in_order())

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
    def test_one_ins_l_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.assertEqual('[ 15, 20 ]', self.__tree.in_order())

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

    def test_one_ins_two_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

    def test_one_ins_two_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual('[ 20, 15, 25 ]', self.__tree.pre_order())

    def test_one_ins_two_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual('[ 15, 25, 20 ]', self.__tree.post_order())

    def test_one_ins_two_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual(2, self.__tree.get_height())

    # When inserting an element into a tree with a height of two
    def test_two_ins_rl_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual('[ 15, 20, 22, 25 ]', self.__tree.in_order())

    def test_two_ins_rl_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual('[ 20, 15, 25, 22 ]', self.__tree.pre_order())

    def test_two_ins_rl_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual('[ 15, 22, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_rl_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.assertEqual(3, self.__tree.get_height())

    def test_two_ins_rr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.assertEqual('[ 15, 20, 22, 25, 30 ]', self.__tree.in_order())

    def test_two_ins_rr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.assertEqual('[ 20, 15, 25, 22, 30 ]', self.__tree.pre_order())

    def test_two_ins_rr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.assertEqual('[ 15, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_rr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.assertEqual(3, self.__tree.get_height())

    def test_two_ins_ll_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 15, 20, 25 ]', self.__tree.in_order())

    def test_two_ins_ll_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.assertEqual('[ 20, 15, 10, 25 ]', self.__tree.pre_order())

    def test_two_ins_ll_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 15, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_ll_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.assertEqual(3, self.__tree.get_height())

    def test_two_ins_lr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.assertEqual('[ 15, 17, 20, 25 ]', self.__tree.in_order())

    def test_two_ins_lr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.assertEqual('[ 20, 15, 17, 25 ]', self.__tree.pre_order())

    def test_two_ins_lr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.assertEqual('[ 17, 15, 25, 20 ]', self.__tree.post_order())

    def test_two_ins_lr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.assertEqual(3, self.__tree.get_height())
    
    # Exception cases
    def test_two_ins_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(15)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

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

    # When inserting an element to a tree with a height of three
    def test_three_ins_l1r_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)

        self.__tree.insert_element(12)
        self.assertEqual('[ 10, 12, 15, 17, 20, 22, 25, 30 ]', self.__tree.in_order())

    def test_three_ins_l1r_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)

        self.__tree.insert_element(12)
        self.assertEqual('[ 20, 15, 10, 12, 17, 25, 22, 30 ]', self.__tree.pre_order())

    def test_three_ins_l1r_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)

        self.__tree.insert_element(12)
        self.assertEqual('[ 12, 10, 17, 15, 22, 30, 25, 20 ]', self.__tree.post_order())    

    def test_three_ins_l1r_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.assertEqual(4, self.__tree.get_height())

    def test_three_ins_l2l_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)

        self.__tree.insert_element(16)
        self.assertEqual('[ 10, 12, 15, 16, 17, 20, 22, 25, 30 ]', self.__tree.in_order())

    def test_three_ins_l2l_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)

        self.__tree.insert_element(16)
        self.assertEqual('[ 20, 15, 10, 12, 17, 16, 25, 22, 30 ]', self.__tree.pre_order())

    def test_three_ins_l2l_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)

        self.__tree.insert_element(16)
        self.assertEqual('[ 12, 10, 16, 17, 15, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_three_ins_l2l_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)
        self.assertEqual(4, self.__tree.get_height())
        
    def test_three_ins_r1r_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)

        self.__tree.insert_element(24)
        self.assertEqual('[ 10, 12, 15, 16, 17, 20, 22, 24, 25, 30 ]', self.__tree.in_order())

    def test_three_ins_r1r_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)

        self.__tree.insert_element(24)
        self.assertEqual('[ 20, 15, 10, 12, 17, 16, 25, 22, 24, 30 ]', self.__tree.pre_order())

    def test_three_ins_r1r_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)

        self.__tree.insert_element(24)
        self.assertEqual('[ 12, 10, 16, 17, 15, 24, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_three_ins_r1r_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)
        self.__tree.insert_element(24)
        self.assertEqual(4, self.__tree.get_height())

    def test_three_ins_r2l_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)
        self.__tree.insert_element(24)

        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 12, 15, 16, 17, 20, 22, 24, 25, 27, 30 ]', self.__tree.in_order())

    def test_three_ins_r2l_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)
        self.__tree.insert_element(24)

        self.__tree.insert_element(27)
        self.assertEqual('[ 20, 15, 10, 12, 17, 16, 25, 22, 24, 30, 27 ]', self.__tree.pre_order())

    def test_three_ins_r2l_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)
        self.__tree.insert_element(24)

        self.__tree.insert_element(27)
        self.assertEqual('[ 12, 10, 16, 17, 15, 24, 22, 27, 30, 25, 20 ]', self.__tree.post_order())

    def test_three_ins_r2l_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(12)
        self.__tree.insert_element(16)
        self.__tree.insert_element(24)
        self.__tree.insert_element(27)
        self.assertEqual(4, self.__tree.get_height())

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

    
    


    # Below are tests for remove_element()

    # Remove a value from an empty tree
    def test_empty_rem_inorder(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
        self.assertEqual('[ ]', self.__tree.in_order())

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
        self.__tree.remove_element(15)
        self.assertEqual('[ 20 ]', self.__tree.in_order())

    def test_two_imperfect_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(15)
        self.assertEqual('[ 20 ]', self.__tree.pre_order())

    def test_two_imperfect_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(15)
        self.assertEqual('[ 20 ]', self.__tree.post_order())

    def test_two_imperfect_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.remove_element(15)
        self.assertEqual(1, self.__tree.get_height())

    # Remove an element from a tree with a height of two, height remains unchanged
    def test_two_rem_l_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(15)
        self.assertEqual('[ 20, 25 ]', self.__tree.in_order())

    def test_two_rem_l_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(15)
        self.assertEqual('[ 20, 25 ]', self.__tree.pre_order())

    def test_two_rem_l_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(15)
        self.assertEqual('[ 25, 20 ]', self.__tree.post_order())

    def test_two_rem_l_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(15)
        self.assertEqual(2, self.__tree.get_height())

    def test_two_rem_r_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('[ 15, 20 ]', self.__tree.in_order())

    def test_two_rem_r_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('[ 20, 15 ]', self.__tree.pre_order())

    def test_two_rem_r_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('[ 15, 20 ]', self.__tree.post_order())

    def test_two_rem_r_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual(2, self.__tree.get_height())

    def test_two_rem_root_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(20)
        self.assertEqual('[ 15, 25 ]', self.__tree.in_order())

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

    # Exception cases for removing an element from a tree with a height of two
    def test_two_rem_exception_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
        self.assertEqual('[ 15, 20, 25 ]', self.__tree.in_order())

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
    def test_three_imperfect_rem_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 20, 25 ]', self.__tree.in_order())

    def test_three_imperfect_rem_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.assertEqual('[ 20, 10, 25 ]', self.__tree.pre_order())

    def test_three_imperfect_rem_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 25, 20 ]', self.__tree.post_order())

    def test_three_imperfect_rem_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.assertEqual(2, self.__tree.get_height())

    def test_three_rem_leaf_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(17)
        self.assertEqual('[ 10, 15, 20, 22, 25 ]', self.__tree.in_order())

    def test_three_rem_leaf_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(17)
        self.assertEqual('[ 20, 15, 10, 25, 22 ]', self.__tree.pre_order())

    def test_three_rem_leaf_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(17)
        self.assertEqual('[ 10, 15, 22, 25, 20 ]', self.__tree.post_order())

    def test_three_rem_leaf_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(17)
        self.assertEqual(3, self.__tree.get_height())

    def test_three_rem_root_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 15, 17, 22, 25 ]', self.__tree.in_order())

    def test_three_rem_root_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(20)
        self.assertEqual('[ 22, 15, 10, 17, 25 ]', self.__tree.pre_order())

    def test_three_rem_root_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 17, 15, 25, 22 ]', self.__tree.post_order())

    def test_three_rem_root_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(20)
        self.assertEqual(3, self.__tree.get_height())

    def test_three_rem_innerl_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(25)
        self.assertEqual('[ 10, 15, 17, 20, 22 ]', self.__tree.in_order())

    def test_three_rem_innerl_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(25)
        self.assertEqual('[ 20, 15, 10, 17, 22 ]', self.__tree.pre_order())

    def test_three_rem_innerl_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(25)
        self.assertEqual('[ 10, 17, 15, 22, 20 ]', self.__tree.post_order())

    def test_three_rem_innerl_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(25)
        self.assertEqual(3, self.__tree.get_height())

    def test_three_rem_innerr_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 17, 20, 22, 25 ]', self.__tree.in_order())

    def test_three_rem_innerr_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(15)
        self.assertEqual('[ 20, 17, 10, 25, 22 ]', self.__tree.pre_order())

    def test_three_rem_innerr_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 17, 22, 25, 20 ]', self.__tree.post_order())

    def test_three_rem_innerr_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)

        self.__tree.remove_element(15)
        self.assertEqual(3, self.__tree.get_height())

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

    # Exception cases for removing an element from a tree with a height of three
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
    def test_four_imperfect_rem_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.remove_element(10)
        self.assertEqual('[ -1, 15, 17, 20, 22, 25, 30 ]', self.__tree.in_order())

    def test_four_imperfect_rem_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.remove_element(10)
        self.assertEqual('[ 20, 15, -1, 17, 25, 22, 30 ]', self.__tree.pre_order())

    def test_four_imperfect_rem_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.remove_element(10)
        self.assertEqual('[ -1, 17, 15, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_four_imperfect_rem_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.insert_element(30)
        self.__tree.insert_element(-1)
        self.__tree.remove_element(10)
        self.assertEqual(3, self.__tree.get_height())

    def test_four_rem_leaf_inorder(self):
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

        self.__tree.remove_element(12)
        self.assertEqual('[ -1, 10, 15, 17, 20, 22, 24, 25, 30 ]', self.__tree.in_order())

    def test_four_rem_leaf_preorder(self):
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

        self.__tree.remove_element(12)
        self.assertEqual('[ 20, 15, 10, -1, 17, 25, 22, 24, 30 ]', self.__tree.pre_order())

    def test_four_rem_leaf_postorder(self):
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

        self.__tree.remove_element(12)
        self.assertEqual('[ -1, 10, 17, 15, 24, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_four_rem_leaf_height(self):
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

        self.__tree.remove_element(12)
        self.assertEqual(4, self.__tree.get_height())

    def test_four_rem_inner1_inorder(self):
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

        self.__tree.remove_element(22)
        self.assertEqual('[ -1, 10, 12, 15, 17, 20, 24, 25, 30 ]', self.__tree.in_order())

    def test_four_rem_inner1_preorder(self):
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

        self.__tree.remove_element(22)
        self.assertEqual('[ 20, 15, 10, -1, 12, 17, 25, 24, 30 ]', self.__tree.pre_order())

    def test_four_rem_inner1_postorder(self):
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

        self.__tree.remove_element(22)
        self.assertEqual('[ -1, 12, 10, 17, 15, 24, 30, 25, 20 ]', self.__tree.post_order())

    def test_four_rem_inner1_height(self):
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

        self.__tree.remove_element(22)
        self.assertEqual(4, self.__tree.get_height())

    def test_four_rem_inner2_inorder(self):
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

        self.__tree.remove_element(15)
        self.assertEqual('[ -1, 10, 12, 17, 20, 22, 24, 25, 30 ]', self.__tree.in_order())

    def test_four_rem_inner2_preorder(self):
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

        self.__tree.remove_element(15)
        self.assertEqual('[ 20, 17, 10, -1, 12, 25, 22, 24, 30 ]', self.__tree.pre_order())

    def test_four_rem_inner2_postorder(self):
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

        self.__tree.remove_element(15)
        self.assertEqual('[ -1, 12, 10, 17, 24, 22, 30, 25, 20 ]', self.__tree.post_order())

    def test_four_rem_inner2_height(self):
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

        self.__tree.remove_element(15)
        self.assertEqual(4, self.__tree.get_height())
        
    def test_four_rem_root_inorder(self):
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

        self.__tree.remove_element(20)
        self.assertEqual('[ -1, 10, 12, 15, 17, 22, 24, 25, 30 ]', self.__tree.in_order())

    def test_four_rem_root_preorder(self):
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

        self.__tree.remove_element(20)
        self.assertEqual('[ 22, 15, 10, -1, 12, 17, 25, 24, 30 ]', self.__tree.pre_order())

    def test_four_rem_root_postorder(self):
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

        self.__tree.remove_element(20)
        self.assertEqual('[ -1, 12, 10, 17, 15, 24, 30, 25, 22 ]', self.__tree.post_order())

    def test_four_rem_root_height(self):
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

        self.__tree.remove_element(20)
        self.assertEqual(4, self.__tree.get_height())

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
    def test_rem_ins_mix1_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.remove_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(21)
        self.assertEqual('[ 15, 17, 20, 21, 22 ]', self.__tree.in_order())

    def test_rem_ins_mix1_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.remove_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(21)
        self.assertEqual('[ 20, 15, 17, 22, 21 ]', self.__tree.pre_order())

    def test_rem_ins_mix1_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.remove_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(21)
        self.assertEqual('[ 17, 15, 21, 22, 20 ]', self.__tree.post_order())

    def test_rem_ins_mix1_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.remove_element(25)
        self.__tree.insert_element(22)
        self.__tree.insert_element(21)
        self.assertEqual(3, self.__tree.get_height())

    def test_rem_ins_mix2_inorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.remove_element(20)
        self.__tree.remove_element(15)
        self.__tree.remove_element(17)
        self.__tree.remove_element(25)
        self.__tree.remove_element(22)
        self.assertEqual('[ ]', self.__tree.in_order())

    def test_rem_ins_mix2_preorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.remove_element(20)
        self.__tree.remove_element(15)
        self.__tree.remove_element(17)
        self.__tree.remove_element(25)
        self.__tree.remove_element(22)
        self.assertEqual('[ ]', self.__tree.pre_order())

    def test_rem_ins_mix2_postorder(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.remove_element(20)
        self.__tree.remove_element(15)
        self.__tree.remove_element(17)
        self.__tree.remove_element(25)
        self.__tree.remove_element(22)
        self.assertEqual('[ ]', self.__tree.post_order())

    def test_rem_ins_mix2_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(17)
        self.__tree.insert_element(22)
        self.__tree.remove_element(20)
        self.__tree.remove_element(15)
        self.__tree.remove_element(17)
        self.__tree.remove_element(25)
        self.__tree.remove_element(22)
        self.assertEqual(0, self.__tree.get_height())


if __name__ == '__main__':
  unittest.main()


