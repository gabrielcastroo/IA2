# Algoritmo Genético para Escolha de Curso Superior

Este é um algoritmo genético simples para escolher o melhor curso superior com base no desempenho escolar em diferentes disciplinas. O algoritmo gera uma população de indivíduos aleatórios, avalia a aptidão de cada indivíduo com base em seus resultados nas disciplinas e nos cursos desejados, seleciona os indivíduos mais aptos para reprodução, realiza cruzamento e mutação aleatória e gera uma nova população. Este processo é repetido até que um indivíduo suficientemente apto seja encontrado.

## Como Usar

Para usar este algoritmo com suas próprias disciplinas e cursos, siga as seguintes etapas:

1. Abra o arquivo `genetic_algorithm.py` em seu editor de código Python.

2. Edite a lista `variables` para incluir as disciplinas que deseja avaliar.

3. Adicione os cursos que deseja avaliar na função `fitness()`.

4. Execute o arquivo `genetic_algorithm.py`.

## Funções

### `generate_individual()`

Gera um indivíduo aleatório com notas aleatórias em cada disciplina.

### `generate_population(size)`

Gera uma população de indivíduos aleatórios de tamanho `size`.

### `fitness(individual)`

Avalia a aptidão de um indivíduo com base em suas notas nas disciplinas e nos cursos desejados.

### `selection(population)`

Seleciona os indivíduos mais aptos da população para reprodução.

### `crossover(parent1, parent2)`

Realiza o cruzamento de dois indivíduos, gerando um novo indivíduo com características dos pais.

### `mutation(individual)`

Realiza uma mutação aleatória em um indivíduo.

### `get_best_individual(population)`

Retorna o indivíduo mais apto da população.

### `main()`

Executa o algoritmo genético. Gera uma população aleatória, avalia a aptidão de cada indivíduo, seleciona os indivíduos mais aptos para reprodução, realiza cruzamento e mutação aleatória, e gera uma nova população. Repete este processo até que um indivíduo suficientemente apto seja encontrado. Imprime o resultado final.

## Parâmetros

O algoritmo usa as seguintes constantes, que podem ser ajustadas para controlar o comportamento do algoritmo:

- `POP_SIZE`: o tamanho da população de indivíduos.
- `NUM_GENERATIONS`: o número máximo de gerações que serão geradas até que um indivíduo suficientemente apto seja encontrado.
- `K`: o número de indivíduos mais aptos que serão selecionados para reprodução.
- `MUTATION_RATE`: a taxa de mutação usada na reprodução.

## Exemplo

Para usar este algoritmo com as disciplinas "Matemática", "Física", "Biologia", "Química", "Língua Portuguesa", "Língua Inglesa", "Artes", "Filosofia", "Redação", "História" e "Geografia", e os cursos "Engenharia", "Direito", "Medicina", "TI", "Artes", "Línguas" e "Psicologia", siga as seguintes etapas:

# Defina as disciplinas
variables = ["Matemática", "Física", "Biologia", "Química", "Língua Portuguesa", "Língua Inglesa", "Artes", "Filosofia", "Redação", "História", "Geografia"]

```python
# Defina a função de aptidão
def fitness(individual):
    # Defina os cursos desejados
    desired_courses = ["Engenharia", "Direito", "Medicina", "TI", "Artes", "Línguas", "Psicologia"]
    
    # Calcule a nota total do indivíduo em cada curso desejado
    course_scores = {course: 0 for course in desired_courses}
    for course in desired_courses:
        for i, score in enumerate(individual):
            if variables[i] in course:
                course_scores[course] += score
    
    # Calcule a nota total do indivíduo
    total_score = sum(individual)
    
    # Aplique bônus ou penalidades para cada curso desejado
    for course in desired_courses:
        # Engenharia
        if course == "Engenharia":
            # Nota mínima: 40 pontos em Matemática e Física
            if course_scores[course] < 40:
                total_score -= 10
        
        # Direito
        elif course == "Direito":
            # Nota mínima: 30 pontos em História e Português
            if course_scores[course] < 30:
                total_score -= 10
        
        # Medicina
        elif course == "Medicina":
            # Nota mínima: 40 pontos em Biologia e Química
            if course_scores[course] < 40:
                total_score -= 10
        
        # TI
        elif course == "TI":
            # Nota mínima: 30 pontos em Matemática e Inglês
            if course_scores[course] < 30:
                total_score -= 10
        
        # Artes
        elif course == "Artes":
            # Nota mínima: 40 pontos em Artes
            if course_scores[course] < 40:
                total_score -= 10
        
        # Línguas
        elif course == "Línguas":
            # Nota mínima: 30 pontos em Inglês e Português
            if course_scores[course] < 30:
                total_score -= 10
        
        # Psicologia
        elif course == "Psicologia":
            # Nota mínima: 30 pontos em Filosofia e Redação
            if course_scores[course] < 30:
                total_score -= 10
    
    return total_score

```