// sort into increasing or equal order
void sort(int* ar, int len) {
    for(int i =0; i < len-1; i++) {
        for (int j=0; j < len-i-1; j++) {
            if (ar[j] > ar[j+1]) {
                swap(ar, j, j+1);
                // [0,1] is correct
                // [1,0] swap
                // [1,1] is correct
            }
        }
    }
}

