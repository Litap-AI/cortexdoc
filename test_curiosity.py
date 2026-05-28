from curiosity_engine import (
    generate_curiosity
)

curiosity = generate_curiosity()

print("\nCURIOSITY ENGINE:\n")

for item in curiosity:

    print("=" * 60)

    print(item)
    