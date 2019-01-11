barcode = "857192004015"

digits = list(barcode)
check_digit = int(digits[-1])
del digits[-1]
upc_11 = []
while len(digits) > 0:
    upc_11.append(int(digits[0]))
    del digits[0]

checksum = ((sum(upc_11[0::2]) * 3) + sum(upc_11[1::2]))
m = checksum % 10       # checksum modulo

print("Kontroll number triibkoodil on " + str(check_digit))

if m == 0:
    print("Triibkoodi kontroll number peaks olema 0")
else:
    m2 = 10 - m
    print("Triibkoodi kontroll number peaks olema " + str(m2))

