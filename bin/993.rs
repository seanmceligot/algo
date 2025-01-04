use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

use leekcode::tree_rc::{build_tree_breadth_first, print_tree, TreeNode};
use tracing_subscriber::fmt::format::FmtSpan;

pub struct Solution {}

//  Definition for a binary tree node.
//  class TreeNode:
//      def __init__(self, val=0, left=None, right=None):
//          self.val = val
//          self.left = left
//          self.right = right

//  (starting point) Given the root of
//  PREREQ: a binary tree
//  PREREQ: with unique values
//  INPUT: and the values of two different nodes of the tree x and y,

//  RETURN: return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

//  Two nodes of a binary tree are cousins
//  if they have the same (TEST 1) depth
//  with different parents (TEST 2).

//  Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
impl Solution {
    pub fn is_cousins(root: Option<Rc<RefCell<TreeNode>>>, x: i32, y: i32) -> bool {
        if root.is_none() {
            return false;
        }
        let mut xy = HashSet::new();
        xy.insert(x);
        xy.insert(y);
        print_tree(&root);
        false
    }
}
fn main() {
    tracing_subscriber::fmt()
        .with_ansi(true)
        .with_max_level(tracing::Level::TRACE)
        //.without_time()
        .with_target(false)
        .with_span_events(FmtSpan::CLOSE)
        .with_timer(tracing_subscriber::fmt::time::uptime())
        .init();
    // Depth first means go deep before doing wide
    // Construct the tree:
    //       1
    //      / \
    //     2   4
    //    /
    //   3
    /*
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t4))));
    let t1 = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    */
    let input_list = vec![Some(1), Some(2), Some(3), None, Some(4), None, Some(5)];
    let root = build_tree_breadth_first(&input_list);
    print_tree(&root);
    //Solution::is_cousins(root, 4, 5);
}
#[cfg(test)]
mod tests {
    //use super::*;

    #[test]
    fn test_all_duplicates2() {}
}
