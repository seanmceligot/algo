// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
struct Solution {
}
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut items: Vec<i32> = Vec::new();
        match root {
            None => {},
            Some(_) => {
                items.extend_from_slice(pre(root));
            }
        }
        items
    }
}
//fn extract_range<'a>(s: &'a str, r: Range<usize>) -> &'a str {
fn pre<'a>(root: Option<Rc<RefCell<TreeNode>>>) -> &'a [i32] {
    let mut items: Vec<i32> = Vec::new();
    match root {
        None => {},
        Some(rc) => match &*rc.borrow() {
            TreeNode {val:val, left:None, right:None} => {
                items.push(val.clone());
            },
            TreeNode {val:val, left:None, right:r} => {
                items.push(val.clone());
                let sl = pre(*r.as_ref());
                items.extend_from_slice(sl)
            },
            TreeNode {val:val, left:l, right:None} => {
                items.push(val.clone());
                items.extend_from_slice(pre(l.clone()))
            },
            TreeNode {val:val, left:l, right:r} => {
                items.push(val.clone());
                items.extend_from_slice(pre(l.clone()));
                items.extend_from_slice(pre(r.clone()));
            }
        }
    }
    items.as_slice()
}
fn main() {
    pre(None);

    
}
