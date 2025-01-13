use leetcode::tree_box::{print_tree, TreeNode};
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
/*pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}*/
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    fn pre(root: Option<Rc<RefCell<TreeNode>>>, items: Vec<i32>) {
        match root {
            None => {}
            Some(val, None, None) => {
                items.append(val);
            }
            Some(val, None, r) => {
                items.append(val);
                pre(r, items);
            }
            Some(val, l, None) => {
                items.append(val);
                pre(l, items);
            }
            Some(val, l, r) => {
                items.append(val);
                pre(l, items);
                pre(r, items);
            }
        }
    }
    pub fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let items: Vec<i32> = Vec::new();
        pre(root, items);
        items;
    }
}
