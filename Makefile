C         = gcc
ASAN_FLAGS = -fsanitize=address -fno-omit-frame-pointer -Wno-format-security
CFLAGS    := -Wall -Werror --std=gnu99 -ggdb $(ASAN_FLAGS)

run_memory: memory
	pahole memory
	time ./memory | tee memory.log 

run_divide: divide
	pahole divide
	time ./divide | tee divide.log 
.dummy: .py
	python $<
btr_lca:
	python btr_lca.py

my:
	python my_build.py

kc:
	python kc_build.py

gg:
	python gg_insert.py
b:
	#/home/sean/git/python/venv/bin/pycodestyle bst_breadth_first.py
	/home/sean/git/python/venv/bin/python  bst_breadth_first.py

run_postorder: postorder
	pahole postorder
	time ./postorder | tee postorder.log 

run_inorder: inorder
	pahole inorder
	time ./inorder | tee inorder.log 

run_merge2: merge2
	./merge2 | tee merge2.log 
	
merge2:

m: mergesort
	./mergesort | tee mergesort.log
	
mergesort:

g: shift_right
	./shift_right
	
shift_right:
