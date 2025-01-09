# Stage 4: Reading from a file (multiple sets of inputs)
with open("/content/input2", "r") as file:
    lines = file.readlines()

for line in lines:
    a, b, c, t = map(float, line.strip().split())
    T = a * t**2 + b * t + c
    print(f"At time {t}, with coefficients a={a}, b={b}, c={c}, the temperature is {T}°C.")