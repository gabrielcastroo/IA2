import random
import json

# Definir a população inicial com 5000 indivíduos
POP_SIZE = 5000
population = []

# Gerar indivíduos aleatórios com notas em cada disciplina e um ID
for i in range(POP_SIZE):
    individual = {}
    individual['id'] = i
    individual['matematica'] = round(random.uniform(0, 10),ndigits=2)
    individual['fisica'] = round(random.uniform(0, 10),ndigits=2)
    individual['biologia'] = round(random.uniform(0, 10),ndigits=2)
    individual['quimica'] = round(random.uniform(0, 10),ndigits=2)
    individual['portugues'] = round(random.uniform(0, 10),ndigits=2)
    individual['ingles'] = round(random.uniform(0, 10),ndigits=2)
    individual['artes'] = round(random.uniform(0, 10),ndigits=2)
    individual['filosofia'] = round(random.uniform(0, 10),ndigits=2)
    individual['redacao'] = round(random.uniform(0, 10),ndigits=2)
    individual['historia'] = round(random.uniform(0, 10),ndigits=2)
    individual['geografia'] = round(random.uniform(0, 10),ndigits=2)
    population.append(individual)

# Definir as variáveis genéticas e seus pesos para a função de aptidão
variables = ['matematica', 'fisica', 'biologia', 'quimica', 'portugues', 'ingles', 'artes', 'filosofia', 'redacao', 'historia', 'geografia']
weights = [0.15, 0.1, 0.1, 0.1, 0.15, 0.1, 0.05, 0.05, 0.1, 0.05, 0.05]

# Definir a função de aptidão
def fitness(individual, course):
    total = 0
    for i in range(len(variables)):
        total += individual[variables[i]] * weights[i]
    if course == 'engenharia':
        return total >= 7.0 and individual['matematica'] >= 8.0 and individual['fisica'] >= 7.0
    elif course == 'medicina':
        return total >= 7.5 and individual['quimica'] >= 8.0 and individual['biologia'] >= 8.0
    elif course == 'direito':
        return total >= 7.0 and individual['portugues'] >= 8.0 and individual['historia'] >= 7.0
    elif course == 'ti':
        return total >= 7.0 and individual['matematica'] >= 7.0 and individual['quimica'] >= 7.0 and individual['ingles'] >= 7.0
    elif course == 'artes':
        return total >= 7.0 and individual['artes'] >= 8.0
    elif course == 'linguas':
        return total >= 7.0 and individual['portugues'] >= 8.0 and individual['ingles'] >= 8.0
    elif course == 'psicologia':
        return total >= 7.0 and individual['portugues'] >= 8.0 and individual['filosofia'] >= 7.0
    else:
        return False

# Selecionar os indivíduos mais aptos para reprodução
def selection(population, course, k=100):
   
    # Ordenar a população pela aptidão decrescente
    population.sort(key=lambda x: fitness(x, course), reverse=True)
    # Selecionar os k indivíduos mais aptos
    return population[:k]

# Realizar a reprodução por cruzamento
def crossover(parents, num_offspring):
    offspring = []
    while len(offspring) < num_offspring:
        # Selecionar dois pais aleatórios
        p1, p2 = random.sample(parents, 2)
        # Gerar um ponto de corte aleatório
        crossover_point = random.randint(1, len(variables)-1)
        # Gerar um filho a partir da combinação dos genes dos pais
        child = {}
        for i in range(len(variables)):
            if i < crossover_point:
                child[variables[i]] = p1[variables[i]]
            else:
                child[variables[i]] = p2[variables[i]]
        offspring.append(child)
    return offspring

# Realizar a mutação aleatória
def mutation(individual, rate=0.01):
    for i in range(len(variables)):
        if random.random() < rate:
            individual[variables[i]] = random.uniform(0, 10)
    return individual

# Definir o curso para o qual queremos selecionar os candidatos
course = 'direito'

# Selecionar os indivíduos mais aptos para reprodução
parents = selection(population, course, k=100)

# Realizar a reprodução por cruzamento
offspring = crossover(parents, num_offspring=POP_SIZE)

# Realizar a mutação aleatória em uma porcentagem dos indivíduos
for i in range(len(offspring)):
    offspring[i] = mutation(offspring[i])

# Combinar os indivíduos antigos e novos em uma nova população
population = population + offspring

# Avaliar a aptidão de cada indivíduo na nova população
for i in range(len(population)):
    individual = population[i]
    fitness_score = fitness(individual, course)
    population[i]['fitness'] = fitness_score

# Ordenar a população pela aptidão decrescente
population.sort(key=lambda x: x['fitness'], reverse=True)

# Selecionar o indivíduo mais apto
best_individual = population[0]

print(f"Melhor indivíduo da população para o curso de {course.upper()} \n{json.dumps(best_individual, ensure_ascii=False, indent=4)}")

