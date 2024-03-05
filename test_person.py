# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: Teste da classe Person
"""
# Importa a classe 'Person' que se encontra na pasta 'classes'
from classes.Person import Person

# Lê os dados da classe Person
Person.read("data/")

# Percorre os objetos do primeiro ao último
print("\nprimeiro->último:")
p1 = Person.first()
while p1 != None:
    print(p1)
    p1 = Person.nextrec()

# Percorre os objetos do último ao primeiro
print("\núltimo->primeiro:")
p1 = Person.last()
while p1 != None:
    print(p1)
    p1 = Person.previous()

# Cria um novo objeto Pessoa
print("\nPessoa com o código '555' criada:")
p1 = Person('555', 'Joana Fonseca', '1995-02-12', 3000)
print(p1)

# Percorre os objetos usando as variáveis de classe 'obj' e 'lst'
print("\nVariáveis de classe 'obj' e 'lst'")
for codigo in Person.lst:
    p1 = Person.obj[codigo]
    print(p1)

# Acede ao objeto cujo código é 555
print("\nPessoa com o código '555':")
p1 = Person.obj['555']
print(p1)

# Apaga a o objeto pessoa com o código '555'
print("\nPessoa com o código 555 removida")
Person.remove('555')

# Percorre os objetos usando a variável de classe 'obj'
print("\nVariável de classe 'obj':")
for p1 in Person.obj.values():
    print(p1)

# Escreve os dados da classe Person
Person.write("data/")
