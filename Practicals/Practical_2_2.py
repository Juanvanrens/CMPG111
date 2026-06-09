len = int(input("Enter the length (cm): "))
wid = int(input("Enter the width (cm): "))

area = len * wid
perimeter = 2*(len+wid)
diagonal = (len**2+wid**2)**0.5

print(f"\nArea of the rectangle is {area:.2f} square cm")
print(f"Perimeter of the rectangle is {perimeter:.1f} cm")
print(f"Diagonal of the rectangle is {diagonal:.3f} cm")

print("\n**Recatangle dimensions**")
print(f"length = {len:.1f} cm    width = {wid:.1f} cm")