
dados_vendas = {
    'Janeiro':12000,
    'Fevereiro':15000,
    'Março':13000,
    'Abril':14000,
    'Maio':16000,
    'Junho':17000
}


total_anual = 0 
mes_valor_maximo = max(dados_vendas, key=dados_vendas.get)
mes_valor_minimo = min(dados_vendas, key=dados_vendas.get)

meses,valores = [],[]

for chave, valor in dados_vendas.items():
    meses.append(chave)
    valores.append(valor)
    total_anual += valor

    
print(total_anual)
print(mes_valor_maximo)
print(mes_valor_minimo)
print(meses)
print(valores)

