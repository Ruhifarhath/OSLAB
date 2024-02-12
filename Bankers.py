if __name__ == "__main__":
    n = 5  # Number of processes
    m = 3  # Number of resources
    alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]  # Allocation matrix
    max1 = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]  # Maximum need matrix
    avail = [3, 3, 2]  # Available resources

    f = [0] * n  # Flags to check if a process is already in the safe sequence
    ans = []  # Stores the safe sequence

    for k in range(n):
        f[k] = 0
        need = [[0 for i in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                need[i][j] = max1[i][j] - alloc[i][j]

        for k in range(5):
            for i in range(n):
                if f[i] == 0:
                    flag = 0
                    for j in range(m):
                        if need[i][j] > avail[j]:
                            flag = 1
                            break
                    if flag == 0:
                        ans.append(i)
                        for y in range(m):
                            avail[y] += alloc[i][y]
                        f[i] = 1

    print("Following is the SAFE Sequence")
    for i in range(len(ans) - 1):
        print(" P", ans[i], " ->", sep="", end="")
    if ans:
        print(" P", ans[-1], sep="")
    else:
        print("No safe sequence found.")
