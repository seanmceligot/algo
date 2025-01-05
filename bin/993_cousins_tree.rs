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

//  Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
impl Solution {
    pub fn is_cousins(mb_root: Option<Rc<RefCell<TreeNode>>>, x: i32, y: i32) -> bool {
        //  (starting point) Given the root of
        //  PREREQ: a binary tree
        //  PREREQ: with unique values
        //  INPUT: and the values of two different nodes of the tree x and y,
        //  RETURN: return true if the nodes corresponding to the values x and y in the tree are cousins,
        //          false otherwise.
        //          false if children.
        //          false they are found not to be cousins.
        //          false if tree ends before found.
        if mb_root.is_none() {
            println!("mb_root is none");
            // false if tree ends before found.
            // no cousins are possible with no children
            return false;
        }
        let root = mb_root.unwrap();
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
        let mut q = VecDeque::new();
        q.push_back((Some(Rc::clone(&root)), None));
        let mut depth = 0;
        let mut ydepth = None;
        let mut xdepth = None;
        let mut xparent = None;
        let mut yparent = None;

        while q.len() > 0 {
            let size = q.len();
            println!("depth={} size={} ", depth, size);
            for _ in 0..size {
                let (node, parent) = q.pop_front().unwrap();
                if let Some(n) = node {
                    if n.borrow().val == x {
                        xdepth = Some(depth);
                        let f = Rc::clone(&n);
                        xparent = Some(f);
                    }
                    if n.borrow().val == y {
                        ydepth = Some(depth);
                        yparent = parent;
                    }
                    if let Some(left) = &n.borrow().left {
                        q.push_back((Some(Rc::clone(left)), Some(Rc::clone(&n))));
                    }
                    if let Some(right) = &n.borrow().right {
                        q.push_back((Some(Rc::clone(right)), Some(Rc::clone(&n))));
                    }
                }
                if xdepth.is_some() && ydepth.is_some() {
                    if xdepth == ydepth && xparent != yparent {
                        println!("xdepth={} ydepth={} xparent={} yparent={}", xdepth.unwrap(), ydepth.unwrap(), xparent.unwrap().borrow().val, yparent.unwrap().borrow().val);
                        return true;
                    }
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
    assert_eq!(result, true);
}
#[cfg(test)]
mod tests {
    //use super::*;

    #[test]
    fn test_all_duplicates2() {}
}
