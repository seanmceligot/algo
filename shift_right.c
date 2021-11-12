#include <stdio.h>

void printa(const char* label, int* arr, int N) {
	printf(label);
	printf(": ");
	for (int i =0; i < N; i++) {
		printf("%d, ", arr[i]);
	}
	printf("\n");
}
void duplicateZeros(int* arr, int arrSize) {    
		printf("arrSize %d\n", arrSize);
    for(int i=0;i<arrSize;i++) {
				printf("test %d %d\n", i, arr[i]);
        if (arr[i] == 0) {
            for (int j=arrSize-1; j>i; j--) {
              arr[j] = arr[j-1];
            }
						printa("shift_right", arr, arrSize);
						i++;
        }
    }
}
void main() {
	int arr[]  = {1,0,2,3,0,4,5,0};
  unsigned int N=sizeof(arr)/sizeof(int);
	printa("start", arr, N);
	duplicateZeros(arr,N );
	printa("done", arr, N);
}
