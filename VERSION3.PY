# Stage 3: Reading from a file (single set of input)
with open("/content/input1", "r") as file:
    line = file.readline().strip()
    a, b, c, t = map(float, line.split())

T = a * t**2 + b * t + c
print(f"At time {t}, the temperature is {T}°C.")