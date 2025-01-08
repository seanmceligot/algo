// leetcode Remove Duplicates from Sorted Tree

use std::{cell::RefCell, clone, collections::VecDeque, rc::Rc};

use leekcode::tree_rc::{TreeNode};

type MaybeTreeNode = Option<Rc<RefCell<TreeNode>>>;

// cargo run --bin dfs
pub struct Solution {}
impl Solution {
  pub fn dfs(head: MaybeTreeNode) -> MaybeTreeNode {
        if !head.is_some() {
            return None;
        }
        let mut stack: VecDeque<MaybeTreeNode> = VecDeque::new();
        stack.push_back(head.clone());

        head
    }
}

fn main() {
 
    // Depth first means go deep before doing wide
    // Construct the tree:
    //       1
    //      / \
    //     2   4
    //    /
    //   3
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t4))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    Solution::dfs(root);
}
#[cfg(test)]
mod tests {
    

    #[test]
    fn test_all_duplicates2() {}
}
