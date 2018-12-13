#naiveSolution
m = [[1,2,3],
[4,0,6],
[7,8,9]]
        
def convertZero(test):
    zeroindex = 0
    for row in test:
        if 0 in row:
            for i in range(len(row)):
                if row[i] == 0:
                    zeroindex = i
                row[i] = 0

            

    for row in test:
        row[zeroindex] = 0
        
    print(test)
    
convertZero(m)

