# Funzione di conversione da una qualsiasi base alla base 10
def baseNbase10(n, base):
    if base > 16 or base <= 1:
        pass
    else:
        esadec = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        r = True
        # Controllo che il numero inserito non contenga cifre maggiori della base
        for i in range(len(n)):
            if '.' in n:
                a = n.split('.')
                for i in range(len(a[0])):
                    if int(esadec.index(a[0][i])) >= base:
                        r = False
                for i in range(len(a[1])):
                    if int(esadec.index(a[1][i])) >= base:
                        r = False
            else:
                for i in range(len(n)):
                    if int(esadec.index(n[i])) >= base:
                        r = False
        if r == False:
            pass
        else:
            # Casistica numero intero (senza la virgola)
            if isinstance(n, int):
                n10 = 0
                c = 0
                # Moltiplico ogni cifra per due elevato alla posizione e le sommo tra loro
                for i in range(len(str(n))-1, -1, -1):
                    n10 += int(str(n)[c])*(base**i)
                    c += 1
                return n10
            # Casistica numero float (con la virgola)
            elif isinstance(n, float):
                c = 0
                parte_intera = str(n).split(".")[0]
                parte_decimale = str(n).split(".")[1]
                parteinteraconv = 0
                partedecimaleconv = 0
                # Conversione parte intera (stesso procedimento del numero intero)
                for i in range(len(str(parte_intera))-1, -1, -1):
                    parteinteraconv += int(str(parte_intera)[c])*(base**i)
                    c += 1
                # Conversione parte decimale
                for i in range(len(str(parte_decimale))):
                    # Moltiplico ogni cifra per due elevato alla posizione in negativo e le sommo tra loro
                    partedecimaleconv += int(str(parte_decimale)[i])*(base**(-i-1))
                partedecimaleconv2 = str(partedecimaleconv).split(".")[1]
                # Unione parte intera con parte decimale
                n10 = float(f"{parteinteraconv}.{partedecimaleconv2}")
                return n10
            # Casistica stringa (Numero in HEX)
            elif isinstance(n, str):
                esadec = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
                # Casistica numero decimale (stesso procedimento della casistica precedente, con aggiunta di sostituzione del numero trovato con l'hex corrispondente (lista soprastante))
                if "." in n:
                    c = 0
                    parte_intera = n.split(".")[0]
                    parte_decimale = n.split(".")[1]
                    parteinteraconv = 0
                    partedecimaleconv = 0
                    for i in range(len(str(parte_intera))-1, -1, -1):
                        parteinteraconv += (esadec.index(n[c]))*(base**i)
                        c+=1
                    for i in range(len(str(parte_decimale))):
                        partedecimaleconv += (esadec.index(parte_decimale[i]))*(base**(-i-1))
                    partedecimaleconv2 = str(partedecimaleconv).split(".")[1]
                    n10 = float(f"{parteinteraconv}.{partedecimaleconv2}")
                    return n10;
                # Casistica numero intero (stesso procedimento numero intero)
                else:
                    n10 = 0
                    c = 0
                    for i in range(len(n)-1,-1,-1):
                        n10 += (esadec.index(n[c]))*(base**i)
                        c += 1
                    return n10;
# Funzione per convertire un numero in base 10 ad una qualsiasi base
def base10baseM(n, base, precisione):
    if base > 16 or base <= 1:
        pass
    else:
        esadec = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        # Casistica numero intero
        if isinstance(n, int):
            conversione = []
            while n > 0:
                # Appendo alla lista i resti relativi alla divisione tra il numero decimale e la base, per poi dividere il numero decimale per la base rimuovendo il resto
                conversione.append(esadec[(n%base)])
                n = n // base
            # Inverto la lista
            conversione.reverse()
            return ''.join(str(v) for v in conversione)
        # Casistica numero decimale
        if isinstance(n, float):
            c = 0
            parte_intera = str(n).split(".")[0]
            parte_decimale = float("0." + str(n).split(".")[1])
            parteinteraconv = []
            partedecimaleconv = []
            # Conversione parte intera (Stesso procedimento della casistica precedente)
            while int(parte_intera)>0:
                parteinteraconv.append(esadec[(int(parte_intera)%base)])
                parte_intera = int(parte_intera) // base
            parteinteraconv.reverse()
            parte_dec = []
            # Conversione parte decimale
            for i in range(precisione):
                if "." in str(parte_decimale):
                    parte_decimale = float(f"0.{str(parte_decimale).split('.')[1]}")
                else:
                    parte_decimale = float(f"0.{parte_decimale}")
                # Moltiplico la parte decimale per la base e salvo in lista la parte intera, continuo invece a lavorare con quella decimale
                parte_decimale = float(parte_decimale)*base
                lista_dec = str(parte_decimale).split(".")[0]
                parte_dec.append(esadec[int(lista_dec)])
            nM = (f"{''.join(str(v) for v in parteinteraconv)}.{''.join(str(v) for v in parte_dec)}")
            parte_dec = []
            return nM
# Funzione per passare da base 8/16 a base 2
def base816base2(n, base):
    esadec = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    # Indico il numero di bit necessari a rappresentare ogni cifra in base 8/16 (esponente potenza)
    num = 4 if base == 16 else 3
    if '.' in n:
        parte_intera = n.split('.')[0]
        parte_decimale = n.split('.')[1]
        parte_intera_lst = []
        parte_decimale_lst = []
        # Conversione parte intera: definisco quoz il numero corrispondente al carattere esadecimale nella posizione i, per il resto procedimento uguale alla funzione basenbase10, con come unica differenza la divisione per 2 e non per la base inserita da tastiera
        for i in range(len(parte_intera)):
            quoz = int(esadec.index((parte_intera[i])))
            quoz_app = ""
            while quoz > 0:
                quoz_app += str(quoz%2)
                quoz = quoz//2
            parte_intera_lst.append(quoz_app)
        # Conrtollo che ogni numero sia composto da num caratteri, se non lo è effettuo un padding a destra per raggiungere il numero num di caratteri, rovescio inoltre ogni numero in modo tale da avere ogni numero nel verso corretto
        for i in range(len(parte_intera_lst)):
            if parte_intera_lst[i] != num:
                parte_intera_lst[i] =  str(parte_intera_lst[i]).ljust(num, "0")
            parte_intera_lst[i] = parte_intera_lst[i][::-1]
        # Conversione parte decimale: procedimento uguale alla conversione della parte intera
        for i in range(len(parte_decimale)):
            quoz = int(esadec.index((parte_decimale[i])))
            quoz_app = ""
            while quoz > 0:
                quoz_app += str(quoz%2)
                quoz = quoz//2
            parte_decimale_lst.append(quoz_app)
        # Controllo che ogni numero sia composto da num caratteri, se non lo è effettuo un padding a sinistra per raggiungere il numero num di caratteri e rovescio anche in questo caso per lo stesso motivo
        for i in range(len(parte_decimale_lst)):
            if parte_decimale_lst[i] != num:
                parte_decimale_lst[i] =  str(parte_decimale_lst[i]).ljust(num, "0")
            parte_decimale_lst[i] = parte_decimale_lst[i][::-1]
        return f"{''.join(str(v) for v in parte_intera_lst)}.{''.join(str(v) for v in parte_decimale_lst)}"
# Funzione per convertire un numero in base 2 in base 8/16
def base2base816(n, base):
    esadec = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    num = 4 if base == 16 else 3
    parte_intera = str(n).split('.')[0]
    #separo le cifre della parte intera a gruppi di num cifre partendo da sinsitra, rovescio poi la lista in modo da avere i numeri nell'ordine corretto
    parte_intera_lst = [str(parte_intera)[::-1][i:i+num] for i in range(0, len(str(parte_intera)), num)]
    parte_intera_lst.reverse()
    # Rovescio ogni elemento della lista in modo da avere i numeri nel verso corretto, inoltre controllo che ogni numero si composto da num cifre, in caso contrario effettuo un padding a sinistra per raggiungere una lunghezza di num cifre
    for i in range(len(parte_intera_lst)):
        parte_intera_lst[i] = parte_intera_lst[i][::-1]
        if len(parte_intera_lst[i]) != num:
            parte_intera_lst[i] = parte_intera_lst[i].zfill(num)
    # Conversione parte intera: stesso procedimento della funzione basenbase10 applicato ai singoli elementi della parte intera
    parte_intera_trad = []
    for item in parte_intera_lst:
        num_trad = sum(int(item[c]) * 2**j for c, j in enumerate(range(len(item) - 1, -1, -1)))

        parte_intera_trad.append(esadec[num_trad])

    parte_decimale = str(n).split('.')[1]
    # Divido la parte decimale a gruppi di num cifre partendo da sinistra e controllo che ogni gruppo sia composto da num cifre, in caso contrario effettuo un padding a destra per raggiungere il numero num di cifre
    parte_decimale_lst = [str(parte_decimale)[i:i+num] for i in range(0, len(str(parte_decimale)), num)]
    parte_decimale_trad = []
    for i in range(len(parte_decimale_lst)):
        if len(parte_decimale_lst[i]) != num:
            parte_decimale_lst[i] = parte_decimale_lst[i].ljust(num, "0")
    # Conversione parte decimale: stesso procedimento della parte intera in quanto utilizzando questo metodo vengono utilizzati procedimenti analoghi (moltiplicare i singoli caratteri dei singoli elementi del numero binario per due elevato alla sua posizione)
    for item_ in parte_decimale_lst:
        num_trad = sum(int(item_[c]) * 2**j for c, j in enumerate(range(len(item_) - 1, -1, -1)))

        parte_decimale_trad.append(esadec[num_trad])
    return f"{''.join(str(v) for v in parte_intera_trad)}.{''.join(str(v) for v in parte_decimale_trad)}"