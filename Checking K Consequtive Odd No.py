T = int(input())
nk = []
arr1 = []
for i in range(T):
    [n, k] = input().split(" ")
    nk.append([n, k])
    arr1.append(input().split(" "))

for i in range(T):

    n = int(nk[i][0])
    k = int(nk[i][1])
    arr = arr1[i]
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    if (k > n):
        print("no")

    else:

        for i in range(n):
            flag = 0
            if (i + k - 1 > n - 1):
                flag = 1
                break

            for j in range(i, i + k):
                if (arr[j] % 2 == 0):
                    flag = 1
                    break

            if (flag == 0):
                break
        if (flag == 0):
            print("yes")

        else:
            print("no")