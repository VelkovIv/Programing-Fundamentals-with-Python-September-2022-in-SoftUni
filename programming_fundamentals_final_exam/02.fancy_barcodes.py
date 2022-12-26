import re

pattern = r'(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})'

number_of_lines = int(input())

for line in range(number_of_lines):
    current_barcode = input()

    extracted_barcode = re.findall(pattern, current_barcode)

    if len(extracted_barcode) == 0:
        print('Invalid barcode')
    else:
        product_group_def = re.findall('\\d', extracted_barcode[0][1])

        if len(product_group_def) == 0:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(product_group_def)}")
