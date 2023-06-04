import re


def extract_quantity_unit(ingredient_name):
    pattern = r'(\d+(\.\d+)?)?\s*([a-zA-Z]+)?'
    match = re.search(pattern, ingredient_name)
    if match:
        quantity = float(match.group(1)) if match.group(1) else 1.0
        unit = match.group(3) if match.group(3) else ingredient_name
        return quantity, unit
    return None, None


def add_quantity_unit(ingredients):
    for ingredient in ingredients:
        quantity, unit = extract_quantity_unit(ingredient["Original Ingredient Name"])
        ingredient["Quantity Magnitude"] = quantity
        ingredient["Quantity Unit"] = unit


'''
add_quantity_unit(ingredients)

for ingredient in ingredients:
    print(ingredient)
'''
