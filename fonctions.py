def appliquer_reduction(montant):
    if montant >= 200:
        return montant * 0.85
    elif montant >= 100:
        return montant * 0.90
    else:
        return montant

for m in [250, 150, 80]:
    final = appliquer_reduction(m)
    print(f"{m} € devient {final:.2f} €")