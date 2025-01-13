// leetcode Remove Duplicates from Sorted Tree

use std::{array, cell::RefCell, clone, collections::VecDeque, rc::Rc};

use leetcode::tree_rc::{to_leetcode, from_leetcode, compare_trees, create_level_order_tree, print_tree_stack, print_tree_tail_recursive, MaybeTreeNode, TreeNode};

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
    //     2   3
    //    / \
    //   4   5
    //   
    let root: Option<Rc<RefCell<TreeNode>>> =  create_level_order_tree();
    let array = to_leetcode(&root);
    //print_tree_tail_recursive(&root);

    let root2 = from_leetcode(
        &[Some(1), Some(2), Some(3), Some(4), Some(5)]);
    let array2 = to_leetcode(&root2);
    println!("level  : {:?}", array);
    println!("breadth: {:?}", array2);
    //print_tree_tail_recursive(&root);

    // compare the two trees to see if they are the same
    //assert!(compare_trees(&root, &root2));

    Solution::dfs(root);
}
#[cfg(test)]
mod tests {

    #[test]
    fn test_all_duplicates2() {}
}
