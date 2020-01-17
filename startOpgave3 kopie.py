##########################################################################
# (c) 2013 HAN/Martijn van der Bruggen                                   #
# Dictionaries voor het gebruik bij de afvinkopdrachten van HBI-Cou3a    #
# Update: 24-feb-2013 voorzien van commentaar en bestandsnaam aangepast  #
##########################################################################

code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
        'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
        'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
        'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
        'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
        'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
        'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
        'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
        'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
        'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
        'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
        'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
        'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
        'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
        'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
        'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
        }


def zoeken():
    """
    Deze functie accepteert een sequentie
    zoekt in de dict, en split de sequentie op in codons.

    :return:
    """
    seq2 = input("geef een sequentie op, de sequentie mag geen enters of "
                 "spaties bevatten: ")
    seq3 = []
    for i in range(0, len(seq2), 3):
        codon = (seq2[i:i + 3])
        seq3.append(codon)
    return seq3


def vertaal(seq3):
    """
    Deze functie vertaald de codons naar eiwitsequenties.

    :param seq3:
    :return:
    """
    try:
        seq4 = ""
        for codon in seq3:
            seq4 += (code[codon])
            print(seq4)
    except KeyError:
        print("de sequentie is niet correct")
        

def main():
    seq3 = zoeken()
    vertaal(seq3)


main()
