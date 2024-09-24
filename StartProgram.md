for row in range(1,6):
    print('*'*row)

space_count = 3
col_count = 4
for row in range(1,col_count):
    space_count = col_count - row -1
    print(' ',end='')
    print(' '*space_count+'*'*row)

col_count = 5
space_count = 0
for row in range(1,col_count+1):
    space_count = col_count - row
    print(' '*space_count,end=' ')
    print('*' + (' ' + '*') * (row - 1))


col_count = 5
for row in range(1,col_count+1):
    print('*' + (' ' + '*') * (row - 1))
    
    
    
