C         = gcc
ASAN_FLAGS = -fsanitize=address -fno-omit-frame-pointer -Wno-format-security
CFLAGS    := -Wall -Werror --std=gnu99 -ggdb $(ASAN_FLAGS)
run_divide2: divide2
	pahole divide2
	size divide2
	bash -c "time ./divide2"

run_divide: divide
	pahole divide
	size divide
	bash -c "time ./divide"
run_memory: memory
	pahole memory
	bash -c "time ./memory"

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
	time ./postorder

run_inorder: inorder
	pahole inorder
	time ./inorder

run_merge2: merge2
	./merge2
	
merge2:

m: mergesort
	./mergesort
	
mergesort:

g: shift_right
	./shift_right
	
shift_right:

rs_leetcode:
	cargo run --bin leetcode

remove_from_sorted:
	cargo run --bin remove_from_sorted
rs_scan:
	cargo run --bin scan
rs_sc:
	cargo run --bin scan
rs_993:
	cargo run --bin 993
