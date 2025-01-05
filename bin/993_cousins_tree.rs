use leekcode::tree_rc::{build_tree_breadth_first, print_tree, TreeNode};
use std::cell::RefCell;
use std::collections::HashSet;
use std::collections::VecDeque;
use std::rc::Rc;
use tracing_subscriber::fmt::format::FmtSpan;

pub struct Solution {}

//  Two nodes of a binary tree are cousins
//  if they have the same (TEST 1) depth
//  with different parents (TEST 2).
type MaybeTreeNode = Option<Rc<RefCell<TreeNode>>>;

//  Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
impl Solution {
    pub fn is_cousins(root: Option<Rc<RefCell<TreeNode>>>, x: i32, y: i32) -> bool {
        //  (starting point) Given the root of
        //  PREREQ: a binary tree
        //  PREREQ: with unique values
        //  INPUT: and the values of two different nodes of the tree x and y,
        //  RETURN: return true if the nodes corresponding to the values x and y in the tree are cousins,
        //          false otherwise.
        //          false if children.
        //          false they are found not to be cousins.
        //          false if tree ends before found.
        if root.is_none() {
            println!("mb_root is none");
            // false if tree ends before found.
            // no cousins are possible with no children
            return false;
        }
        let root = root.unwrap();
        let mut xy = HashSet::new();
        xy.insert(x);
        xy.insert(y);
        print_tree(&Some(Rc::clone(&root)));
        println!("node val={}", root.borrow().val);
        println!("left is some={}", root.borrow().left.is_some());
        println!("right is some={}", root.borrow().right.is_some());

        if let Some(left) = &root.borrow().left {
            println!("left val={}", left.borrow().val);
            // at the root level we can only have children, not cousins
            if xy.contains(&left.borrow().val) {
                println!("left val={} is in xy", left.borrow().val);
                return false;
            }
        }
        if let Some(right) = &root.borrow().right {
            println!("right val={}", right.borrow().val);
            // at the root level we can only have children, not cousins
            if xy.contains(&right.borrow().val) {
                println!("right val={} is in xy", right.borrow().val);
                return false;
            }
        }
        let mut q: VecDeque<(MaybeTreeNode, MaybeTreeNode)> = VecDeque::new();
        q.push_back((Some(Rc::clone(&root)), None));
        let mut depth = 0;
        let mut ydepth = None;
        let mut xdepth = None;
        let mut xparent: MaybeTreeNode = None;
        let mut yparent: MaybeTreeNode = None;

        while !q.is_empty() {
            let size = q.len();
            println!("depth={} size={} ", depth, size);
            for _ in 0..size {
                
                let (node, parent) = q.pop_front().unwrap();
                // if node is not None
                if let Some(n) = node {
                    if n.borrow().val == x {
                        // found x
                        xdepth = Some(depth);
                        if let Some(p) = parent {
                            // save x parent to check later if x and y are cousins
                            xparent = Some(Rc::clone(&p));
                        }
                    } else if n.borrow().val == y {
                        ydepth = Some(depth);
                        if let Some(p) = parent {
                            // save y parent to check later if x and y are cousins
                            yparent = Some(Rc::clone(&p));
                        }
                    }
                    if let Some(left) = &n.borrow().left {
                        // if current node has a left child, add it to the queue
                        let left_node = Some(Rc::clone(left));
                        let parent_node = Some(Rc::clone(&n));
                        q.push_back(
                            ( left_node, parent_node));
                    }
                    if let Some(right) = &n.borrow().right {
                        // if current node has a right child, add it to the queue
                        let right_node = Some(Rc::clone(right));
                        let parent_node = Some(Rc::clone(&n));
                        q.push_back(
                            ( right_node, parent_node));
                    }
                }
                if xdepth.is_some() && ydepth.is_some() {
                    // we found both x and y
                    let same_depth = xdepth == ydepth;
                    let diff_parent = xparent != yparent;
                    if same_depth & diff_parent {
                        // x and y are cousins (same depth, different parent)
                        println!("xdepth={} ydepth={} xparent={} yparent={}", xdepth.unwrap(), ydepth.unwrap(), xparent.unwrap().borrow().val, yparent.unwrap().borrow().val);
                        return true;
                    }
                    // x and y are not cousins
                    return false;
                }
            }
            depth += 1;
        }
        false
    }
}
fn main() {
    println!("start");
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
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t4))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    /*
    let input_list = vec![Some(1), Some(2), Some(3), None, Some(4), None, Some(5)];
    let root = build_tree_breadth_first(&input_list);
    */
    // root value should be 1
    if let Some(r) = &root {
        println!("root={}", r.borrow().val);
    }
    print_tree(&root);
    // should be true with 4, 5
    let result = Solution::is_cousins(root, 4, 5);
    println!("result={}", result);
 
    //[1,2,3,null,null,4,5]
    // with 4, 5
    //       1
    //      / \
    //     2   3
    //        / \
    //       4   5 
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, t4, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, None))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    let result = Solution::is_cousins(root, 4, 5);
    println!("result={}", result);
    //should be false becuase 4 and 5 are children, not cousins
    assert_eq!(result, false);
}
#[cfg(test)]
mod tests {
    //use super::*;

    #[test]
    fn test_all_duplicates2() {}
}
