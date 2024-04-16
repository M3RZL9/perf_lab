import sys

def circular_array_path(n, m):
    arr = m * [int(i) for i in range(1, n + 1)]
    path_temp = [0]
    path = []
    cnt = 0

    while path_temp[-1] != 1:
        path_temp.clear()
        for i in range(cnt, m + cnt):
            path_temp.append(arr[i])
            cnt += 1
        path_temp_copy = path_temp.copy()
        path.append(path_temp_copy)
        cnt -= 1
    
    path_temp.clear()

    for i in range(len(path)):
        path_temp.append(str(path[i][0]))

    return path_temp 


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("How to use: python3 task1.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    print("".join(circular_array_path(n, m)))

 












