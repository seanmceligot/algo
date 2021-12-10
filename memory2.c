// File name: ExtremeC_exampels_chapter4_6.c
// Description: Example 4.6

#include <unistd.h> // Needed for sleep function
#include <stdio.h>

int main(int argc, char** argv) {
  // Infinite loop
  printf("%p\n", main);
  // 558df2aa5149
  // cat /proc/PID/maps 
  // 558df3400000-558df3421000 rw-p 00000000 00:00 0                          [heap]

  while (1) {
    sleep(1); // Sleep 1 second
  };
  return 0;
}
/*
 *
 * ✦ ❯ ./ex4_6.out &
[2] 38660
56361b641149
Extreme-C/ch04-process-memory-structure on  master via △ v3.22.0
✦2 ➜ cat /proc/38660/maps
───────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: /proc/38660/maps
───────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ 56361b640000-56361b641000 r--p 00000000 00:1b 1486893                    /home/sean/git/facebook/Extreme-C/ch04-process-mem
       │ ory-structure/ex4_6.out
   2   │ 56361b641000-56361b642000 r-xp 00001000 00:1b 1486893                    /home/sean/git/facebook/Extreme-C/ch04-process-mem
       │ ory-structure/ex4_6.out
   3   │ 56361b642000-56361b643000 r--p 00002000 00:1b 1486893                    /home/sean/git/facebook/Extreme-C/ch04-process-mem
       │ ory-structure/ex4_6.out
   4   │ 56361b643000-56361b644000 r--p 00002000 00:1b 1486893                    /home/sean/git/facebook/Extreme-C/ch04-process-mem
       │ ory-structure/ex4_6.out
   5   │ 56361b644000-56361b645000 rw-p 00003000 00:1b 1486893                    /home/sean/git/facebook/Extreme-C/ch04-process-mem
       │ ory-structure/ex4_6.out
   6   │ 56361c0a6000-56361c0c7000 rw-p 00000000 00:00 0                          [heap]
   7   │ 7fce7a1b9000-7fce7a1bb000 rw-p 00000000 00:00 0
   8   │ 7fce7a1bb000-7fce7a1e1000 r--p 00000000 00:1b 4012                       /usr/lib/libc-2.33.so
   9   │ 7fce7a1e1000-7fce7a32c000 r-xp 00026000 00:1b 4012                       /usr/lib/libc-2.33.so
  10   │ 7fce7a32c000-7fce7a378000 r--p 00171000 00:1b 4012                       /usr/lib/libc-2.33.so
  11   │ 7fce7a378000-7fce7a37b000 r--p 001bc000 00:1b 4012                       /usr/lib/libc-2.33.so
  12   │ 7fce7a37b000-7fce7a37e000 rw-p 001bf000 00:1b 4012                       /usr/lib/libc-2.33.so
  13   │ 7fce7a37e000-7fce7a389000 rw-p 00000000 00:00 0
  14   │ 7fce7a39d000-7fce7a39e000 r--p 00000000 00:1b 4001                       /usr/lib/ld-2.33.so
  15   │ 7fce7a39e000-7fce7a3c2000 r-xp 00001000 00:1b 4001                       /usr/lib/ld-2.33.so
  16   │ 7fce7a3c2000-7fce7a3cb000 r--p 00025000 00:1b 4001                       /usr/lib/ld-2.33.so
  17   │ 7fce7a3cb000-7fce7a3cd000 r--p 0002d000 00:1b 4001                       /usr/lib/ld-2.33.so
  18   │ 7fce7a3cd000-7fce7a3cf000 rw-p 0002f000 00:1b 4001                       /usr/lib/ld-2.33.so
  19   │ 7ffdda0ef000-7ffdda110000 rw-p 00000000 00:00 0                          [stack]
  20   │ 7ffdda1cf000-7ffdda1d3000 r--p 00000000 00:00 0                          [vvar]
  21   │ 7ffdda1d3000-7ffdda1d5000 r-xp 00000000 00:00 0                          [vdso]
  22   │ ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0                  [vsyscall]
*/
