import periodictable

# simple code for special seperate  element
"""
element = periodictable.Rn

print("Name:",element.name)
print("Symbol:",element.symbol)
print("Atomic Number:",element.number)
print("Atomic Mass:",element.mass)
print("Density (g/cm^3):",element.density)
"""
"""

# for taking the name  of the element as  input 


import periodictable

# User se element name lo (e.g. sodium)

name = input("Enter the name of the element (e.g. sodium, oxygen): ").strip().lower()

found = False

# Periodic Table ke sabhi elements loop me check karo
for element in periodictable.elements:
    if element and element.name.lower() == name:
        print("Name:", element.name)
        print("Symbol:", element.symbol)
        print("Atomic Number:", element.number)
        print("Atomic Mass:", element.mass)
        print("Density (g/cm^3):", element.density)
        found = True
        break

if not found:
    print("❌ Element not found. Please check the spelling.")
    
    """



# To take the symbol of element as input 

import periodictable

# User se element ka symbol input lo
symbol = input("Enter the symbol of the element (e.g. H, Na, O): ").strip()

# Check if symbol is valid and get element
try:
    element = getattr(periodictable, symbol)

    print("Name:", element.name)
    print("Symbol:", element.symbol)
    print("Atomic Number:", element.number)
    print("Atomic Mass:", element.mass)
    print("Density (g/cm^3):", element.density)

except AttributeError:
    print("❌ Invalid element symbol. Please enter a valid one like H, O, Na, Fe, etc.")


print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎👍👍👍👍👍👍👍👍👍👍👍👍")