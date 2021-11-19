from matplotlib import pyplot as plt
from Anses.Anses import leerDataEspecificaEventoparaMapa, leerDataEspecificaEvento


def mapa():
    plt.style.use('seaborn')
    x=[]
    leerDataEspecificaEventoparaMapa(x,6)
    y=[]
    leerDataEspecificaEventoparaMapa(y, 7)
    nombres=[]
    leerDataEspecificaEvento(nombres,0)
    for i, label in enumerate(nombres):
        plt.annotate(label, (x[i], y[i]))
    colores = [0,1]
    plt.scatter(x, y, s = 100, c=colores,cmap = 'Blues', marker='o', edgecolor='black', linewidths=2, alpha=0.55)
    plt.title('EVENT-IT')
    plt.show()
