def three_sum_zero(A):
    num_found = 0

    N = len(A)
    print(A)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                print("test", [i, j, k])
                if A[i] + A[j] + A[k] == 0:
                    #  print(A[i], A[j], A[k])
                    num_found += 1

    return num_found


print(three_sum_zero([1, 2, -3, 4]))
