// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,

}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
pub fn print_list(msg: &str, head: &Option<Box<ListNode>>) {
    //println!("begin print_list");
    let mut it = head;
    print!("{}: ", msg);
    while let Some(cur) = it {
        print!("{} ", cur.val);
        it = &cur.next;
    }
    println!();
}
// Helper function to build a linked list from a slice of i32 values
pub fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {
    let mut head: Option<Box<ListNode>> = None;
    for &val in vals.iter().rev() {
        let mut new_node = Box::new(ListNode::new(val));
        new_node.next = head;
        head = Some(new_node);
    }
    head
}

// Helper function to convert a linked list back into a vector of i32 values
pub fn list_to_vec(head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut vec = Vec::new();
    let mut cur = head.as_ref();
    while let Some(node) = cur {
        vec.push(node.val);
        cur = node.next.as_ref();
    }
    vec
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_list() {
        let ll = build_list(&[1, 1, 2, 3, 3]);
        assert_eq!(list_to_vec(ll), vec![1, 1, 2, 3, 3]);
    }
}
