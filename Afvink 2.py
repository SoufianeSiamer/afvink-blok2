def open_bestand():
    """

    :return:
    """
    lijst = []
    bestand = open('yeast_genes.csv', 'r')
    bestand.readline()
    for regel in bestand:
        regel = regel.strip()
        regel = regel.split(',')[1]
        lijst.append(regel)
    return lijst


def lijsten(lijst):
    """

    :param lijst:
    :return:
    """
    lijst2 = []
    lijst3 = []
    for i in lijst:
        if i not in lijst2:
            lijst2.append(i)
            lijst3.append(1)
        else:
            index = lijst2.index(i)
            lijst3[index] += 1
    print(lijst2)
    print(lijst3)
    return lijst2, lijst3


def grafiek(lijst2, lijst3):
    """

    :param lijst2:
    :param lijst3:
    :return:
    """
    from numpy import arange
    import matplotlib.pyplot
    objects = lijst2
    y_pos = arange(len(objects))
    performance = lijst3

    matplotlib.pyplot.bar(y_pos, performance, align='center', alpha=0.5)
    matplotlib.pyplot.xticks(y_pos, objects)
    matplotlib.pyplot.ylabel('Hoeveelheid')
    matplotlib.pyplot.title('Hoeveelheid genen met de bijbehorende status')

    matplotlib.pyplot.show()
    return


def main():
    """

    :return:
    """

    lijst = open_bestand()
    lijst2, lijst3 = lijsten(lijst)
    grafiek(lijst2, lijst3)


main()
