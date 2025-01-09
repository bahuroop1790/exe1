# Stage 2: Keyboard input
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
t = float(input("Enter the time t: "))

T = a * t**2 + b * t + c
print(f"At time {t}, the temperature is {T}°C.")