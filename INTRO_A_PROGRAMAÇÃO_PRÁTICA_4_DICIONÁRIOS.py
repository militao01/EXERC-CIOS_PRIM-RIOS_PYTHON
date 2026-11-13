# %%
#========================================
# EXERCÍCIO 1
# Crie um dicionário chamado aluno contendo as seguintes informações:
# Aluno - Curso - Idade
# Depois imprima cada valor
#========================================
aluno = {"Nome":"João","Curso":"BIA","Idade": 19}
for i in aluno:
    print(aluno[i])

# %%
#========================================
# EXERCÍCIO 2
# Dado o dicionário:
pessoa = {"Nome": "João","Hobbies": ["Futebol", "Xadrez", "Leitura"]}
# Imprima o nome, imprima a lista de hobbies, imprima apenas o segundo hobby
#========================================
print(pessoa["Nome"])
print(pessoa["Hobbies"])
print(pessoa["Hobbies"][1])

# %%
#=========================================
#EXERCÍCIO 3
# Usando o dicionário abaixo:
carro = {"Marca": "Toyota","Modelo": "Corolla","Ano": 2018}
# Adicione ao dicionário:
#A chave cor com o valor prata
#A chave dono com o valor Carlos
#=========================================
carro["Cor"] = "Prata"
carro["Dono"] = "Carlos"
print(carro)
# %%
#===========================================
# EXERCÍCIO 4 
# Ainda no dicionário anterior
# Altere o valor da chave "Ano" para 2020
# Altere o valor da chave "Cor" para "Preto"
#===========================================
carro["Cor"] = "Preto"
carro["Ano"] = 2020
print(carro)
# %%
#===========================================
# EXERCÍCIO 5 
#Ainda no dicionário carro
#Remova a chave dono
#===========================================
carro.pop("Dono")
print(carro)
# %%
#===========================================
# EXERCÍCIO 6
#Dado o dicionário:
produto = {"Nome": "Notebook","Preço": 3500, "Estoque": 12}
#Imprima todas as chaves usando um for
#Imprima todos os valores usando um for 
#imprima todos os pares chave e valor usando items()
#===========================================
print("\nTodas as chaves:")
for i in produto:
    print(i)
print("\nTodos os Valores:")
for i in produto:
    print(produto[i])

print(produto.items())

