N = int(input())

arr = []

for i in range(N):
    name = input()
    arr.append(name)

new_arr = arr[:]
arr.sort()

if arr == new_arr:
    print("INCREASING")
elif arr == new_arr[::-1]:
    print("DECREASING")
else:
    print("NEITHER")