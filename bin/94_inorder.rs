// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use leetcode::tree_rc::{from_leetcode, print_tree_stack, TreeNode};
use std::cell::RefCell;
//use std::collections::HashSet;
//use std::collections::VecDeque;
use std::rc::Rc;

pub struct Solution {}

//  Two nodes of a binary tree are cousins
//  if they have the same (TEST 1) depth
//  with different parents (TEST 2).
type MaybeTreeNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut stack: Vec<MaybeTreeNode> = Vec::new();
        let mut current = root.clone();
        while current.is_some() || !stack.is_empty() {
            while let Some(node) = current {
                stack.push(Some(Rc::clone(&node)));
                current = node.borrow().left.clone();
            }
            current = stack.pop().unwrap();
            if let Some(node) = current {
                result.push(node.borrow().val);
                current = node.borrow().right.clone();
            }
        }
        result
        
    }
}

fn main() {
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t4))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    print_tree_stack(&root);
    let input_list = vec![Some(1), Some(2), Some(3), Some(4), Some(5), None, Some(8), None, None, Some(6), Some(7), Some(9)];
    let root = from_leetcode(&input_list);
    print_tree_stack(&root);
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_inorder_traversal() {
        // Construct the tree:
        //       1
        //      / \
        //     2   3
        //    / \   \
        //       4   5
        //     
        let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
        let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
        let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t5))));
        let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t4))));
        let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
        assert_eq!(Solution::inorder_traversal(root), vec![2, 4, 1, 3, 5]);
    }
}
