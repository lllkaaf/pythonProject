
x = [['Apple', 2.2],
     ['Microsoft', 1.6],
     ['Amazon',  1.6],
     ['Delta Electronics', 1.4],
     ['Alphabet', 1.2],
     ['Tesla', 0.8]]

n = len(x)

print(n)

m = 0
z = 0

while z < n:

    print('Капитализация компании', x[z][m], 'составляет', x[z][m+1], 'триллиона долларов')
    z = z + 1
