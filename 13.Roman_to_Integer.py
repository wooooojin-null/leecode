s = 'III'

t = s + '0'
sum = 0
rank = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, '0' : 0}

for i in range(len(s)):

    if rank[ t[i] ] >= rank[ t[i+1] ]:
        sum += rank[ t[i] ]
    else:
        sum -= rank[ t[i] ]

print(sum)