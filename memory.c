#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

unsigned long long getTotalSystemMemory()
{
    long pages = sysconf(_SC_PHYS_PAGES);
    long page_size = sysconf(_SC_PAGE_SIZE);
    printf("pages %ld\n", pages);
    printf("page_size %ld\n", page_size);
    return pages * page_size;
}
int main(int argc, char** argv) {
	getTotalSystemMemory();
	return 0;
}
