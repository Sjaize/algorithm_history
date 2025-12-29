n = int(input())

for _ in range(n):
    test = input()

    # for each test case
    count = 0
    result = 0
    for i in range(len(test)):
        if test[i] == 'O':
            count = count + 1
            result = result + count
        else:
            count = 0
    
    print(result)