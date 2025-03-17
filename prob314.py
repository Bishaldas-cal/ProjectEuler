import math

def enclosed_area_ratio():
    # The side of the square plot
    side_length = 500
    
    # Cutting off four right triangles with sides 75, 75, and 75√2
    cut_off_area = 4 * (0.5 * 75 * 75)
    
    # Enclosed area after cutting off
    enclosed_area = side_length**2 - cut_off_area

    # Perimeter with four edges of 350 meters and four diagonal edges
    perimeter = 4 * 350 + 4 * (75 * math.sqrt(2))

    # Area-to-wall-length ratio
    ratio = enclosed_area / perimeter

    return round(ratio, 8)

if __name__ == "__main__":
    print(enclosed_area_ratio())
