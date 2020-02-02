#import readline
import shlex
import random
#pre config
dozwolone_parametry = (
        "dstrening", "dstest", "dswalidacja", "features", "dsfiltrowany", "target", "wierszeklasy", "lst",
        "etykiety")
zmienna1=()
naglowek=()
etykiety=()
kolumny=()
sciezka=()
lst = list()
features = list()
target = list()
wierszeklasy = list()
min=0
max=0
dstrening=list()
dstest=list()
dswalidacja=list()
listawierszy=0
pomocniczny1=0
#instrukcja

print('Komenda "help" przywoluje pomoc, "exit" konczy aplikacje; ponizej dostepne komendy oraz ich atrybuty pomocnicze : ')
print('kolejnosc wykonywania komend: i , e, k, w, s, f')
print(
    'komenda "import,sciezka" lub "i" w argumencie sciezka podaj nazwe pliku datasetu lub przyjmuje domyslna wartosc iris.csv')
print("komenda 'etykiety T/N' lub 'e,T/N' w argumencie podajemy czy dataset posiada naglowki domyslnie 'T'")
print("komenda 'klasy,' lub 'k' zwraca unikatowe wartosci dla klasy decyzyjnej(ostatnia kolumna)")
print(
    "komenda 'wierszeklasy,1-n' lub 'w,1-n' zwraca wiersze wybranej klasy (unikatowe wartosci z ostatnia kolumna 1-n kolejnosc z listy wystepowania - przywolaj poleceniem 'e')")
print(
    "komenda 'filtrdataset min(int) max(int)' lub 'f,min,max' w argumencie podajemy wartosci min i max dla filtra datasetu domyslnie min=0 max=ostatni wiersz")
print(
    "komenda 'splitdataset trening(float) test(float) walidacja(float)' lub 's,trening,test,walidacja' w argumentach podajemy wartosci podzialu datasetu domyslne wartosci 0.7 0.15 0.15 suma musi byc równa 1 lub <1")
print(
	"komenda 'save,nazwapliku,lista wartosci' zapisz wartosci swoich filtrow lub datasetów dostępne argumenty dla listy wartości",dozwolone_parametry)


while True: #glowna petla

    print(
        'Komenda "help" przywoluje pomoc, "exit" konczy aplikacje; ponizej dostepne komendy oraz ich atrybuty pomocnicze : ')
    print('kolejnosc wykonywania komend: i , e, k, w, s, f')

    cmd, *args = shlex.split(input('> '))
    if cmd=='exit':
        break

    elif cmd=='help':
        print('Komenda "help" przywoluje pomoc, "exit" konczy aplikacje; ponizej dostepne komendy oraz ich atrybuty : ')
        print('kolejnosc wykonywania komend: i , e, k, w, s, f')
        print('komenda "import,sciezka" lub "i" w argumencie sciezka podaj nazwe pliku datasetu lub przyjmuje domyslna wartosc iris.csv')
        print("komenda 'etykiety T/N' lub 'e,T/N' w argumencie podajemy czy dataset posiada naglowki domyslnie 'T'")
        print("komenda 'klasy,' lub 'k' zwraca unikatowe wartosci dla klasy decyzyjnej(ostatnia kolumna)")
        print("komenda 'wierszeklasy,1-n' lub 'w,1-n' zwraca wiersze wybranej klasy (unikatowe wartosci z ostatnia kolumna 1-n kolejnosc z listy wystepowania - przywolaj poleceniem 'e')")
        print("komenda 'filtrdataset min(int) max(int)' lub 'f,min,max' w argumencie podajemy wartosci min i max dla filtra datasetu domyslnie min=0 max=ostatni wiersz")
        print("komenda 'splitdataset trening(float) test(float) walidacja(float)' lub 's,trening,test,walidacja' w argumentach podajemy wartosci podzialu datasetu domyslne wartosci 0.7 0.15 0.15 suma musi byc równa 1 lub <1")
    elif cmd=='import' or cmd=='i': #importowanie pliku csv
        if len(args) == 0:
            sciezka = "iris.csv"
        else:
            zmienna1 = args[0]
            sciezka = str(zmienna1)
        print('Adres pliku to: "%s"' % (str(sciezka)))
        lst = list()
        with open(str(sciezka)) as ds:
            for line in ds:
                lst.append(line.rstrip())
                kolumny = line.rstrip('\n').count(",") + 1
                listawierszy =+ 1
        print(lst)

    elif cmd=='etykiety' or cmd=='e': #importowanie etykiety lub generowanie numerów kolumn i ich echo
        if pomocniczny1==1:
            print("Załadowano etykiety", etykiety)
        elif len(args) == 0:
            etykiety = lst.pop(0).split(",")
            print("Załadowano etykiety", etykiety)
            pomocniczny1=1
        else:
            if args[0] == 'T':
                etykiety = lst.pop(0).split(",")
                print("Załadowano etykiety", etykiety)
                pomocniczny1=1
            else:
                kolumny = lst[0].count(",") + 1
                etykiety = range(1, kolumny, 1)
                pomocniczny1=1
            print("Brak etykiet, nadano kolejne numery")

    elif cmd=='klasy' or cmd=='k': #export unikatowych klas i ich echo
        for linia in lst:
            x = linia.split(",")
            features.append(x)
            if x[kolumny - 1] not in target:
                target.append(x[kolumny - 1])
        print("Unikatowe klasy to:",target)
        listawierszy=len(features)

    elif cmd=='wierszeklasy' or cmd=='w': #eksport linii dla wybranej klasy i ich echo
        if len(args)==0:
            print("wybrano domyslne wartosci - klasa #0")
            indexklasy=0
        else:
            if int(args[0])>=len(target)-1:
                indexklasy=len(target)-1
            else:
                indexklasy=int(args[0])
        for linia in lst :
            x = linia.split(",")
            if x[kolumny - 1] == target[indexklasy]:
                wierszeklasy.append(x)
        print("Wiersze z klasy ",target[indexklasy]," to: ",wierszeklasy)

    elif cmd=='filtrdataset' or cmd=='f': #filtrowanie wierszy po indeksach 0:n i echo wierszy
        if len(args)==0 or len(args)==1:
            print("wybrano domyslne wartosci")
            dsfiltrowany = features[0:listawierszy]
        else:
            min, max = tuple(args)
            dsfiltrowany=features[int(args[0]):int(args[1]):1]
        print("Przefiltrowany dataset :",dsfiltrowany)
    elif cmd=='splitdataset' or cmd=='s': #tworzenie 3 datasetów i echo statystyki plus wartosci dla datasetów

        print(sum([float(i) for i in args ]),sum(float(i) for i in args))
        if len(args) == 0 or len(args) == 1 or len(args) == 2 or sum(float(i) for i in args)> 1.0 or all(type(i) is int for i in args):
            print("wybrano domyslne wartosci")
            filtrtrening = 0.7
            filtrtest = 0.15
            filtrwalidacja = 0.15

        else:
            filtrtrening = float(args[0])
            filtrtest = float(args[1])
            filtrwalidacja = float(args[2])
        max = len(features)
        random.shuffle(features)
        dstrening = features[:int((len(features)) * filtrtrening )]
        dstest = features[int((len(features)) * filtrtrening):int(len(features) * (filtrtest + filtrtrening))]
        dswalidacja = features[int(len(features) * (filtrtest + filtrtrening)):int(len(features) * (filtrtest + filtrtrening + filtrwalidacja))]
        print("Dataset trening elementów",len(dstrening),"z dostepnych ",max,"lista :",dstrening)
        print("Dataset trening elementów",len(dstest),"z dostepnych ",max,"lista :",dstest)
        print("Dataset trening elementów",len(dswalidacja),"z dostepnych ",max,"lista :",dswalidacja)

    elif cmd=='save': # zapis do pliku mozliwe laczenie danych przez append np etykiety + ds do tego samego pliku


        if len(args)==0 or len(args)==1:
            print("argument 1- nazwa ; dozwolone parametry dla argumentu 2",dozwolone_parametry)
        else:
            if str(args[1]) not in dozwolone_parametry:

                print("podano niedozwolony argument listy")
                pass
            else:

                def write_to_csv(lista_zapis):
                    iterator = 0
                    with open('{0}_{1}.csv'.format(str(args[0]),sciezka), 'a') as csvfile:
                        for domain in lista_zapis:
                            if type(domain)==type(list()):
                                sdomain=",".join(domain)
                                csvfile.write(sdomain + '\n')

                            else:
                                csvfile.write(domain + ',')
                                iterator = iterator+1
                                if len(lista_zapis)==iterator:
                                    csvfile.write('\n')


                write_to_csv(eval(str(args[1])))
    else:
        print('Nieznana komenda: {}'.format(cmd))