// leetcode Remove Duplicates from Sorted Tree

use leekcode::tree_box::{print_tree, TreeNode};
use tracing_subscriber::fmt::format::FmtSpan;

// cargo run --bin remove_from_sorted
pub struct Solution {}
impl Solution {
    pub fn dfs(head: Option<Box<TreeNode>>) -> Option<Box<TreeNode>> {
        print_tree(&head);
        head
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
    let t3 = Some(Box::new(TreeNode::new(3, None, None)));
    let t2 = Some(Box::new(TreeNode::new(2, t3, None)));
    let t4 = Some(Box::new(TreeNode::new(4, None, None)));
    let t1 = Some(Box::new(TreeNode::new(1, t2, t4)));
    Solution::dfs(t1);
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_all_duplicates2() {}
}
