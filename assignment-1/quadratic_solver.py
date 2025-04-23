import math
import cmath  # Für komplexe Zahlen

# Funktion zur Berechnung der Diskriminante
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

# Funktion zur Berechnung der Nullstellen
def solve_quadratic(a, b, c, discriminant):
    if discriminant < 0:
        # Komplexe Lösungen
        return lambda: (
            (-b + cmath.sqrt(discriminant)) / (2 * a),
            (-b - cmath.sqrt(discriminant)) / (2 * a)
        )
    elif discriminant == 0:
        # Doppelte Nullstelle
        return lambda: (-b / (2 * a),)
    else:
        # Reelle Nullstellen
        return lambda: (
            (-b + math.sqrt(discriminant)) / (2 * a),
            (-b - math.sqrt(discriminant)) / (2 * a)
        )

# Funktion zur Ausgabe der Ergebnisse
def display_results(results):
    if len(results) == 1:
        print(f"Die Gleichung hat eine doppelte Nullstelle: x = {results[0]}")
    elif isinstance(results[0], complex):
        print(f"Die Gleichung hat komplexe Lösungen: x1 = {results[0]}, x2 = {results[1]}")
    else:
        print(f"Die Nullstellen der Gleichung sind: x1 = {results[0]}, x2 = {results[1]}")

# Hauptfunktion zur Eingabe und Verarbeitung
def main():
    print("Gib die Parameter für die quadratische Gleichung ax^2 + bx + c = 0 ein:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    discriminant = calculate_discriminant(a, b, c)
    results_function = solve_quadratic(a, b, c, discriminant)
    results = results_function()
    display_results(results)

# Programm ausführen
if __name__ == "__main__":
    main()