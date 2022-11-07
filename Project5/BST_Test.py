import unittest
from Binary_Search_Tree import Binary_Search_Tree

class DSQTester(unittest.TestCase):


    def setUp(self):
        self.__tree = Binary_Search_Tree()

    # First Test Insertion

    # Test empty string methods

    def test_empty_str(self):
        self.assertEqual('[ ]', str(self.__tree))

    def test_empty_in_order(self):
        self.assertEqual('[ ]', str(self.__tree.in_order()))

    def test_empty_pre_order(self):
        self.assertEqual('[ ]', str(self.__tree.pre_order()))

    def test_empty_post_order(self):
        self.assertEqual('[ ]', str(self.__tree.post_order()))

    def test_empty_to_list(self):
        self.assertEqual([], self.__tree.to_list())

    def test_get_height_empty(self):
        self.assertEqual(0,self.__tree.get_height())


    # Test insertion into an empty tree

    def test_insert_empty_with_in_order(self):
        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree.in_order()))

    def test_insert_empty_with_pre_order(self):
        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree.pre_order()))

    def test_insert_empty_with_post_order(self):
        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree.post_order()))

    def test_empty_to_list(self):
        self.__tree.insert_element(1)
        self.assertEqual([1], self.__tree.to_list())

    def test_get_height_one(self):
        self.__tree.insert_element(1)
        self.assertEqual(1,self.__tree.get_height())

    # Test insertion into a height one tree

    # Test inserting a repetitive element
    def test_insert_repetitive_with_one_in_order(self):
        self.__tree.insert_element(1)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree.in_order()))

    def test_insert_repetitive_with_one_pre_order(self):
        self.__tree.insert_element(1)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree.pre_order()))

    def test_insert_repetitive_with_one_post_order(self):
        self.__tree.insert_element(1)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree.post_order()))

    def test_insert_repetitive_with_one_to_list(self):
        self.__tree.insert_element(1)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(1)
        self.assertEqual([1], self.__tree.to_list())

    def test_insert_repetitive_with_one_get_height(self):
        self.__tree.insert_element(1)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(1)
        self.assertEqual(1, self.__tree.get_height())

    # Test insert a large element

    def test_insert_R_into_one_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2 ]', str(self.__tree.in_order()))

    def test_insert_R_into_one_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2 ]', str(self.__tree.pre_order()))

    def test_insert_R_into_one_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 2, 1 ]', str(self.__tree.post_order()))

    def test_insert_R_into_one_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual([1,2], self.__tree.to_list())

    def test_get_height_after_insert_R_into_one(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual(2,self.__tree.get_height())

    # Test insert a small element

    def test_insert_Left_into_one_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.assertEqual('[ 0, 1 ]', str(self.__tree.in_order()))

    def test_insert_Left_into_one_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.assertEqual('[ 1, 0 ]', str(self.__tree.pre_order()))

    def test_insert_Left_into_one_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.assertEqual('[ 0, 1 ]', str(self.__tree.post_order()))

    def test_insert_Left_into_one_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.assertEqual([0,1], self.__tree.to_list())

    def test_get_height_after_insert_R_into_two(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.assertEqual(2,self.__tree.get_height())


    # Test insert into an tree of height 2

    # Test insert a repetitive element into a height 2 tree

    def test_insert_repetitive_into_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(0)
        self.assertEqual('[ 0, 1 ]', str(self.__tree.in_order()))

    def test_insert_repetitive_into_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(0)
        self.assertEqual('[ 1, 0 ]', str(self.__tree.pre_order()))

    def test_insert_repetitive_into_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(0)
        self.assertEqual('[ 0, 1 ]', str(self.__tree.post_order()))

    def test_insert_repetitive_into_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(0)
        self.assertEqual([0,1], self.__tree.to_list())

    def test_get_height_after_repetitive_insertion_two(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(0)
        self.assertEqual(2,self.__tree.get_height())


    # Test insert a large element into a complete tree of height 2

    def test_insert_right_into_complete_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.assertEqual('[ 0, 1, 3 ]', str(self.__tree.in_order()))

    def test_insert_right_into_complete_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.assertEqual('[ 1, 0, 3 ]', str(self.__tree.pre_order()))

    def test_insert_right_into_complete_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.assertEqual('[ 0, 3, 1 ]', str(self.__tree.post_order()))

    def test_insert_right_into_complete_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.assertEqual([0,1,3], self.__tree.to_list())

    def test_get_height_after_insert_right_into_two_complete(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.assertEqual(2,self.__tree.get_height())

    # Test insert a small element into an incomplete tree of height 2

    def test_insert_left_into_imcomplete_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.assertEqual('[ 0, 1, 2 ]', str(self.__tree.in_order()))

    def test_insert_left_into_imcomplete_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.assertEqual('[ 1, 0, 2 ]', str(self.__tree.pre_order()))

    def test_insert_left_into_incomplete_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.assertEqual('[ 0, 2, 1 ]', str(self.__tree.post_order()))

    def test_insert_left_into_imcomplete_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.assertEqual([0,1,2], self.__tree.to_list())

    def test_get_height_after_insert_into_two_incomplete(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.assertEqual(2,self.__tree.get_height())


    # Test insert a largest element into an incomplete tree of height 2

    def test_insert_RR_into_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__tree.in_order()))

    def test_insert_RR_into_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual('[ 2, 1, 3 ]', str(self.__tree.pre_order()))

    def test_insert_RR_into_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual('[ 1, 3, 2 ]', str(self.__tree.post_order()))

    def test_insert_RR_into_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual([1,2,3], self.__tree.to_list())

    def test_get_height_after_insert_RR_into_two_incomplete(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual(2,self.__tree.get_height())

    # Test insert a large element into an incomplete tree of height 2
    # Need double rotationx

    def test_insert_RL_into_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.assertEqual('[ 1, 1.5, 2 ]', str(self.__tree.in_order()))

    def test_insert_RL_into_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.assertEqual('[ 1.5, 1, 2 ]', str(self.__tree.pre_order()))

    def test_insert_RL_into_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.assertEqual('[ 1, 2, 1.5 ]', str(self.__tree.post_order()))

    def test_insert_RL_into_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.assertEqual([1,1.5,2], self.__tree.to_list())

    def test_get_height_after_insert_RL_into_two_incomplete(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.assertEqual(2,self.__tree.get_height())

    # Test insert a smallest element into a complete tree of height 2

    def test_insert_LL_into_complete_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.assertEqual('[ -1, 0, 1 ]', str(self.__tree.in_order()))

    def test_insert_LL_into_complete_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.assertEqual('[ 0, -1, 1 ]', str(self.__tree.pre_order()))

    def test_insert_LL_into_complete_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.assertEqual('[ -1, 1, 0 ]', str(self.__tree.post_order()))

    def test_insert_LL_into_complete_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.assertEqual([-1,0,1], self.__tree.to_list())

    def test_get_height_after_insert_LL_into_two_complete(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.assertEqual(2,self.__tree.get_height())

    # Test insert a small element into a complete tree of height 2
    # Needs double rotation

    def test_insert_LR_into_complete_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.assertEqual('[ 0, 0.5, 1 ]', str(self.__tree.in_order()))

    def test_insert_LR_into_complete_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.assertEqual('[ 0.5, 0, 1 ]', str(self.__tree.pre_order()))

    def test_insert_LR_into_complete_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.assertEqual('[ 0, 1, 0.5 ]', str(self.__tree.post_order()))

    def test_insert_LR_into_complete_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.assertEqual([0,0.5,1], self.__tree.to_list())

    def test_get_height_after_insert_LR_into_two_complete(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.assertEqual(2,self.__tree.get_height())

    # Test insert right then right into a perfect tree of height 2

    def test_insert_RR_into_perfect_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 0, 0.5, 1, 4 ]', str(self.__tree.in_order()))

    def test_insert_RR_into_perfect_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 0.5, 0, 1, 4 ]', str(self.__tree.pre_order()))

    def test_insert_RR_into_perfect_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 0, 4, 1, 0.5 ]', str(self.__tree.post_order()))

    def test_insert_RR_into_perfect_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.__tree.insert_element(4)
        self.assertEqual([0,0.5,1,4], self.__tree.to_list())

    def test_get_height_after_insert_RR_into_two_perfect(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(0.5)
        self.__tree.insert_element(4)
        self.assertEqual(3,self.__tree.get_height())

    # Test insert a right then left into a perfect tree of height 2

    def test_insert_RL_into_perfect_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.assertEqual('[ 1, 2, 2.5, 3 ]', str(self.__tree.in_order()))

    def test_insert_RL_into_perfect_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.assertEqual('[ 2, 1, 3, 2.5 ]', str(self.__tree.pre_order()))

    def test_insert_RL_into_perfect_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.assertEqual('[ 1, 2.5, 3, 2 ]', str(self.__tree.post_order()))

    def test_insert_RL_into_perfect_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.assertEqual([1,2,2.5,3], self.__tree.to_list())

    def test_get_height_after_insert_RL_into_two_perfect(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.assertEqual(3,self.__tree.get_height())

    # Test insert Left then Left into a perfect tree of height 2

    def test_insert_LL_into_perfect_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(-1)
        self.assertEqual('[ -1, 1, 2, 3 ]', str(self.__tree.in_order()))

    def test_insert_LL_into_perfect_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(-1)
        self.assertEqual('[ 2, 1, -1, 3 ]', str(self.__tree.pre_order()))

    def test_insert_LL_into_perfect_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(-1)
        self.assertEqual('[ -1, 1, 3, 2 ]', str(self.__tree.post_order()))

    def test_insert_LL_into_perfect_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(-1)
        self.assertEqual([-1,1,2,3], self.__tree.to_list())

    def test_get_height_after_insert_LL_into_two_perfect(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(-1)
        self.assertEqual(3,self.__tree.get_height())

    # Test insert Left then Right into a perfect tree of height 2

    def test_insert_LR_into_perfect_two_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(-0.5)
        self.assertEqual('[ -1, -0.5, 0, 1 ]', str(self.__tree.in_order()))

    def test_insert_LR_into_perfect_two_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(-0.5)
        self.assertEqual('[ 0, -1, -0.5, 1 ]', str(self.__tree.pre_order()))

    def test_insert_LR_into_perfect_two_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(-0.5)
        self.assertEqual('[ -0.5, -1, 1, 0 ]', str(self.__tree.post_order()))

    def test_insert_LR_into_perfect_two_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(-0.5)
        self.assertEqual([-1,-0.5,0,1], self.__tree.to_list())

    def test_get_height_after_insert_LR_into_two_perfect(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(-0.5)
        self.assertEqual(3,self.__tree.get_height())

    # Test Insert Into a Tree of Height 3

    # Test Insert a repetitive element into a Tree of Height 3
    def test_insert_repetitive_into_perfect_three_with_in_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(25)
        self.assertEqual('[ 10, 15, 20, 25 ]', str(self.__tree.in_order()))

    def test_insert_repetitive_into_perfect_three_with_pre_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(25)
        self.assertEqual('[ 20, 10, 15, 25 ]', str(self.__tree.pre_order()))

    def test_insert_repetitive_into_perfect_three_with_post_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(25)
        self.assertEqual('[ 15, 10, 25, 20 ]', str(self.__tree.post_order()))

    def test_insert_repetitive_into_perfect_three_with_to_list(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(25)
        self.assertEqual([10,15,20,25], self.__tree.to_list())

    def test_insert_repetitive_into_perfect_three_get_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(25)
        self.assertEqual(3, self.__tree.get_height())


    # Test insert Left right right into a tree of height 3
    # rotation once

    def test_insert_LRR_into_three_with_in_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(17)
        self.assertEqual('[ 9, 10, 15, 17, 20, 25 ]', str(self.__tree.in_order()))

    def test_insert_LRR_into_three_with_pre_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(17)
        self.assertEqual('[ 15, 10, 9, 20, 17, 25 ]', str(self.__tree.pre_order()))

    def test_insert_LRR_into_three_with_post_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(17)
        self.assertEqual('[ 9, 10, 17, 25, 20, 15 ]', str(self.__tree.post_order()))

    def test_insert_LRR_into_three_with_to_list(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(17)
        self.assertEqual([9,10,15,17,20,25], self.__tree.to_list())

    def test_insert_LRR_into_three_with_get_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(17)
        self.assertEqual(3, self.__tree.get_height())

    # Test insert Left right Left into a tree of height 3
    # double rotation

    def test_insert_LRL_into_three_with_in_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(13)
        self.assertEqual('[ 9, 10, 13, 15, 20, 25 ]', str(self.__tree.in_order()))

    def test_insert_LRL_into_three_with_pre_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(13)
        self.assertEqual('[ 15, 10, 9, 13, 20, 25 ]', str(self.__tree.pre_order()))

    def test_insert_LRL_into_three_with_post_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(13)
        self.assertEqual('[ 9, 13, 10, 25, 20, 15 ]', str(self.__tree.post_order()))

    def test_insert_LRL_into_three_with_to_list(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(13)
        self.assertEqual([9,10,13,15,20,25], self.__tree.to_list())

    def test_insert_LRL_into_three_with_get_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(9)
        self.__tree.insert_element(13)
        self.assertEqual(3, self.__tree.get_height())

    # Test insert right right right into a tree of height 3
    # rotation once

    def test_insert_RRR_into_three_with_in_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(31)
        self.assertEqual('[ 10, 20, 25, 26, 30, 31 ]', str(self.__tree.in_order()))

    def test_insert_RRR_into_three_with_pre_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(31)
        self.assertEqual('[ 26, 20, 10, 25, 30, 31 ]', str(self.__tree.pre_order()))

    def test_insert_RRR_into_three_with_post_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(31)
        self.assertEqual('[ 10, 25, 20, 31, 30, 26 ]', str(self.__tree.post_order()))

    def test_insert_RRR_into_three_with_to_list(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(31)
        self.assertEqual([10,20,25,26,30,31], self.__tree.to_list())

    def test_insert_RRR_into_three_with_get_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(31)
        self.assertEqual(3, self.__tree.get_height())

    # Test insert right right Left into a tree of height 3
    # double rotation

    def test_insert_RRL_into_three_with_in_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 20, 25, 26, 27, 30 ]', str(self.__tree.in_order()))

    def test_insert_RRL_into_three_with_pre_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(27)
        self.assertEqual('[ 26, 20, 10, 25, 30, 27 ]', str(self.__tree.pre_order()))

    def test_insert_RRL_into_three_with_post_order(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 25, 20, 27, 30, 26 ]', str(self.__tree.post_order()))

    def test_insert_RRL_into_three_with_to_list(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(27)
        self.assertEqual([10,20,25,26,27,30], self.__tree.to_list())

    def test_insert_RRL_into_three_with_get_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.__tree.insert_element(26)
        self.__tree.insert_element(31)
        self.assertEqual(3, self.__tree.get_height())


    # Test insert left left left into a perfect tree of height 3
    def test_insert_LLL_into_perfect_three_with_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 2, 5, 7, 10, 15, 20, 25 ]', str(self.__tree.in_order()))

    def test_insert_LLL_into_perfect_three_with_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(1)
        self.assertEqual('[ 10, 5, 2, 1, 7, 20, 15, 25 ]', str(self.__tree.pre_order()))

    def test_insert_LLL_into_perfect_three_with_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 2, 7, 5, 15, 25, 20, 10 ]', str(self.__tree.post_order()))

    def test_insert_LLL_into_perfect_three_with_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(1)
        self.assertEqual([1,2,5,7,10,15,20,25], self.__tree.to_list())

    def test_insert_LLL_into_perfect_three_with_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(1)
        self.assertEqual(4, self.__tree.get_height())


    # Test insert Left Right Left into a perfect tree of height 3

    def test_insert_LRL_into_perfect_three_with_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(6)
        self.assertEqual('[ 2, 5, 6, 7, 10, 15, 20, 25 ]', str(self.__tree.in_order()))

    def test_insert_LRL_into_perfect_three_with_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(6)
        self.assertEqual('[ 10, 5, 2, 7, 6, 20, 15, 25 ]', str(self.__tree.pre_order()))

    def test_insert_LRL_into_perfect_three_with_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(6)
        self.assertEqual('[ 2, 6, 7, 5, 15, 25, 20, 10 ]', str(self.__tree.post_order()))

    def test_insert_LRL_into_perfect_three_with_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(6)
        self.assertEqual([2,5,6,7,10,15,20,25], self.__tree.to_list())

    def test_insert_LRL_into_perfect_three_with_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(6)
        self.assertEqual(4, self.__tree.get_height())

    
    # Test insert Right left Right into a perfect tree of height 3

    def test_insert_RLR_into_perfect_three_with_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.assertEqual('[ 2, 5, 7, 10, 15, 16, 20, 25 ]', str(self.__tree.in_order()))

    def test_insert_RLR_into_perfect_three_with_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.assertEqual('[ 10, 5, 2, 7, 20, 15, 16, 25 ]', str(self.__tree.pre_order()))

    def test_insert_RLR_into_perfect_three_with_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.assertEqual('[ 2, 7, 5, 16, 15, 25, 20, 10 ]', str(self.__tree.post_order()))

    def test_insert_RLR_into_perfect_three_with_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.assertEqual([2,5,7,10,15,16,20,25], self.__tree.to_list())

    def test_insert_RLR_into_perfect_three_with_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.assertEqual(4, self.__tree.get_height())


    # Test insert Right Right Right into a perfect tree of height 3

    def test_insert_RRR_into_perfect_three_with_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual('[ 2, 5, 7, 10, 15, 20, 25, 30 ]', str(self.__tree.in_order()))

    def test_insert_RRR_into_perfect_three_with_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual('[ 10, 5, 2, 7, 20, 15, 25, 30 ]', str(self.__tree.pre_order()))

    def test_insert_RRR_into_perfect_three_with_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual('[ 2, 7, 5, 15, 30, 25, 20, 10 ]', str(self.__tree.post_order()))

    def test_insert_RRR_into_perfect_three_with_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual([2,5,7,10,15,20,25,30], self.__tree.to_list())

    def test_insert_RRR_into_perfect_three_with_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(30)
        self.assertEqual(4, self.__tree.get_height())

    # Test insert into to form a perfect tree of height 4

    def test_insert_to_form_perfect_height_four_with_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]', str(self.__tree.in_order()))

    def test_insert_to_form_perfect_height_four_with_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.assertEqual('[ 8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15 ]', str(self.__tree.pre_order()))

    def test_insert_to_form_perfect_height_four_with_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8 ]', str(self.__tree.post_order()))

    def test_insert_to_form_perfect_height_four_with_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.assertEqual([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], self.__tree.to_list())

    def test_insert_to_form_perfect_height_perfect_four_get_heignt(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.assertEqual(4, self.__tree.get_height())


    # Test removal function

    # Test remove from an empty string

    def test_remove_empty_str(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ ]', str(self.__tree))

    def test_remove_empty_in_order(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ ]', str(self.__tree.in_order()))

    def test_remove_empty_pre_order(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ ]', str(self.__tree.pre_order()))

    def test_remove_empty_post_order(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ ]', str(self.__tree.post_order()))

    def test_remove_empty_to_list(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual([], self.__tree.to_list())

    def test_remove_empty_get_height(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual(0,self.__tree.get_height())


    # Test remove from a tree of height 1

    # Test remove an element not in the tree

    def test_remove_nonexistence_from_one_in_order(self):
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ 2 ]', str(self.__tree.in_order()))

    def test_remove_nonexistence_from_one_pre_order(self):
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ 2 ]', str(self.__tree.pre_order()))

    def test_remove_nonexistence_from_one_post_order(self):
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ 2 ]', str(self.__tree.post_order()))

    def test_remove_nonexistence_from_one_to_list(self):
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual([ 2 ], self.__tree.to_list())

    def test_remove_nonexistence_from_one_get_height(self):
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual(1,self.__tree.get_height())

    # Test remove an element in the tree

    def test_remove_element_from_one_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual('[ ]', str(self.__tree.in_order()))

    def test_remove_element_from_one_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual('[ ]', str(self.__tree.pre_order()))

    def test_remove_element_from_one_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual('[ ]', str(self.__tree.post_order()))

    def test_remove_element_from_one_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual([ ], self.__tree.to_list())

    def test_remove_element_from_one_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual(0,self.__tree.get_height())

    
    # Test of removing an element from height 2

    # Test of removing an non-existence element

    def test_remove_non_existence_from_two_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(4)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__tree.in_order()))

    def test_remove_non_existence_from_two_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(4)
        self.assertEqual('[ 2, 1, 3 ]', str(self.__tree.pre_order()))

    def test_remove_non_existence_from_two_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(4)
        self.assertEqual('[ 1, 3, 2 ]', str(self.__tree.post_order()))

    def test_remove_non_existence_from_two_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(4)
        self.assertEqual([1,2,3], self.__tree.to_list())

    def test_remove_non_existence_from_two_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(4)
        self.assertEqual(2,self.__tree.get_height())


    # Test remove leaf from height 2

    def test_remove_leaf_from_two_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1 ]', str(self.__tree.in_order()))

    def test_remove_leaf_from_two_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1 ]', str(self.__tree.pre_order()))

    def test_remove_leaf_from_two_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1 ]', str(self.__tree.post_order()))

    def test_remove_leaf_from_two_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.remove_element(2)
        self.assertEqual([1], self.__tree.to_list())

    def test_remove_leaf_from_two_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.remove_element(2)
        self.assertEqual(1,self.__tree.get_height())


    # Test remove root from height 2

    def test_remove_root_from_two_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1, 3 ]', str(self.__tree.in_order()))

    def test_remove_root_from_two_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 3, 1 ]', str(self.__tree.pre_order()))

    def test_remove_root_from_two_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1, 3 ]', str(self.__tree.post_order()))

    def test_remove_root_from_two_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual([1,3], self.__tree.to_list())

    def test_remove_root_from_two_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual(2,self.__tree.get_height())

    
    # Test remove root from height 2 incomplete

    def test_remove_root_from_two_complete_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.__tree.remove_element(3)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0 ]', str(self.__tree.in_order()))

    def test_remove_root_from_two_complete_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.__tree.remove_element(3)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0 ]', str(self.__tree.pre_order()))

    def test_remove_root_from_two_complete_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.__tree.remove_element(3)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0 ]', str(self.__tree.post_order()))

    def test_remove_root_from_two_complete_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.__tree.remove_element(3)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual([0], self.__tree.to_list())

    def test_remove_root_from_two_complete_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.__tree.remove_element(3)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual(1,self.__tree.get_height())

    # Test remove an element from height 3

    # Test of removing an non-existence element

    def test_remove_non_existence_from_three_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ 2, 3, 4, 5, 6 ]', str(self.__tree.in_order()))

    def test_remove_non_existence_from_three_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ 3, 2, 5, 4, 6 ]', str(self.__tree.pre_order()))

    def test_remove_non_existence_from_three_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual('[ 2, 4, 6, 5, 3 ]', str(self.__tree.post_order()))

    def test_remove_non_existence_from_three_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual([2,3,4,5,6], self.__tree.to_list())

    def test_remove_non_existence_from_three_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(1)
        self.assertEqual(3,self.__tree.get_height())

    # Test remove an leaf element(element with no children)
    # Double rotation

    def test_remove_leaf_from_three_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 3, 4 ]', str(self.__tree.in_order()))

    def test_remove_leaf_from_three_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual('[ 3, 2, 4 ]', str(self.__tree.pre_order()))

    def test_remove_leaf_from_three_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 4, 3 ]', str(self.__tree.post_order()))

    def test_remove_leaf_from_three_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual([2,3,4], self.__tree.to_list())

    def test_remove_leaf_from_three_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(-1)
        self.__tree.remove_element(1)
        self.__tree.remove_element(1.5)
        self.__tree.remove_element(-1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(7)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual(2, self.__tree.get_height())

# Single Rotation

    def test_remove_L_leaf_from_three_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 4, 5 ]', str(self.__tree.in_order()))

    def test_remove_L_leaf_from_three_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.remove_element(1)
        self.assertEqual('[ 4, 2, 5 ]', str(self.__tree.pre_order()))

    def test_remove_L_leaf_from_three_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 5, 4 ]', str(self.__tree.post_order()))

    def test_remove_L_leaf_from_three_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.remove_element(1)
        self.assertEqual([2,4,5], self.__tree.to_list())

    def test_remove_L_leaf_from_three_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(-1)
        self.__tree.remove_element(1)
        self.__tree.remove_element(1.5)
        self.__tree.remove_element(-1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(7)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.remove_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual(2, self.__tree.get_height())

    # Test remove an root element (element with two children)
    # Single rotation

    def test_remove_root_from_three_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual('[ 0, 1, 1.5, 4 ]', str(self.__tree.in_order()))

    def test_remove_root_from_three_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1, 0, 4, 1.5 ]', str(self.__tree.pre_order()))

    def test_remove_root_from_three_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual('[ 0, 1.5, 4, 1 ]', str(self.__tree.post_order()))

    def test_remove_root_from_three_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual([0,1,1.5,4], self.__tree.to_list())

    def test_remove_root_from_three_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual(3, self.__tree.get_height())

    # Double Rotation

    def test_remove_root_from_three_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual('[ 0, 1, 1.5, 4 ]', str(self.__tree.in_order()))

    def test_remove_root_from_three_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1, 0, 4, 1.5 ]', str(self.__tree.pre_order()))

    def test_remove_root_from_three_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual('[ 0, 1.5, 4, 1 ]', str(self.__tree.post_order()))

    def test_remove_root_from_three_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual([0,1,1.5,4], self.__tree.to_list())

    def test_remove_root_from_three_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(2)
        self.assertEqual(3, self.__tree.get_height())

    # Test remove an inner node with 2 children

    def test_remove_inner_from_three_in_order(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0, 1.5, 2, 3, 4 ]', str(self.__tree.in_order()))

    def test_remove_inner_from_three_pre_order(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 1.5, 0, 4, 3 ]', str(self.__tree.pre_order()))

    def test_remove_inner_from_three_post_order(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0, 1.5, 3, 4, 2 ]', str(self.__tree.post_order()))

    def test_remove_inner_from_three_to_list(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual([0,1.5,2,3,4], self.__tree.to_list())

    def test_remove_inner_from_three_get_height(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual(3, self.__tree.get_height())

    # Test remove an inner node with 1 children

    def test_remove_inner_2_children_from_three_in_order(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(4)
        self.assertEqual('[ 0, 1, 1.5, 2, 3 ]', str(self.__tree.in_order()))

    def test_remove_inner_1_children_from_three_pre_order(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(4)
        self.assertEqual('[ 2, 1, 0, 1.5, 3 ]', str(self.__tree.pre_order()))

    def test_remove_inner_1_children_from_three_post_order(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(4)
        self.assertEqual('[ 0, 1.5, 1, 3, 2 ]', str(self.__tree.post_order()))

    def test_remove_inner_2_children_from_three_to_list(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(4)
        self.assertEqual([0,1,1.5,2,3], self.__tree.to_list())

    def test_remove_inner_1_children_from_three_get_height(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.remove_element(4)
        self.assertEqual(3, self.__tree.get_height())

    # Test use remove to change a perfect tree of height 3 into height 2

    def test_remove_from_perfect_three_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.remove_element(4)
        self.__tree.remove_element(5)
        self.__tree.remove_element(6)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 3, 7 ]', str(self.__tree.in_order()))

    def test_remove_from_perfect_three_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.remove_element(4)
        self.__tree.remove_element(5)
        self.__tree.remove_element(6)
        self.__tree.remove_element(1)
        self.assertEqual('[ 3, 2, 7 ]', str(self.__tree.pre_order()))

    def test_remove_from_perfect_three_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.remove_element(4)
        self.__tree.remove_element(5)
        self.__tree.remove_element(6)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2, 7, 3 ]', str(self.__tree.post_order()))

    def test_remove_from_perfect_three_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.remove_element(4)
        self.__tree.remove_element(5)
        self.__tree.remove_element(6)
        self.__tree.remove_element(1)
        self.assertEqual([2,3,7], self.__tree.to_list())

    def test_remove_from_perfect_three_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.remove_element(4)
        self.__tree.remove_element(5)
        self.__tree.remove_element(6)
        self.__tree.remove_element(1)
        self.assertEqual(2, self.__tree.get_height())

    # Test remove from height 4
    # Test remove a leaf from height 4 tree

    def test_remove_leaf_from_four_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(6)
        self.assertEqual('[ 1, 2, 2.5, 3, 4, 5 ]', str(self.__tree.in_order()))
    
    def test_remove_leaf_from_four_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(6)
        self.assertEqual('[ 3, 2, 1, 2.5, 4, 5 ]', str(self.__tree.pre_order()))

    def test_remove_leaf_from_four_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(6)
        self.assertEqual('[ 1, 2.5, 2, 5, 4, 3 ]', str(self.__tree.post_order()))

    def test_remove_leaf_from_four_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(6)
        self.assertEqual([1,2,2.5,3,4,5], self.__tree.to_list())

    def test_remove_leaf_from_four_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(6)
        self.assertEqual(3, self.__tree.get_height())

    # Remove root from height 4 tree

    def test_remove_root_from_four_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3.5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(4)
        self.assertEqual('[ 0, 1, 1.5, 2, 2.5, 3, 3.5, 5, 6 ]', str(self.__tree.in_order()))
    
    def test_remove_root_from_four_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(3.5)
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(4)
        self.assertEqual('[ 2, 1, 0, 1.5, 5, 3, 2.5, 3.5, 6 ]', str(self.__tree.pre_order()))

    def test_remove_root_from_four_post_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(3.5)
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(4)
        self.assertEqual('[ 0, 1.5, 1, 2.5, 3.5, 3, 6, 5, 2 ]', str(self.__tree.post_order()))

    def test_remove_root_from_four_to_list(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3.5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(4)
        self.assertEqual([0, 1, 1.5, 2, 2.5, 3, 3.5, 5, 6], self.__tree.to_list())

    def test_remove_root_from_four_get_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3.5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2.5)
        self.__tree.remove_element(4)
        self.assertEqual(4, self.__tree.get_height())

    # Test remove an inner node with 2 children
    # Double rotation
    def test_remove_inner_2_children_from_four_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual('[ 1, 2, 6, 7, 8, 9, 10, 11 ]', str(self.__tree.in_order()))
    
    def test_remove_inner_2_children_from_four_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 2, 1, 6, 9, 8, 10, 11 ]', str(self.__tree.pre_order()))

    def test_remove_inner_2_children_from_four_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual('[ 1, 6, 2, 8, 11, 10, 9, 7 ]', str(self.__tree.post_order()))

    def test_remove_inner_2_children_from_four_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual([1, 2, 6, 7, 8, 9, 10, 11], self.__tree.to_list())

    def test_remove_inner_2_children_from_four_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual(4, self.__tree.get_height())

    # Single rotation
    def test_remove_single_inner_2_children_from_four_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual('[ 0, 1, 2, 6, 7, 8, 9, 10, 11 ]', str(self.__tree.in_order()))
    
    def test_remove_single_inner_2_children_from_four_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 1, 0, 6, 2, 9, 8, 10, 11 ]', str(self.__tree.pre_order()))

    def test_remove_single_inner_2_children_from_four_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual('[ 0, 2, 6, 1, 8, 11, 10, 9, 7 ]', str(self.__tree.post_order()))

    def test_remove_single_inner_2_children_from_four_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual([0, 1, 2, 6, 7, 8, 9, 10, 11], self.__tree.to_list())

    def test_remove_single_inner_2_children_from_four_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(5)
        self.assertEqual(4, self.__tree.get_height())


    # Test remove an inner node with 1 children
    # Double rotation
    def test_remove_double_inner_1_child_from_four_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(5.5)
        self.__tree.insert_element(6.5)
        self.__tree.remove_element(10)
        self.assertEqual('[ 1, 5, 5.5, 6, 6.5, 7, 8 ]', str(self.__tree.in_order()))
    
    def test_remove_double_inner_1_child_from_four_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(5.5)
        self.__tree.insert_element(6.5)
        self.__tree.remove_element(10)
        self.assertEqual('[ 6, 5, 1, 5.5, 7, 6.5, 8 ]', str(self.__tree.pre_order()))

    def test_remove_double_inner_1_child_from_four_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(5.5)
        self.__tree.insert_element(6.5)
        self.__tree.remove_element(10)
        self.assertEqual('[ 1, 5.5, 5, 6.5, 8, 7, 6 ]', str(self.__tree.post_order()))

    def test_remove_double_inner_1_child_from_four_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(5.5)
        self.__tree.insert_element(6.5)
        self.__tree.remove_element(10)
        self.assertEqual([1, 5, 5.5, 6, 6.5, 7, 8], self.__tree.to_list())

    def test_remove_double_inner_1_child_from_four_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(5.5)
        self.__tree.insert_element(6.5)
        self.__tree.remove_element(10)
        self.assertEqual(3, self.__tree.get_height())

    # single rotation
    def test_remove_single_inner_1_child_from_four_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(10)
        self.assertEqual('[ 0, 1, 1.5, 5, 6, 7, 8 ]', str(self.__tree.in_order()))
    
    def test_remove_single_inner_1_child_from_four_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 1, 0, 1.5, 7, 6, 8 ]', str(self.__tree.pre_order()))

    def test_remove_single_inner_1_child_from_four_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(10)
        self.assertEqual('[ 0, 1.5, 1, 6, 8, 7, 5 ]', str(self.__tree.post_order()))

    def test_remove_single_inner_1_child_from_four_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(10)
        self.assertEqual([0, 1, 1.5, 5, 6, 7, 8], self.__tree.to_list())

    def test_remove_single_inner_1_child_from_four_get_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.remove_element(9)
        self.__tree.insert_element(0)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(10)
        self.assertEqual(3, self.__tree.get_height())

    # Test remove elements from 4 to perfect 3
    def test_remove_from_four_in_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.__tree.remove_element(8)
        self.__tree.remove_element(9)
        self.__tree.remove_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(11)
        self.__tree.remove_element(12)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 3, 4, 5, 6, 7, 13, 14 ]', str(self.__tree.in_order()))
    
    def test_remove_from_four_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.__tree.remove_element(8)
        self.__tree.remove_element(9)
        self.__tree.remove_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(11)
        self.__tree.remove_element(12)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 6, 4, 3, 5, 13, 7, 14 ]', str(self.__tree.pre_order()))

    def test_remove_from_four_post_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.__tree.remove_element(8)
        self.__tree.remove_element(9)
        self.__tree.remove_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(11)
        self.__tree.remove_element(12)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 3, 5, 4, 7, 14, 13, 6 ]', str(self.__tree.post_order()))

    def test_remove_from_four_to_list(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10)
        self.__tree.insert_element(11)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(15)
        self.__tree.remove_element(8)
        self.__tree.remove_element(9)
        self.__tree.remove_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(11)
        self.__tree.remove_element(12)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.assertEqual([3, 4, 5, 6, 7, 13, 14], self.__tree.to_list())

    def test_remove_from_four_get_height(self):
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(-1)
        self.__tree.insert_element(5.5)
        self.__tree.insert_element(2.5)
        self.__tree.insert_element(8)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.__tree.remove_element(4)
        self.__tree.remove_element(8)
        self.assertEqual(3, self.__tree.get_height())

if __name__ == '__main__':
  unittest.main()