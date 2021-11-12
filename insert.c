   struct TreeNOde root = build_tree(input, input_size); 

struct TreeNode* build_tree(int* input, size_t input_size) {
   int input[] = {-64,12,18,-4,-53,0,76,0,-51,0,0,-93,3,0,-31,47,0,3,53,-81,33,4,0,-51,-44,-60,11,0,0,0,0,78,0,-35,-64,26,-81,-31,27,60,74,0,0,8,-38,47,12,-24,0,-59,-49,-11,-51,67,0,0,0,0,0,0,0,-67,0,-37,-19,10,-55,72,0,0,0,-70,17,-4,0,0,0,0,0,0,0,3,80,44,-88,-91,0,48,-90,-30,0,0,90,-34,37,0,0,73,-38,-31,-85,-31,-96,0,0,-18,67,34,72,0,-17,-77,0,56,-65,-88,-53,0,0,0,-33,86,0,81,-42,0,0,98,-40,70,-26,24,0,0,0,0,92,72,-27,0,0,0,0,0,0,-67,0,0,0,0,0,0,0,-54,-66,-36,0,-72,0,0,43,0,0,0,-92,-1,-98,0,0,0,0,0,0,0,39,-84,0,0,0,0,0,0,0,0,0,0,0,0,0,-93,0,0,0,98};
   int size = sizeof(input) / sizeof(input[0]);
	struct TreeNode* root = malloc(sizeof(struct TreeNode));
	struct TreeNode* cur = root;
	int i = 0;
	while(i  < input_size) {
	    cur->val = input[i];
	    if (i < input_size) {
		int val = input[i];
		if (val) {
		   cur->left = new TreeNode
		} else {
		}
	    }
	}
	return root;
}

