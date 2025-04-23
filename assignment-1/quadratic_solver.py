import math

# Festgelegte Parameter
a = 1
b = 0
c = -4

# Berechnung der Diskriminante
discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("Die Gleichung hat keine reellen Lösungen.")
else:
    # Berechnung der Nullstellen
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    print(f"Die Nullstellen der Gleichung sind: x1 = {x1}, x2 = {x2}")