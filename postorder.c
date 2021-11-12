#include <stdio.h>
#include <stdlib.h>

void printa(const char *label, int *arr, int N) {
  printf("%s[%d]: ", label, N);
  for (int i = 0; i < N; i++) {
    printf("%d, ", arr[i]);
  }
  printf("\n");
}

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

size_t buffer_block_size = 64 / 4;

int *traverse(struct TreeNode *cur, int *list, int *count, int *bsize) {
  if (cur) {
    list = traverse(cur->left, list, count, bsize);
    list = traverse(cur->right, list, count, bsize);
    if (*count == *bsize) {
      *bsize = (*bsize) + buffer_block_size;
      size_t newsize = *bsize * sizeof(list[0]);
      printf("realloc %d * %zu %zu %p\n", *bsize, buffer_block_size, newsize, list);
      fflush(stdout);
      list = realloc(list, newsize);
    }
    printf("count %d bsize %d %p\n", *count, *bsize, list);
    fflush(stdout);
    list[*count] = cur->val;
    printa("add", list, *count);
    *count = *count + 1;
  }
  return list;
}
int *postorderTraversal(struct TreeNode *root, int *returnSize) {
  int bsize = buffer_block_size;
  int count = 0;
  int *list = calloc(buffer_block_size, sizeof(int));
  list = traverse(root, list, &count, &bsize);
  *returnSize = count;
  return list;
}

struct TreeNode *new_tree(int val) {
  struct TreeNode *node = calloc(1, sizeof(struct TreeNode));
  node->val = val;
  return node;
}

int main() {
  struct TreeNode *root = new_tree(1);
  struct TreeNode *cur = root;
  int i = 0;
  while (i < 20) {
    cur->left = new_tree(++i);
    cur->right = new_tree(++i);
    cur = cur->right;
  }

  // struct TreeNode right = {.left = NULL, .right = NULL, .val = 3};
  // struct TreeNode left = {.left = NULL, .right = &right, .val = 1};
  // struct TreeNode root = {.left = &left, .right = NULL, .val = 2};

  int returnSize = 0;
  int *list = postorderTraversal(root, &returnSize);
  printa("final", list, returnSize);
  free(list);
  return 0;
}
