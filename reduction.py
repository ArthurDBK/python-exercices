montant = float(input("Quel est le montant de l'achat ? "))

if montant >= 200:
    montant_final = montant * 0.85
elif montant >= 100 :
    montant_final = montant *0.90
else:
    montant_final = montant

print(f"Montant final : {montant_final:.2f} €")