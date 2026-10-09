import sys
if len(sys.argv) < 4:
    print("Использование: ./deposit.py <сумма> <ставка_%> <лет>")
    sys.exit(1)
summ = float(sys.argv[1])
stavka = float(sys.argv[2]) / 100
years = int(sys.argv[3])
summ2 = summ * (1 + stavka) ** years
print(f"{summ2:.2f}")
