import math

# Benutzerdefinierte Eingabe der Parameter
print("Gib die Parameter für die quadratische Gleichung ax^2 + bx + c = 0 ein:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Berechnung der Diskriminante
discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("Die Gleichung hat keine reellen Lösungen.")
else:
    # Berechnung der Nullstellen
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    print(f"Die Nullstellen der Gleichung sind: x1 = {x1}, x2 = {x2}")