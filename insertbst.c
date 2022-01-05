#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    struct TreeNode* newnode = calloc(1,sizeof( struct TreeNode));
    newnode-> val = val;
    if (root == NULL) {
        return newnode;
    }
    struct TreeNode* cur = root;
    while(cur) {
        if (cur->val == newnode->val) {
            // already found, not duplicates
            return root;
        }
        if (newnode->val < cur->val) {
            if (cur->left == NULL) {
                cur->left = newnode;  // insert to the left
                return root;
            } else {
                cur = cur->left; // continue to the left
            }
        } else if (newnode->val > cur->val) {
            if (cur->right == NULL) {
                cur->right = newnode;
                return root;
	    } else {
                cur = cur->right;
            }
	}
    }
    return root;
}
