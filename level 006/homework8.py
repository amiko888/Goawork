#ki sheudzlia miighos 1ze meti argumenti
pairs = [(1, 2), (3, 4), (5, 6)]

for a, b in pairs:
    print(a, b)


colors = ["red", "blue", "green"]

for index, color in enumerate(colors):
    print(index, color)


names = ["Ana", "Gio"]
ages = [18, 22]

for name, age in zip(names, ages):
    print(name, age)
