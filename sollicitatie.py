# Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
# In bezit van een Diploma MBO-4 ondernemen
# In bezit van een geldig Vrachtwagen rijbewijs
# In bezit van een hoge hoed
# Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm
# Is langer dan 150 cm
# Is zwaarder dan 90 kg
# Heeft Certificaat “Overleven met gevaarlijk personeel”

ongeschikt = ("je bent niet geschikt voor deze baan")
geschikt = ("je bent geschikt voor deze baan")
soort_diplomas = ["mavodiploma","havodiploma","vwodiploma"]
havo = ("havodiploma")
print("dieren-dressuur of jongleren of acrobatiek")
ervaring = input("heb je ervaring in een van deze dingen:")
if ervaring == "ja":
    jaren = input("hoeveel jaren heb daar ervaring in? ")
    if int(jaren) < 3:
        print(ongeschikt)
    else:
        diploma = input("heb je een MBO 4 diploma?")
        if diploma == "nee":
            soort_diploma = input("wat voor diploma heb je? ")
            if soort_diploma == havo:
                print("top")
            else:
                print(ongeschikt)


        else:
           bezit = input("ben je in het bezit van een vrachtwagen rijbewijs? ")
           if bezit =="nee":
               print(ongeschikt)
           else:
                hoed = input("ben je in het bezit van een hoge hoed? ")
                if hoed == "nee":
                    print(ongeschikt)
                else:
                    manOfvrouw = input("ben je een man en heb je een snor of ben je een vrouw met rood haar?")
                    if manOfvrouw == "nee":
                        print(ongeschikt)
                    else:
                        lengte = input("ben je langer 150 centimeter?")
                        if lengte == "nee":
                            print(ongeschikt)
                        else:
                            gewicht = input("ben je zwaarder dan 90 kg? ")
                            if gewicht == "nee":
                                print(ongeschikt)
                            else:
                                certificaat = input("heb je een cerrtificaat genaamd overleven met gevaarlijk personeel? ")
                                if certificaat == "ja":
                                    print(geschikt)
                                elif certificaat == "nee":
                                    print(ongeschikt)
                    

                
else:
    print(ongeschikt)