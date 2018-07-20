sal = float(raw_input())

if sal <= 1000:
    sal *= 1.2
elif sal > 1000 and sal <= 1500:
    sal *= 1.15
elif sal > 1500 and sal <= 2000:
    sal *= 1.1
else:
    sal *= 1.05

print("%.2f" %sal)