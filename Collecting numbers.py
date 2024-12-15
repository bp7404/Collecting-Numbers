def count_rounds(n, arr):
    ans = 1

    # Array to store the index of numbers from 1 to N
    indices = [0] * (n + 1)

    # Store the index of all elements of arr[]
    for i in range(n):
        indices[arr[i]] = i

    # If num occurs after (num + 1), increment ans by 1
    for num in range(1, n):
        if indices[num + 1] < indices[num]:
            ans += 1
    return ans

# Adatok beolvasása
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(count_rounds(n, arr))
