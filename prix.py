prix_htva = float(input("Quel est le prix htva ? "))
prix_tvac = prix_htva * 1.21
tva = prix_tvac - prix_htva
print(f"Prix TVAC : {prix_tvac:.2f} €")
print(f"Montant de la TVA : {tva:.2f} €")