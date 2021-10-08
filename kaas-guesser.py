kleur = input("is de kaas geel? ")
gaten = input("heeft de kaas gaten? ")
schimmel = input("heeft de kaas schimmel? ")
korst =  input("heeft de kaas een korst? ")
duur = input("is de kaas belachelijk duur? ")
hard = input("is de kaas hard als steen? ")

if kleur == "ja":
    if gaten == "ja":
        if duur == "ja":
            print("emmenthaler ")   
        else:
            print("leerdammer ")
    else:
        if hard == "ja":
            print("pammigiano reggiano ")
        else: 
            print("goudse kaas ")
else:
    if schimmel == "ja":
        if korst == "ja":
            print("blue de Rochbaron")
        else:
            print("foume d' Ambert")
    if schimmel == "nee":
        if gaten == "ja":
           print("Camembert")
        else:
            print("Mozzarella")
