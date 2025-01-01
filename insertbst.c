#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

struct TreeNode *insertIntoBST(struct TreeNode *root, int val) {

  // Allocate memory for new node and initialize its value
  struct TreeNode *newnode = calloc(1, sizeof(struct TreeNode));
  newnode->val = val;

  // If the tree is empty, return the new node as the root
  if (root == NULL) {
    return newnode;
  }

  // Start at the root of the tree
  struct TreeNode *cur = root;

  // Traverse the tree to find the correct position for the new node
  while (cur) {

    // If the current node's value is equal to the new node's value, return the
    // original root (no duplicates allowed)
    if (cur->val == newnode->val) {
      // already found, not duplicates
      return root;
    }

    // If the new node's value is less than the current node's value, move to
    // the left subtree
    if (newnode->val < cur->val) {
      if (cur->left == NULL) {
        cur->left = newnode; // insert to the left
        return root;
      } else {
        cur = cur->left; // continue to the left
      }
    }

    // If the new node's value is greater than the current node's value, move to
    // the right subtree
    else if (newnode->val > cur->val) {
      if (cur->right == NULL) {
        cur->right = newnode;
        return root;
      } else {
        cur = cur->right;
      }
    }
  }

  // If the while loop completes without finding a suitable position, return the
  // original root
  return root;
}
