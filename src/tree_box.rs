#[derive(PartialEq, Eq, Clone, Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Box<TreeNode>>,
    pub right: Option<Box<TreeNode>>,
}

impl TreeNode {
    pub fn new(val: i32, left: Option<Box<TreeNode>>, right: Option<Box<TreeNode>>) -> Self {
        Self { val, left, right }
    }

    #[inline]
    fn edges(&self) -> [&Option<Box<TreeNode>>; 2] {
        [&self.left, &self.right]
    }
}

//#[tracing::instrument]
pub fn print_tree(head: &Option<Box<TreeNode>>) {
    //let span = span!(Level::TRACE, "outer print_tree");
    //let _enter = span.enter();
    //println!("begin print_tree");
    let mut lifo_stack: Vec<&Option<Box<TreeNode>>> = Vec::new();
    //event!(Level::DEBUG, "before push stack {}", stack.len());
    lifo_stack.push(head);
    //event!(Level::DEBUG, "after push stack {}", stack.len());
    while let Some(mb_current) = lifo_stack.pop() {
        //event!(Level::DEBUG, "after pop stack {}", stack.len());
        if let Some(current) = mb_current {
            let edges = current.edges();
            let right = edges[1];
            if right.is_some() {
                lifo_stack.push(right);
            }
            let left = edges[0];
            if left.is_some() {
                lifo_stack.push(left);
            }
            println!("val:{} l:{} r:{}", current.val, left.is_some(), right.is_some());
            //event!( Level::DEBUG, "trace left:{:?} current:{}  r:{:?}", left.is_some(), current.val, right.is_some());
        }
    }
    //event!(Level::DEBUG, "done {}", stack.len());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_tree() {
        let t1 = Some(Box::new(TreeNode {
            val: 1,
            left: None,
            right: None,
        }));
        print_tree(&t1);
    }
}
