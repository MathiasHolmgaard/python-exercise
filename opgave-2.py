# Find ud af hvordan du med en løkke-struktur kan lægge tallene sammen fra 1 til 100, begge inklusive, og udskrive resultatet.

# syntax for for loops er nedenfor
# for variabel in sekvens:

sum = 0

for tal in range(1, 100):
# tallet 101 anvendes for at skrive et tal efter det sidste jeg ønsker i rækken. På denne måde så er rangen alle tal fra 1 til 100.
    sum = int(sum) + int(tal)    
    
print("Summen er:", sum)
