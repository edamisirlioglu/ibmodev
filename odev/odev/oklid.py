import math

# Öklid Mesafesi Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.
    point1: (x1, y1) şeklinde bir demet (tuple)
    point2: (x2, y2) şeklinde bir demet (tuple)
    """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 1), (3, 5)]  # Örnek nokta listesi
distances = []  # Mesafeleri tutmak için boş liste

# Mesafelerin Hesaplanması
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktaların tekrarlanmasını önlemek için
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"Mesafe {points[i]} ve {points[j]} arasında: {distance:.2f}")

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print(f"\nEn küçük mesafe: {min_distance:.2f}")
