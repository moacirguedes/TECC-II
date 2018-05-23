# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath("../helpers"))
reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('Cientometria\\resultadoConsultaQualis.txt', names = ["ano","qualisJournalId","areaConhecimentoId","areaConhecimento","qualisScoreValue","grupoName","paperName"])
#"ano","qualisJournalId","areaConhecimentoId","areaConhecimento","qualisScoreValue","grupoName","paperName"
#"2005","0567-7572","12","ENGENHARIAS II","B3","DEAGRO/G","Evaluation of different substrates on african violet (Saintpaulia ionantha Wendl.) growth."

data = data.drop('qualisJournalId',axis=1)
data = data.drop('paperName',axis=1)
#"ano" , "areaConhecimentoId","areaConhecimento" ,"qualisScoreValue", "grupoName"
#"2005", "12"                ,"ENGENHARIAS II"   ,"B3"              , "DEAGRO/G"

data.qualisScoreValue[data.qualisScoreValue == 'A1'] = 1 
data.qualisScoreValue[data.qualisScoreValue == 'A2'] = 0.85 
data.qualisScoreValue[data.qualisScoreValue == 'B1'] = 0.70 
data.qualisScoreValue[data.qualisScoreValue == 'B2'] = 0.55 
data.qualisScoreValue[data.qualisScoreValue == 'B3'] = 0.40 
data.qualisScoreValue[data.qualisScoreValue == 'B4'] = 0.25 
data.qualisScoreValue[data.qualisScoreValue == 'B5'] = 0.10 
data.qualisScoreValue[data.qualisScoreValue == 'C'] = 0.05 

# imprimindo o score geral por ano
input = data.drop(["grupoName", "areaConhecimentoId","areaConhecimento"], axis=1)

gr = input.groupby(['ano']).sum()
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
input = data.drop(["grupoName","areaConhecimentoId"], axis=1)
df = groupSumSort(input, ['ano', 'areaConhecimento'], ['ano', 'qualisScoreValue'], [True, False])
gp = df.reset_index().head(5).groupby(['areaConhecimento'])
for area in gp.groups:
    plt.plot('ano', 'qualisScoreValue', data=df[df.areaConhecimento == area], label=area)

plt.xlabel('Ano de publicação')
plt.ylabel('Total score')
plt.title('3 areas com maior score')
plt.legend()
plt.show()

# input = data.drop(["ano","areaConhecimentoId","areaConhecimento"], axis=1)
# gr = input.groupby(['grupoName']).sum().sort_values('qualisScoreValue', ascending=False)

# x = gr.index.values[:-1] # menos 1 pq a última posição tem o nome da coluna (não é número)
# y = gr.values[:-1]

# # plt.hist()
# #plt.title("Score geral por ano")
# # plt.xlabel("Ano")
# # plt.ylabel("score")
# plt.legend(loc=2)
# plt.show()