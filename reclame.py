from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."
    return tekst.replace(".", ".")
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
   totaal = sum(inkomsten)
   btw_bedrag = totaal * btw
   tekst = f"Het totaal van inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
   return tekst
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return[laagste, hoogste]
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gem= totaal / aantal
    tekst = f"De gemiddel inkomsten deze week zijn {gem} euro."
    return tekst
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)   
print(meervoudig([10, 5, 3, 2, 1, 2, 9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer