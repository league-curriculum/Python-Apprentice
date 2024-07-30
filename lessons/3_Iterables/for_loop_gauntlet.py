"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""



# 1.
for i in range(101):
    print(i)

# 2.
for i in range(100, -1, -1):
    print(i)

# 3.
for i in range(2, 101):
    if i % 2 == 0:
        print(i)

# 4.
for i in range(1, 100):
    if i % 2 == 1:
        print(i)

# 5.
for i in range(1, 501):
    if i % 2 == 0:
        print(str(i) + ' is even')
    else:
        print(str(i) + ' is odd')

# 6.
for i in range(7, 778):
    if i % 7 == 0:
        print(i)

# 7.
for i in range(0, 39):
    print('In ' + str(2021 - i) + ' I was ' + str(38 - i) + ' years old')

# Nested 1
for i in range(3):
    for j in range(3):
        print(str(i) + ' ' + str(j))

# Nested 2
for i in range(3):
    row = ''
    for j in range(1, 4):
        row += str((3 * i) + j) + ' '
    print(row)

# Nested 3
for i in range(10):
    row = ''
    for j in range(1, 11):
        row += str((10 * i) + j) + ' '
    print(row)

# Nested 4
stars = '*'
for i in range(6):
    print(stars)
    stars += ' *'

# Nested 4 alternate
for i in range(6):
    stars = ''
    for j in range(i+1):
        stars += '* '
    print(stars)
