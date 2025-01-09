// leetcode Remove Duplicates from Sorted Tree

use std::{cell::RefCell, clone, collections::VecDeque, rc::Rc};

use leekcode::tree_rc::{build_tree_breadth_first, MaybeTreeNode, TreeNode};

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
    let t5: MaybeTreeNode = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4: MaybeTreeNode = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t3: MaybeTreeNode = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t5))));
    let t2: MaybeTreeNode = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t4))));
    let root: MaybeTreeNode = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));

    let root2 = build_tree_breadth_first(&[Some(1), Some(2), Some(4), Some(3)]);

    // compare the two trees to see if they are the same
    assert!(compare_trees(&root, &root2));

    Solution::dfs(root);
}
fn compare_trees(t1: &MaybeTreeNode, t2: &MaybeTreeNode) -> bool {
    // compare the two trees to see if they are the same
    //println!("t1:{:?} t2:{:?}", t1, t2);
    if t1.is_none() && t2.is_none() {
        println!("both are None");
        return false;
    }
    if t1.is_none() || t2.is_none() {
        println!("one is None");
        return false;
    }
    let t1 = t1.as_ref().unwrap();
    let t2 = t2.as_ref().unwrap();
    let t1 = t1.borrow();
    let t2 = t2.borrow();
    println!("t1:{} t2:{}", t1.val, t2.val);
    if t1.val != t2.val {
        println!("values are different");
        return false;
    }
    return compare_trees(&t1.left, &t2.left) & compare_trees(&t1.right, &t2.right);
}
#[cfg(test)]
mod tests {

    #[test]
    fn test_all_duplicates2() {}
}
