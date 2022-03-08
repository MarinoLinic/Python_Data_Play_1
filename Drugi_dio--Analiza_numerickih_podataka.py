import csv
import statistics as st
import math as m
import matplotlib.pyplot as plt

with open("Migracija.csv", "r") as f:
    podaci = list(csv.reader(f, delimiter=';'))

izlaz = open('vanjska_datoteka.txt', 'w', encoding="utf-8")

def glavna_funkcija():

    def zbroj(x):
        return sum(x)

    def aritm_sredina(y):
        return st.mean(y)

    def modd(z):
        z = "X" #mod ne postoji, a ne može se koristiti st.mode() ako ga nema
        return z

    def medijan(a):
        return st.median(a)

    def devijacija(b):
        return st.stdev(b)

    def minimum(c):
        return min(c)

    def maksimum(d):
        return max(d)

    # stavljanje svih elemenata u jednu listu
    sve = []
    for i in podaci:
        for j in i:
            sve.append(j)

    # duljina liste 'sve'
    duljina_sve = len(sve)

    # Lista za nazive gradova
    nazivi = []
    j = 2 #preskakanje prvih elemenata
    while j < duljina_sve:
        nazivi.append(sve[j])
        j += 4 #preskakanje elemenata s godinama

    # Lista za 2011
    dvije_tisuce_jedanaesta = []
    j = 3
    while j < duljina_sve:
        dvije_tisuce_jedanaesta.append(sve[j])
        j += 4

    # Lista za 2015
    dvije_tisuce_petnaesta = []
    j = 4
    while j < duljina_sve:
        dvije_tisuce_petnaesta.append(sve[j])
        j += 4

    # Lista za 2018
    dvije_tisuce_osamnaesta = []
    j = 5
    while j < duljina_sve:
        dvije_tisuce_osamnaesta.append(sve[j])
        j += 4

    # Pretvaranje elemenata liste u brojeve (int)
    dvije_tisuce_jedanaesta = list(map(int, dvije_tisuce_jedanaesta))
    dvije_tisuce_petnaesta = list(map(int, dvije_tisuce_petnaesta))
    dvije_tisuce_osamnaesta = list(map(int, dvije_tisuce_osamnaesta))

    # Podaci za 2011
    suma_2011 = zbroj(dvije_tisuce_jedanaesta) #Suma
    aritm_2011 = aritm_sredina(dvije_tisuce_jedanaesta) #Aritmetička sredina
    mod_2011 = modd(dvije_tisuce_jedanaesta) #Mod
    medi_2011 = medijan(dvije_tisuce_jedanaesta) #Medijan
    stddev_2011 = devijacija(dvije_tisuce_jedanaesta) #Standardna devijacija
    minimum_2011 = minimum(dvije_tisuce_jedanaesta) #Minimum
    maksimum_2011 = maksimum(dvije_tisuce_jedanaesta) #Maksimum

    # Podaci za 2015
    suma_2015 = zbroj(dvije_tisuce_petnaesta) #Suma
    aritm_2015 = aritm_sredina(dvije_tisuce_petnaesta) #Aritmetička sredina
    mod_2015 = modd(dvije_tisuce_petnaesta) #Mod
    medi_2015 = medijan(dvije_tisuce_petnaesta) #Medijan
    stddev_2015 = devijacija(dvije_tisuce_petnaesta) #Standardna devijacija
    minimum_2015 = minimum(dvije_tisuce_petnaesta) #Minimum
    maksimum_2015 = maksimum(dvije_tisuce_petnaesta) #Maksimum

    # Podaci za 2018
    suma_2018 = zbroj(dvije_tisuce_osamnaesta) #Suma
    aritm_2018 = aritm_sredina(dvije_tisuce_osamnaesta) #Aritmetička sredina
    mod_2018 = modd(dvije_tisuce_osamnaesta) #Mod
    medi_2018 = medijan(dvije_tisuce_osamnaesta) #Medijan
    stddev_2018 = devijacija(dvije_tisuce_osamnaesta) #Standardna devijacija
    minimum_2018 = minimum(dvije_tisuce_osamnaesta) #Minimum
    maksimum_2018 = maksimum(dvije_tisuce_osamnaesta) #Maksimum

    izlaz.write('IMIGRACIJA U HRVATSKU IZ INOZEMSTVA PO ŽUPANIJAMA\n\n' + '\t\t\t2011\t2015\t2018' + '\n' +
                '---------------------------------------------\n' +
                'Suma:\t\t\t' + str(suma_2011) + '\t' + str(suma_2015) + '\t' + str(suma_2018) + '\n' +
                'Aritmetička sredina*:\t' + str(m.trunc(aritm_2011)) + '\t' + str(m.trunc(aritm_2015)) + '\t' + str(m.trunc(aritm_2018)) + '\n' +
                'Mod:\t\t\t' + mod_2011 + '\t' + mod_2015 + '\t' + mod_2018 + '\n' +
                'Medijan:\t\t' + str(medi_2011) + '\t' + str(medi_2015) + '\t' + str(medi_2018) + '\n' +
                'Standardna devijacija*:\t' + str(m.trunc(stddev_2011)) + '\t' + str(m.trunc(stddev_2015)) + '\t' + str(m.trunc(stddev_2018)) + '\n' +
                'Minimum:\t\t' + str(minimum_2011) + '\t' + str(minimum_2015) + '\t' + str(minimum_2018) + '\n' +
                'Maksimum:\t\t' + str(maksimum_2011) + '\t' + str(maksimum_2015) + '\t' + str(maksimum_2018) + '\n'
                '\n\n\n*Aritmetička sredina i standardna devijacija prikazane su bez decimalnih mjesta.')

    izlaz.close()
    
    # -------- GRAFIKON --------
    broj_im = [suma_2011, suma_2015, suma_2018]
    godine = ['2011.', '2015.', '2018.']
    
    plt.figure(figsize = [7,4], dpi = 400)
    plt.title('Prikaz totalne (sume) imigracije iz inozemstva')
    plt.xlabel('Godina')
    plt.ylabel('Broj imigranata')
    plt.grid(axis='y', linestyle="--", color="grey", alpha = 0.2, zorder = 0)
    plt.bar(godine, broj_im, color = '#800000', zorder = 2)
    plt.savefig('grafikon_slika_zad_2.png')
    plt.show()

    return

if __name__ == '__main__':
    glavna_funkcija()