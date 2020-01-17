import re
import time


def lees_inhoud():
    """
    Een functie die het volledige bestand inleest en deze scheid op headers en
    sequenties. Het resultaat zijn twee lijsten.
    """
    bestand = "Mus_musculus.GRCm38.pep.all.fa"
    headers = []
    seqs = []
    try:
        bestand = open(bestand)
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
    except FileNotFoundError:
        print('Het bestand is niet gevonden')

    return headers, seqs


def is_eiwit(seqs, headers):
    for i in range(len(seqs)):
        m = re.search(r"BZXVO", (seqs[i]))
        if m:
            print((headers[i]) + " dit is Geen eiwit")


def eiwitzoeken(headers, seqs):
    cons1 = "MCNSSCMGGMNRR"
    cons2 = 'MCNSSCVGGMNRR'
    dna = 'ATG'
    for i in seqs:
        if dna not in seqs:
            for i in range(len(headers)):
                if cons1 in seqs[i] or cons2 in seqs[i]:
                    print("Header:", headers[i])
                    print(seqs[i])
                else:
                    "het consescus is niet gevonden"
        else:
            print("dit is geen eiwitsequentie")


# OPDRACHT 2

def reg(headers, seqs):
    cons2 = r"MCNSSC[MV]GGMNRR"

    for i in range(len(seqs)):
        m = re.search(cons2, seqs[i])
        if m:
            print(headers[i], '\n', seqs[i])


def regluar(seqs):
    start = time.time()
    for i in range(len(seqs)):
        m = re.search(r'[^ATCGN]', seqs[i])
        if m:
            print("er is een verkeerde nucleotide gevonden")
            print(m.group())
        else:
            print("het is DNA")
    einde = time.time()
    print(einde - start)


def ita(seqs):
    """
    Deze functie zoekt doormiddel van iteratie of het DNA puur is.
    Het houdt ook de tijd bij
    """
    print("------------------------------------------------")
    start2 = time.time()
    verif = seqs.count("A") + seqs.count("T") \
            + seqs.count("G") + seqs.count("C") + seqs.count("N")
    # telt de lengte van het bestand.
    verif2 = len(seqs)

    if verif == verif2:
        print("het is weer dnaa")
    else:
        print("het is geen dna")

    einde2 = time.time()
    print(einde2 - start2)


def main():
    headers, seqs = lees_inhoud()
    is_eiwit(seqs, headers)
    eiwitzoeken(headers, seqs)
    reg(headers, seqs)
    regluar(seqs)
    ita(seqs)


main()
