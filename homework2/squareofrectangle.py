w, h = map(int, input("Введите ширину и высоту прямоугольника: ").split())
a = int(input("Введите количество квадратов: "))
Matrix = [[0 for x in range(w)] for y in range(h)]
count = 0
Square = w * h
for step in range(0, a, 1):
    x1, y1, x2, y2 = map(int, input("Введите координаты в виде x1 y1 x2 y2: ").split())
    for i in range(x1, x2):
        for z in range(y1, y2):
            Matrix[i][z] = 1

for i in range(len(Matrix)):
    for z in range(len(Matrix[i])):
        if Matrix[i][z] == 1:
            count += 1

result = Square - count
print(result)
