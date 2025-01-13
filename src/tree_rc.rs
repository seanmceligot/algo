use std::collections::VecDeque;
use std::{cell::RefCell, rc::Rc};

//use tracing::{event, span, Level};

// Rc<RefCell<TreeNode>>
// Option<Rc<RefCell<TreeNode>>>

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    pub fn new(
        val: i32,
        left: Option<Rc<RefCell<TreeNode>>>,
        right: Option<Rc<RefCell<TreeNode>>>,
    ) -> Self {
        Self { val, left, right }
    }
}

pub type MaybeTreeNode = Option<Rc<RefCell<TreeNode>>>;

/// From leetcode
///
/// Build a tree leetcode style from an array such as:
/// Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
/// In rust this would be
/// Input: root = [Some(1), Some(2), Some(3), Some(4), Some(5), None, Some(8), None, None, Some(6), Some(7), Some(9)]
/// Output: MaybeTreeNode
/// 
/// The tree would look like:
///        1
///       / \
///      2   3
///     / \   \ 
///    4   5   8
///       / \ /
///      6  7 9
///     
pub fn from_leetcode(input_list: &[Option<i32>]) -> MaybeTreeNode {
    let mut queue: VecDeque<MaybeTreeNode> = VecDeque::new();
    let mut iter = input_list.iter();
    let next = iter.next();
    if next.is_none() {
        // empty list
        None
    } else {
        let next_val = next.unwrap();
        if next_val.is_none() {
            // you can't have an empty root node
            None
        } else {
            let root = 
            Some(
                Rc::new(
                    RefCell::new(
                        TreeNode::new( next_val.unwrap(), None, None)
            )));
            // we have our root node
            queue.push_back(root.clone());

            // begin building the tree
            // iter is an iterator over the input list
            // queue is a queue of nodes
            while !queue.is_empty() {
                let current = queue.pop_front().unwrap();
                // take the next input and assign it to left node or None
                if let Some(Some(val)) = iter.next() {
                    let left = 
                        Some(
                            Rc::new(
                                RefCell::new(
                                    TreeNode::new(*val, None, None))));
                    current.as_ref().unwrap().borrow_mut().left = left.clone();
                    // we add the left node to the queue before right node so
                    // we can build the tree in a breadth first manner 
                    queue.push_back(left);
                }
                if let Some(Some(val)) = iter.next() {
                    let right =
                     Some(Rc::new(RefCell::new(TreeNode::new(*val, None, None))));
                    current.as_ref().unwrap().borrow_mut().right = right.clone();
                    queue.push_back(right);
                }
            }
            root
        }
    }
} 
/// To leetcode
/// 
/// Convert a tree to a leetcode style array
/// 
/// Input: MaybeTreeNode
/// Output: Vec<Option<i32>>
/// 
pub fn to_leetcode(head: &MaybeTreeNode) -> Vec<Option<i32>> {
    let mut result: Vec<Option<i32>> = Vec::new();
    let mut queue: VecDeque<MaybeTreeNode> = VecDeque::new();
    // add the root node to the queue
    queue.push_back(head.clone());
    while !queue.is_empty() {
        let current = queue.pop_front().unwrap();
        if current.is_some() {
            let rc_current = current.as_ref().unwrap();
            let ref_current = rc_current;
            let current = ref_current;
            let cb = current.borrow();
            result.push(Some(cb.val));
            queue.push_back(cb.left.clone());
            queue.push_back(cb.right.clone());
        } else {
            result.push(None);
        }
    }
    // remove trailing None values
    while let Some(None) = result.last() {
        result.pop();
    }
    result
}

// test to_leekcode and from_leekcode
#[cfg(test)]
mod test_leetcode {
    use super::*;
    #[test]
    fn test_leetcode() {
        let input_list = vec![Some(1), Some(2), Some(3), Some(4), Some(5), None, Some(8), None, None, Some(6), Some(7), Some(9)];
        let root = from_leetcode(&input_list);
        let output_list = to_leetcode(&root);
        assert_eq!(input_list, output_list);
    }
}


pub fn print_tree_tail_recursive(head: &Option<Rc<RefCell<TreeNode>>>) {
    //println!("begin print_tree");
    if head.is_some() {
        let rc_current = head.as_ref().unwrap();
        let ref_current = rc_current;
        let current = ref_current;
        let cb = current.borrow();
        println!(
            "    {}
  /   \\
{}     {}",
            cb.val,
            if let Some(left_val) = &cb.left {
                left_val.borrow().val.to_string()
            } else {
                " ".to_string()
            },
            if let Some(right_val) = &cb.right {
                right_val.borrow().val.to_string()
            } else {
                " ".to_string()
            }
        );
        print_tree_tail_recursive(&cb.left);
        print_tree_tail_recursive(&cb.right);
    } else {
        // head is None
    }
    //println!("done print_tree");
}
//#[tracing::instrument]
pub fn print_tree_stack(head: &Option<Rc<RefCell<TreeNode>>>) {
    //let span = span!(Level::TRACE, "outer print_tree");
    //let _enter = span.enter()
    //println!("begin print_tree");
    let mut lifo_stack: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();

    //event!(Level::DEBUG, "before push stack {}", stack.len());
    if head.is_some() {
        lifo_stack.push(head.clone());
        //event!(Level::DEBUG, "after push stack {}", stack.len());
        while let Some(mb_current) = lifo_stack.pop() {
            //event!(Level::DEBUG, "after pop stack {}", stack.len());
            if let Some(rc_current) = mb_current {
                let ref_current = rc_current;
                let current = ref_current;
                let cb = current.borrow();
                if cb.right.is_some() {
                    lifo_stack.push(cb.right.clone())
                }
                if cb.left.is_some() {
                    lifo_stack.push(cb.left.clone())
                }
                println!(
                    "print_tree: val:{} l:{} r:{}",
                    cb.val,
                    cb.left.is_some(),
                    cb.right.is_some()
                );
                //event!( Level::DEBUG, "trace left:{:?} current:{}  r:{:?}", left.is_some(), current.val, right.is_some());
            }
        }
    } else {
        // head is None
    }

    //event!(Level::DEBUG, "done {}", stack.len());
}
pub fn compare_trees(t1: &MaybeTreeNode, t2: &MaybeTreeNode) -> bool {
    // compare the two trees to see if they are the same
    println!("compare: t1:{:?}", t1);
    println!("         t2:{:?}", t2);
    if t1.is_none() && t2.is_none() {
        println!("both are None");
        return false;
    }
    if t1.is_none() || t2.is_none() {
        println!("one one is None");
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
    compare_trees(&t1.left, &t2.left) & compare_trees(&t1.right, &t2.right)
}

// Function for Preorder Traversal tree
// ASCII representation:
//         1
//        / \
//       2   3
//      /
//     4
//      \
//       5
pub fn create_preorder_tree() -> MaybeTreeNode {
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, t4, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, None))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    root
}

// Function for Inorder Traversal tree
// ASCII representation:
//         4
//        / \
//       1   5
//        \
//         2
//          \
//           3
pub fn create_inorder_tree() -> MaybeTreeNode {
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, None))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t3))));
    let t1 = Some(Rc::new(RefCell::new(TreeNode::new(1, None, t2))));
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(4, t1, t5))));
    root
}

// Function for Postorder Traversal tree
// ASCII representation:
//         5
//        /
//       4
//      /
//     3
//    /
//   2
//  /
// 1
pub fn create_postorder_tree() -> MaybeTreeNode {
    let t1 = Some(Rc::new(RefCell::new(TreeNode::new(1, None, None))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, t1, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, t2, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, t3, None))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(5, t4, None))));
    root
}

// Function for Level Order Traversal tree
// ASCII representation:
//         1
//        / \
//       2   3
//          / \
//         4   5
pub fn create_level_order_tree() -> MaybeTreeNode {
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, None))));
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, t4, t5))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, None))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, t2, t3))));
    root
}

// Function for Depth-First Traversal tree
// ASCII representation:
//         1
//          \
//           2
//            \
//             3
//              \
//               4
//                \
//                 5
pub fn create_depth_first_tree() -> MaybeTreeNode {
    let t5 = Some(Rc::new(RefCell::new(TreeNode::new(5, None, None))));
    let t4 = Some(Rc::new(RefCell::new(TreeNode::new(4, None, t5))));
    let t3 = Some(Rc::new(RefCell::new(TreeNode::new(3, None, t4))));
    let t2 = Some(Rc::new(RefCell::new(TreeNode::new(2, None, t3))));
    let root = Some(Rc::new(RefCell::new(TreeNode::new(1, None, t2))));
    root
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_from_leetcode() {
        let input_list = vec![Some(1), Some(2), Some(3), None, Some(4), None, Some(5)];
        let root = from_leetcode(&input_list);
        print_tree_stack(&root);
    }
    #[test]
    fn test_build_tree() {
        let t1 = Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: None,
            right: None,
        })));
        print_tree_tail_recursive(&t1);
    }
}
