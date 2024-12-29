// leetcode Remove Duplicates from Sorted List

use leekcode::linked_list::{build_list, list_to_vec, print_list, ListNode};

// cargo run --bin remove_from_sorted
pub struct Solution {}
impl Solution {
    pub fn delete_duplicates(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        print_list("before delete_duplicates", &head);
        let mut current = head.as_mut();
        while let Some(node) = current {
            // node.next.as_ref creates &Box like a pointer to the ListNode
            // repeat until node.next is none or node.val != next.next.val
            while let Some(next_node) = node.next.as_ref() {
                if next_node.val == node.val {
                    // Remove the duplicate by skipping to the next node.
                    let next_next = node.next.as_mut().unwrap().next.take();
                    node.next = next_next;
                } else {
                    break; // Exit the inner loop if values are different.
                }
            }
            current = node.next.as_mut();
        }
        print_list("after delete_duplicates", &head);
        head
    }
}

fn main() {
    let input = build_list(&[1, 2, 2, 3]);
    let output = Solution::delete_duplicates(input);
    assert_eq!(list_to_vec(output), vec![1, 2, 3]);
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_all_duplicates2() {
        let input = build_list(&[1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1]);
    }
    #[test]
    fn test_0_1_1() {
        let input = build_list(&[0, 1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![0, 1]);
    }
    #[test]
    fn test_1_1() {
        let input = build_list(&[1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1]);
    }
    #[test]
    fn test_1_1_1() {
        let input = build_list(&[1, 1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1]);
    }
    #[test]
    fn test_all_duplicates3() {
        let input = build_list(&[1, 1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1]);
    }
    #[test]
    fn test_all_duplicates4() {
        let input = build_list(&[1, 1, 1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1]);
    }
    #[test]
    fn test_all_duplicates() {
        let input = build_list(&[1, 1, 1, 1]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1]);
    }
    #[test]
    fn test_no_duplicates() {
        let input = build_list(&[1, 2, 3]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1, 2, 3]);
    }

    #[test]
    fn test_mixed_duplicates() {
        let input = build_list(&[1, 1, 2, 3, 3]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), vec![1, 2, 3]);
    }

    #[test]
    fn test_empty_list() {
        let input = build_list(&[]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(list_to_vec(output), Vec::<i32>::new());
    }
}
