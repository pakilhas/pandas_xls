import pandas as pd

      #importar a base de dados

pd.set_option('display.max_columns', None) #mostrar quantidade de colunas('opção',quantidade)



faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum() #nova tebela filtrada, agrupada e somada

print(faturamento)

quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()

print(quantidade)

print('-' * 50)#mostrar como texto - como divizao

ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame() #oprações entre tabelas //.to_frame faz a coluna virar tabela
print(ticket_medio)