from random import randint
import pandas as pd
import numpy as np


# это класс предковых особей, их показатели определяются случайны образом
class Ancestor:
    genetic = {'aguti': ['AA', 'Aat', 'Aa', 'atA', 'aA'], 'tan': ['atat', 'ata', 'aat'], 'plain': ['aa']}
    color_scheme_gens = ['A', 'at', 'a']
    pigments = ['yellow', 'dark brown']
    color_store = ['white', 'black', 'red', 'brown', 'gray']
    sex_store = {'male': ['Y', 'X'], 'female': ['X', 'X']}

    def __init__(self, name, sex):
        self.name = name
        self.sex_gen = sex
        self.age = 0
        if self.sex_gen == Ancestor.sex_store['male']:
            self.sex = 'male'
        elif self.sex_gen == Ancestor.sex_store['female']:
            self.sex = 'female'
        self.color = Ancestor.color_store[randint(0, 4)]
        self.color_scheme_gen = [Ancestor.color_scheme_gens[randint(0, 2)], Ancestor.color_scheme_gens[randint(0, 2)]]
        self.color_scheme_gen_sum = f'{self.color_scheme_gen[0] + self.color_scheme_gen[1]}'
        if self.color_scheme_gen_sum in Ancestor.genetic['aguti']:
            self.color_scheme = 'aguti'
        elif self.color_scheme_gen_sum in Ancestor.genetic['tan']:
            self.color_scheme = 'tan'
        elif self.color_scheme_gen_sum in Ancestor.genetic['plain']:
            self.color_scheme = 'plain'

    def __str__(self):
        return f'Имя = {self.name}\n' \
               f'Пол = {self.sex}\n' \
               f'Цвет = {self.color}\n' \
               f'Гены схемы окраса = {self.color_scheme_gen_sum}\n' \
               f'Схема окраса = {self.color_scheme}'

    def reproduction(self):
        return [self.sex, self.sex_gen[randint(0, 1)], self.color_scheme_gens[randint(0, 1)], self.age, self.name]


# это класс потомков, их показатели зависят от родительских показателей
class Descendent:

    def __init__(self, name, male_genes, female_genes):
        while male_genes[0] != 'male':
            male_genes = gene_pool[randint(0, (len(gene_pool) - 1))]
        while female_genes[0] != 'female':
            female_genes = gene_pool[randint(0, (len(gene_pool) - 1))]
        self.name = name
        self.age = 0
        self.sex_gen = [male_genes[1], female_genes[1]]
        if self.sex_gen == Ancestor.sex_store['male']:
            self.sex = 'male'
        elif self.sex_gen == Ancestor.sex_store['female']:
            self.sex = 'female'
        else:
            print(self.sex_gen)

        self.color_scheme_gen_1 = male_genes[2]
        self.color_scheme_gen_2 = female_genes[2]
        self.color_scheme_gens = [male_genes[2], female_genes[2]]
        self.color_scheme_gen_sum = f'{male_genes[2] + female_genes[2]}'
        if self.color_scheme_gen_sum in Ancestor.genetic['aguti']:
            self.color_scheme = 'aguti'
        elif self.color_scheme_gen_sum in Ancestor.genetic['tan']:
            self.color_scheme = 'tan'
        elif self.color_scheme_gen_sum in Ancestor.genetic['plain']:
            self.color_scheme = 'plain'

    def __str__(self):
        return f'Имя = {self.name}\n' \
               f'Пол = {self.sex}\n' \
               f'Гены схемы окраса = {self.color_scheme_gen_sum}\n' \
               f'Схема окраса = {self.color_scheme}'

    def reproduction(self):
        return [self.sex, self.sex_gen[randint(0, 1)], self.color_scheme_gens[randint(0, 1)], self.age, self.name]


class Predator:

    def __init__(self):
        self.fullness = 10
        self.water = 5
        self.age = 0


# генерируем предков
rabbit1 = Ancestor('rabbit1', ['Y', 'X'])
rabbit2 = Ancestor('rabbit2', ['X', 'X'])
rabbit3 = Ancestor('rabbit3', ['Y', 'X'])
rabbit4 = Ancestor('rabbit4', ['X', 'X'])
rabbit5 = Ancestor('rabbit5', ['Y', 'X'])
rabbit6 = Ancestor('rabbit6', ['X', 'X'])

# формируем генофонд популяции
gene_pool = [rabbit1.reproduction(), rabbit2.reproduction(), rabbit3.reproduction(), rabbit4.reproduction(),
             rabbit5.reproduction(), rabbit6.reproduction()]
count_limit = 30  # тут задаём предел особей в популяции
count = 6
rabbits = pd.DataFrame(columns=['Имя', 'Пол', 'Гены с.о', 'Схема окраса'])  # популяция кроликов
for i in range(7, count_limit):
    # создаём новую особь
    rabbit = Descendent(name=f'rabbit{i}', male_genes=gene_pool[randint(0, (len(gene_pool) - 1))],
                        female_genes=gene_pool[randint(0, (len(gene_pool) - 1))])
    # добавляем новую особь в популяцию
    rabbits.loc[f'rabbit{i}'] = [rabbit.name, rabbit.sex, rabbit.color_scheme_gen_sum, rabbit.color_scheme]
    # добавляем гены новой особи в генофонд популяции
    gene_pool.append(rabbit.reproduction())
    # убиваем особи старше 9 лет
    for j in gene_pool:
        j[3] += 1
        if j[3] > 9:
            print(f'Умер от старости {gene_pool[(gene_pool.index(j))][4]}')
            gene_pool.pop(gene_pool.index(j))

print(rabbits)
print(gene_pool)
