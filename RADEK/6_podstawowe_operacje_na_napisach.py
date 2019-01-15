s = "Napi powinian tne"

# Powinien byc dlugi na 17 znakow
print ("Dlugosc napisu = %d" % len(s))

# Pierwsza litera 'a' w tekscie powinna miec indeks nr 1
print ("Indeks pierwszej litery 'a' = %d" % s.index("a"))

# W napisie musza byc dwie litery 'a'
print ("'a' wystepuje %d razy" % s.count("a"))

# Dzielenie napisu na kawalki
print ("Pierwszych piec znakow to '%s'" % s[:5])
print ("Nastepne piec znakow to '%s'" % s[5:10])
print ("Dwunastym znakiem jest '%s'" % s[12])

print ("Ostatnie piec znakow to '%s'" % s[-5:])

# Zamien wszystkie male litery na duze
print ("Uzywajac duzych liter: %s" % s.upper())

# Zamien wszystkie litery na male
print ("Uzywajac malych liter: %s" % s.lower())

# Musi sie zaczynac od "Nap"
if s.startswith("Nap"):
    print ("Napis zaczyna sie od 'Nap'. Dobrze!")

# Sprawdzamy jak konczy sie napis
if s.endswith("tne"):
    print ("Napis konczy sie 'tne'. Dobrze!")

# Rozdziela napis na trzy czesci,
# z ktorych kazda zawiera tylko jedno slowo
print ("Napis rozdzielony na slowa: %s" % s.split(" "))