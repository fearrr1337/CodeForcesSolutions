figures = {"Tetrahedron": 4,
           "Cube": 6,
           "Octahedron": 8,
           "Dodecahedron": 12,
           "Icosahedron": 20
           }

n = int(input())

sumf = 0

for i in range(n):
    figure = input()

    sumf += figures[figure]

print(sumf)