def solution(N):
    binary = bin(N)
    count = 0
    countGap = 0
    for i in binary:
        if i == '0':
            count += 1
        else:
            if countGap < count:
                countGap = count
            count = 0

    return countGap

number = int(input("Type a number to see its longest binary gap: "))

print(solution(number))