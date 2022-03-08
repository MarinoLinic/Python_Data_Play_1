import re
import matplotlib.pyplot as plt

with open('Linic_Marino_ZastitaAutorskihPrava.txt', 'r', encoding="utf8") as datoteka:
    podaci = datoteka.read()

# Prva funkcija: broj elemenata u listi
def elementi(x):
    x = len(x)
    return x

# Druga funkcija koja sadrži algoritam
def funkcija():
    # Broj riječi u tekstu
    broj_rijeci = re.findall(r'[\w-]+', podaci)

    # Broj razmaka u tekstu
    broj_razmaka = re.findall(r'\s', podaci)

    # Broj brojeva u tekstu
    #broj_brojeva = re.findall(r'\b\d+?\b', podaci) || samo za obične brojeve
    broj_brojeva = re.findall(r'\d+[\/\d.]*|\d', podaci)

    # Broj riječi koje počinju s prvim slovom u imenu
    broj_ime = re.findall(r'\bm\w+?\b', podaci, re.IGNORECASE)

    # Broj riječi koje počinju s prvim slovom u prezimenu
    broj_prezime = re.findall(r'\b\w+?l\b', podaci, re.IGNORECASE)

    print('Ukupan broj riječi:', elementi(broj_rijeci), '\nUkupan broj razmaka:', elementi(broj_razmaka),
          '\nUkupan broj brojeva:', elementi(broj_brojeva),
          '\nUkupan broj riječi koje počinju s prvim slovom imena studenta:', elementi(broj_ime),
          '\nUkupan broj riječi koje završavaju s prvim slovom prezimena studenta:', elementi(broj_prezime))
    return

funkcija() #pozivanje glavne (druge) funkcije

# -------- HISTOGRAM --------
jedno = len(re.findall(r'\b[a-zšđčćž]{1}\b', podaci, re.IGNORECASE))
dva = len(re.findall(r'\b[a-zšđčćž]{2}\b', podaci, re.IGNORECASE))
tri = len(re.findall(r'\b[a-zšđčćž]{3}\b', podaci, re.IGNORECASE))
cetiri = len(re.findall(r'\b[a-zšđčćž]{4}\b', podaci, re.IGNORECASE))
pet = len(re.findall(r'\b[a-zšđčćž]{5}\b', podaci, re.IGNORECASE))
sest_plus = len(re.findall(r'\b[a-z]{6,}\b', podaci, re.IGNORECASE))

frekvencije = [jedno, dva, tri, cetiri, pet, sest_plus]
data_set = ['1', '2', '3', '4', '5', '6+']

plt.figure(figsize = [6,4], dpi = 400)
plt.title('Histogram frekvencije pojavljivanja riječi s različitim duljinama')
plt.xlabel('Broj slova u riječi')
plt.ylabel('Frekvencija')
plt.grid(axis='y', linestyle="--", color="grey", alpha = 0.2, zorder = 0)
plt.bar(data_set, frekvencije, color = '#006666', zorder = 2)
plt.savefig('histogram_slika_zad_1.png')
plt.show()
