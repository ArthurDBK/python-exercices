prix = [19.99, 5.50, 42.00, 8.75]
total_htva = 0

for p in prix:
    total_htva = total_htva + p
    if p > 20:
        print(f"Article cher : {p:.2f} €")

total_tvac = total_htva * 1.21

print(f"Total HTVA : {total_htva:.2f} €")
print(f"Total TVAC : {total_tvac:.2f} €")