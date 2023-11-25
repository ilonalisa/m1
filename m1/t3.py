units = input("Введіть одиниці вимірювання (фути або метри): ")
width = float(input(f"Введіть ширину кімнати у {units}: "))
length = float(input(f"Введіть довжину кімнати у {units}: "))

area = width * length

print(f"Площа кімнати: {area} {units} квадратних")