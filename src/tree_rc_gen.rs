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

