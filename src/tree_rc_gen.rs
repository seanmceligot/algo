use std::collections::VecDeque;
use std::fmt::Display;
use std::{cell::RefCell, rc::Rc};

//use tracing::{event, span, Level};

// Rc<RefCell<TreeNode>>
// Option<Rc<RefCell<TreeNode>>>

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct TreeNode<T: Clone + Eq + PartialEq + Display> {
    pub val: T,
    pub left: Option<Rc<RefCell<TreeNode<T>>>>,
    pub right: Option<Rc<RefCell<TreeNode<T>>>>,
}

//impl<T> TreeNode<T> {

impl<T: Clone + PartialEq + Eq + Display> TreeNode<T> {
    pub fn new(
        val: T,
        left: Option<Rc<RefCell<TreeNode<T>>>>,
        right: Option<Rc<RefCell<TreeNode<T>>>>,
    ) -> Self {
        Self { val, left, right }
    }
}

type MaybeTreeNode<T> = Option<Rc<RefCell<TreeNode<T>>>>;

//#[inline]
//fn edges(nodeCell<TreeNode>) -> [&Option<Rc<RefCell<TreeNode>>>; 2] {
//    [&node.left, &node.right]
//}
/*
build_tree_breadth_first

LeetCode uses a level-order traversal (breadth-first search) representation for trees in array format. Here's how it works:

How the Array Format Represents a Tree
Root Node:

The first element of the array is the root node.
Left and Right Children:

For a node at index i:
The left child is at index 2 * i + 1.
The right child is at index 2 * i + 2.
null for Missing Nodes:

null represents a missing node (e.g., no child at that position).
Traversal Order:

The array is filled level by level, from left to right.
*/
pub fn build_tree_breadth_first<T: Clone + Eq + Display + PartialEq>(
    input_list: &[Option<T>],
) -> MaybeTreeNode<T> {
    if let Some(first) = input_list.get(0) {
        if let Some(val) = first {
            //        CREATE queue (empty)
            let mut queue: VecDeque<MaybeTreeNode<T>> = VecDeque::new();
            //        SET root = nodes_list[0]
            let root = Rc::new(RefCell::new(TreeNode::new(val.clone(), None, None)));
            //        ADD root TO queue
            queue.push_back(Some(Rc::clone(&root)));
            //
            //        SET i = 1  # Pointer to track position in nodes_list
            let mut i = 1;
            let len = input_list.len();

            //  WHILE queue IS NOT EMPTY AND i < LENGTH(nodes_list):
            while !queue.is_empty() && (i < len) {
                //      current_node = REMOVE first element FROM queue
                let mb_current_node = queue.pop_front().unwrap();
                //      IF current_node IS NOT null:
                if let Some(current_node) = mb_current_node {
                    // left
                    if i < len {
                        if let Some(val) = &input_list[i] {
                            // SET current_node.left = nodes_list[i]
                            let left =
                                Rc::new(RefCell::new(TreeNode::new(val.clone(), None, None)));
                            current_node.borrow_mut().left = Some(Rc::clone(&left));
                            //  ADD nodes_list[i] TO queue
                            queue.push_front(Some(left));
                        }
                        // INCREMENT i
                        i += 1;
                    }
                    // right
                    if i < len {
                        if let Some(val) = &input_list[i] {
                            // SET current_node.right = nodes_list[i]
                            let right =
                                Rc::new(RefCell::new(TreeNode::new(val.clone(), None, None)));
                            current_node.borrow_mut().right = Some(Rc::clone(&right));
                            //  ADD nodes_list[i] TO queue
                            queue.push_front(Some(right));
                        }
                        // INCREMENT i
                        i += 1;
                    }
                }
            }
            Some(root)
        } else {
            // first is None
            None
        }
    } else {
        // input_list is empty
        None
    }
}
//        RETURN root

//#[tracing::instrument]
pub fn print_tree<T: Clone + Eq + Display>(head: &MaybeTreeNode<T>) {
    //let span = span!(Level::TRACE, "outer print_tree");
    //let _enter = span.enter()
    //println!("begin print_tree");
    let mut lifo_stack: Vec<MaybeTreeNode<T>> = Vec::new();

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
                    "val:{} l:{} r:{}",
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_tree_breadth_first() {
        let input_list = vec![Some(1), Some(2), Some(3), None, Some(4), None, Some(5)];
        let root = build_tree_breadth_first(&input_list);
        print_tree(&root);
    }
    #[test]
    fn test_build_tree() {
        let t1 = Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: None,
            right: None,
        })));
        print_tree(&t1);
    }
}
