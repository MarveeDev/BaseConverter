from functions import *
class App():
    def __init__(self):
        # Input da tastiera
        n = input("Inserire un numero in qualsiasi base (base max = 16): ").upper()
        base_p = int(input("Inserire la base di partenza (<= 16): "))
        base_a = int(input("Inserire la base di arrivo (<= 16): "))
        # Casistica base 8 - base 16 e viceversa
        if (base_p == 8 and base_a == 16) or (base_p == 16 and base_a == 8):
            a = base816base2(n, base_p)
            b = base2base816(a, base_a)
            print(f"Il numero {n} in base {base_p} corrisponde al numero {b} in base {base_a}")
        else:
            # Tutte le altre casistiche
            precisione = int(input("Inserire la precisione: "))
            a = baseNbase10(n, base_p)
            b = base10baseM(a, base_a, precisione)
            print(f"Il numero {n} in base {base_p} corrisponde al numero {b} in base {base_a} (in caso di float le ultime cifre decimali potrebbero risultare cancellate)")
if __name__ == "__main__":
    app = App()
