# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath("../helpers"))
reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('Cientometria\\resultadoConsultaSJR.txt', header = 0, names = ["ano","sjrJournalId","areaConhecimento","sjrScoreValue","nomeGrupo","nomeAutor","nomePaper"])
#"ano","sjrJournalId","areaConhecimento","sjrScoreValue","nomeGrupo","nomeAutor","nomePaper"

data = data.drop('sjrJournalId',axis=1)
data = data.drop('nomePaper',axis=1)
data = data.drop('nomeAutor',axis=1)

input = data.drop(["nomeGrupo","areaConhecimento"], axis=1)

gr = input.groupby(['ano']).sum()

print input.groupby(['ano']).sum()
print 

x = gr.index.values[:-1] # menos 1 pq a última posição tem o nome da coluna (não é número)
y = gr.values[:-1]

plt.plot(gr.index.values[:-1], gr.values[:-1], color = 'blue', marker = '*', linestyle = 'solid', label = "Score geral")
plt.title("Score geral por ano")
plt.xlabel("Ano")
plt.ylabel("score")
plt.legend(loc=2)
plt.show()


def groupSumSort(data, groupBy, sortBy=False, ascending=True, top=False, func='sum'):
    df = data.groupby(by=groupBy)
    
    if func=='sum':
        df = df.sum().reset_index()
    else:
        if func=='mean':
            df = df.mean().reset_index()

    df = df[:-1]
    if sortBy:
        df = df.sort_values(by=sortBy, ascending=ascending)
    if top:
        df = df.groupby(top[0]).head(top[1])
        df = df.sort_values(by=top[0]).reset_index()
    return df


# imprimingo as 5 areas que mais publicaram
input = data.drop(["nomeGrupo"], axis=1)
df = groupSumSort(input, ['ano', 'areaConhecimento'], ['ano', 'sjrScoreValue'], [True, False])
gp = df.reset_index().head(5).groupby(['areaConhecimento'])
for area in gp.groups:
    plt.plot('ano', 'sjrScoreValue', data=df[df.areaConhecimento == area], label=area)

plt.xlabel('Ano de publicação')
plt.ylabel('Total score')
plt.title('3 areas com maior score')
plt.legend()
plt.show()