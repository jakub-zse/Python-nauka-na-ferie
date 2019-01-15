x = object()
y = object()
x_tab = [x]*10
y_tab = [y]*10
duza_tab=x_tab + y_tab
print (len(x_tab))
print (len(y_tab))
print (len(duza_tab))

# sprawdzenie poprawnosci
if x_tab.count(x) == 10 and y_tab.count(y) == 10:
    print ("Prawie zrobione...")
if duza_tab.count(x) == 10 and duza_tab.count(y) == 10:
    print ("Doskonale!")