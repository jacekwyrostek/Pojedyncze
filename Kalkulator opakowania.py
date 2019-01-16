import os

start=True
ileHakow=0
index=0

#Funkcja licząca ilości dla jednego haka
def licz(ileHakow, x):
    lFolia=0.4231
    lEtykieta=2
    lZszywki=10
    ileKarton=1
    lPaleta=1

    ileKarton=1/ileHakow
    lFolia=lFolia/ileHakow
    lEtykieta=lEtykieta/ileHakow
    lZszywki=lZszywki/ileHakow
    lPaleta=lPaleta/(ileHakow*x)
    return ileKarton, lFolia, lEtykieta, lZszywki, lPaleta
    

while start:
    print('-'*45)
    print('|%10s|%10s|%10s|%10s|'%('Karton'.center(10),'1200x800'.center(10),'590x370'.center(10),'390x290'.center(10)))
    print('-'*45)
    print('|%10s|%10s|%10s|%10s|'%('Nr'.center(10),'1'.center(10),'2'.center(10),'3'.center(10)))
    print('-'*45)
    karton=input('Wybierz Karton(Nr): ')
    ileHakow=int(input('Podaj ilość haków na karton: '))
    if ileHakow<0 or karton not in ['1','2','3']:
        print('='*50,'\nSPRAWDŹ DANE')
        print('='*50)
    else:
        #Dane dla kartona 1200x800
        if karton == '1':
            ileKarton, lFolia, lEtykieta, lZszywki, lPaleta = licz(ileHakow, 16)
            index='716015036'

        #Dane dla kartona 590x370
        elif karton == '2':
            ileKarton, lFolia, lEtykieta, lZszywki, lPaleta = licz(ileHakow, 16)
            index='716015045'

        #Dane dla kartona 390x290
        elif karton == '3':
            ileKarton, lFolia, lEtykieta, lZszywki, lPaleta = licz(ileHakow, 32)
            index='716015039'

        #Zmiana kropki na przecinek
        ileKarton=str(ileKarton)
        ileKarton=ileKarton.replace(".",",")
        lFolia=str(lFolia)
        lFolia=lFolia.replace(".",",")
        lEtykieta=str(lEtykieta)
        lEtykieta=lEtykieta.replace(".",",")
        lZszywki=str(lZszywki)
        lZszywki=lZszywki.replace(".",",")
        lPaleta=str(lPaleta)
        lPaleta=lPaleta.replace(".",",")

        #Zapis do pliku
        wyjscie = open("Opakowanie.txt", "w")
        print('\n')
        print('-'*40,file=wyjscie)
        print('|%10s|%11s|%15s|'%('Nazwa'.ljust(10),'Indeks'.center(11),'Ilość'),file=wyjscie)
        print('-'*40,file=wyjscie)
        print('|%10s|%11s|%15.8s|'%('Karton'.ljust(10),index.center(11),ileKarton),file=wyjscie)
        print('|%10s|%11s|%15.8s|'%('Folia'.ljust(10),'716990003'.center(11),lFolia),file=wyjscie)
        print('|%10s|%11s|%15.8s|'%('Etykieta'.ljust(10),'716031008'.center(11),lEtykieta),file=wyjscie)
        print('|%10s|%11s|%15.8s|'%('Zszywki'.ljust(10),'700399903'.center(11),lZszywki),file=wyjscie)
        print('|%10s|%11s|%15.8s|'%('Paleta'.ljust(10),'714200110'.center(11),lPaleta),file=wyjscie)
        print('-'*40,file=wyjscie)
        wyjscie.close()
        start=False
        os.startfile("Opakowanie.txt")
