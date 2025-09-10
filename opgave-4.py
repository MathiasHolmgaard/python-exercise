# Opgave 4 - SHA256 i Python SHA256 er en kryptografisk hashfunktion. Man giver den en streng af vilkårlig længde, og der kommer en hashværdi ud på 256 bit - svarende til 32 bytes. Vi kan ikke bare skrive sådan en hashværdi ud, da en byte kan indeholde alt fra 0 til 255, herunder ikke-printbare tegn. Derfor repræsenterer vi den som en hex-streng, hvor hver byte bliver til 2 hex-tegn, dvs 64 tegn. Det kan se sådan ud: # shatest.py import hashlib pw = "Secret1234" h = hashlib.sha256() h.update(pw.encode('utf-8')) hex = h.hexdigest() print(hex) Strengen pw bliver konverteret til et byte-array med funktionen encode. Derefter får vi hashværdien som hex, og den bliver: 815b0eeca9134e4445afe419300b419b033a306344e5cef549b1b671e9841237 Din opgave er at få programmet til at køre, og give samme udskrift. Derefter skal du finde en anden streng, der også får hashværdien til at begynde med 81. Det kan godt kræve mange forsøg. 

# shatest.py

import hashlib
import random

characters = "ABCDEF0123456789"  # your list of letters and numbers



winningcondition = False
Forsøg = 0

while winningcondition != True:
    Forsøg = Forsøg + 1
    random_string = ''.join(random.choice(characters) for _ in range(8))
    print(random_string)
    
    #pw = "Secret1234"  gammel kode
    pw = random_string 
    h = hashlib.sha256() 
    h.update(pw.encode('utf-8')) 
    hex = h.hexdigest() 
    print(hex)

    if hex[:2] == "81":
        winningcondition = True
        print("Så for satan!")
        print(f"Det tog {Forsøg} forsøg")
        print(f"Koden blev {random_string}")
        break
        






# bogstaver = ["A", "B", "C", "D", "E", "F"]
# # Brug range til tal


# if hex[:2] == "81":
#     print(hex)
#     print("De første to tegn er 81")
#     break # Hvorfor er der rød streg under???!!! Jeg vil breake mit loop hvis de første to tegn er 81 er variablen hex
# else:
#     h.update(pw.encode('utf-8')) 
#     hex = h.hexdigest()
#     print(hex)

    
