# Naam: Soufiane Si Amer


def main():
    """
    Deze main open het bestand en zoek naar een woord dat wordt opgegeven.
    daarna roept hij alle functies aan .

    :return:
    """
    try:
        bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
        headers, seqs = lees_inhoud(bestand)
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA.")
    except FileNotFoundError:
        print('het bestand isx niet gevonden')
    except TypeError:
        print('verkeerde invoer')
    except PermissionError:
        print('je hebt  geen rechten')


def lees_inhoud(bestands_naam):
    """
    Opent het bestand en leest het in
    """
    try:
        bestand = open(bestands_naam)
        headers = []
        seqs = []
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
        return headers, seqs
    except FileNotFoundError:
        print('Bestand niet gevonden')


def is_dna(seq):
    """
    deze functie bepaalt of het dna is of niet
    :param seq:
    :return:
    """

    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    """
    deze functie bepaaltof de restrictieenzymen kunnen knippen.
    :param alpaca_seq:
    :return:
    """
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except FileNotFoundError:
        print('bestand niet gevonden (enzymen.txt)')
    except ValueError:
        print('Verkeerde invoer voor enzym')


main()
