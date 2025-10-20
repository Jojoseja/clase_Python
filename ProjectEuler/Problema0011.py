def return_grid():
    grid = []
    with open("Resources/Problema0011.txt", 'r') as f:
        for line in f:
            numbers = [int(num) for num in line.split()]
            grid.append(numbers)
    return grid


for i in enumerate(return_grid()):
    print(f" {i[0]}. {i[1]} con longitud {len(i[1])}")