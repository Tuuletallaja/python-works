a = float(input("Palun sisesta kroonide summa, mida teisendada eurodesse"))

e_kurss = 16.6466

eurod = a * e_kurss
print(eurod)
print(str(a) + " krooni on " + str("%.2f" % eurod) + " eurot")