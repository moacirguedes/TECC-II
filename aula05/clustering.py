"""
"""

import numpy as np
import matplotlib.pyplot as plt
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
print input.groupby(['ano']).sum()
print 

# imprimindo o score geral por grupo
input = data.drop(["ano","areaConhecimentoId","areaConhecimento"], axis=1)
print input.groupby(['grupoName']).sum().sort_values('qualisScoreValue', ascending=False)
print

# imprimindo o score geral por grupo
input = data.drop(["areaConhecimentoId","areaConhecimento"], axis=1)
print input.groupby(["ano", 'grupoName']).sum().sort_values('qualisScoreValue', ascending=False)
print


# imprimindo o score geral por area
input = data.drop(["ano","grupoName","areaConhecimentoId"], axis=1)
print input.groupby(['areaConhecimento']).sum().sort_values('qualisScoreValue', ascending=False)
print

# plt.hist([y1], label = ["1"])
# plt.legend(loc=2)
# plt.show()