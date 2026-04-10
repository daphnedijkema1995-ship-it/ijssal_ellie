from helper import *
from presentatie import *
import csv

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chcolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}
totaal_inkomsten = som(inkomsten)
presenteer(inkomsten, totaal_inkomsten)
print(totaal_inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
     for key, value in inkomsten.items():
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([key,value])
