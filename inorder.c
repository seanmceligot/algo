#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
  struct TreeNode *left;
  struct TreeNode *right;
  int val;
};
void printa(const char *label, int *arr, int N) {
  printf("%s[%d]: ", label, N);
  for (int i = 0; i < N; i++) {
    printf("%d, ", arr[i]);
  }
  printf("\n");
}

const unsigned int buffer_block_size = 1;
int *traverse(struct TreeNode *root, int *list, int *bsize, int *count) {
  if (root) {
    list = traverse(root->left, list, bsize, count);
    if (*count == *bsize) {
      *bsize = *bsize + buffer_block_size;
      // printf("realloc buffer %p %ld\n", list, (*bsize)*sizeof(int));
      list = (int *)realloc(list, (*bsize) * sizeof(int));
    }
    // printf("list %p\n", list);
    // printf("index %d\n", *count);
    // printf("val %d\n", root->val);
    list[*count] = root->val; // failes when root->0 and count=1
    *count = *count + 1;
    printa("inorder", list, *count);
    list = traverse(root->right, list, bsize, count);
  }
  return list;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *inorderTraversal(struct TreeNode *root, int *returnSize) {
  int bsize = buffer_block_size;
  int count = 0;
  int *list = calloc(bsize,sizeof(int));
  for (int i = 0; i < bsize; i++) {
    list[i] = 0;
  }
  printf("list %p\n", list);
  list = traverse(root, list, &bsize, &count);
  printf("bsize %d count %d\n", bsize, count);
  *returnSize = count;
  return list;
}
struct TreeNode* new_tree(int val) {
  struct TreeNode *node= calloc(1, sizeof(struct TreeNode));
  node->val = val;
  return node;
}
int main() {
  struct TreeNode *root = new_tree(1);
  struct TreeNode *cur = root;
  int i=0;
  while(i < 20) {
 	cur->left = new_tree(++i);
 	cur->right = new_tree(++i);
	cur = cur->right;
  }
  
  //struct TreeNode right = {.left = NULL, .right = NULL, .val = 3};
  //struct TreeNode left = {.left = NULL, .right = &right, .val = 1};
  //struct TreeNode root = {.left = &left, .right = NULL, .val = 2};

  int returnSize = 0;
  int *list = inorderTraversal(root, &returnSize);
  printa("final", list, returnSize);
  free(list);
  return 0;
}
