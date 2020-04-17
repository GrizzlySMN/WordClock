from deap import creator, base, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

import random
toolbox = base.Toolbox()

toolbox.register(
  "random_char",
  random.choice,
  "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ") # Random chars in clock

DIM = 10 #matrix size

toolbox.register(
  "individual",
  tools.initRepeat,
  creator.Individual,
  toolbox.random_char,
  n=DIM * DIM)

def __str__(individual):
    s = ""
    for i in range(len(individual)):
        s += individual[i]
        if i % DIM == DIM-1: s+='#'
    return s

creator.Individual.__str__ = __str__

toolbox.register("population",
                  tools.initRepeat,
                  list,
                  toolbox.individual)

#regex list: Numbers that the clock should display
hours = ("EIS", "ZWÖI", "DRÜ", "VIERI", "FÜFI", "SÄCHSI",
        "SIEBNI", "ACHTI", "NÜNI", "ZÄHNI", "EUFI", "ZWÖUFI",)

restrings = [] # hours to display. Like every 5min? every 10?
for h in hours: restrings.append(h)
for h in hours: restrings.append("FÜÜF.+AB.+"+h)
for h in hours: restrings.append("ZÄÄ.+AB.+"+h)
for h in hours: restrings.append("VIERTU.+AB.+"+h)
for h in hours: restrings.append("ZWÄNZG.+AB.+"+h)
for h in hours: restrings.append("FÜÜF.+VOR.+HAUBI.+"+h)
for h in hours: restrings.append("HAUBI.+"+h)
for h in hours: restrings.append("FÜÜF.+AB.+HAUBI.+"+h)
for h in hours: restrings.append("ZWÄNZG.+VOR.+"+h)
for h in hours: restrings.append("VIERTU.+VOR.+"+h)
for h in hours: restrings.append("ZÄÄ.+VOR.+"+h)
for h in hours: restrings.append("FÜÜF.+VOR.+"+h)

def evaluateInd(individual):
    import re
    s = str(individual)
    scores = [re.compile(r).search(s) != None for r in restrings]
    return (float(sum(scores)),)

#build a keyword list for mutation
keywords = set()
for r in restrings:
    for i in r.split(".+"):
        keywords.add(i)
keywords = list(keywords)

def myMutation(individual):
    kw = random.choice(keywords)
    pos = random.randint(1,len(individual)-len(kw))
    for i, ch in enumerate(kw):
        individual[pos+i]=ch
    return (individual,)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("select", tools.selBest)
toolbox.register("evaluate", evaluateInd)
toolbox.register("mutate", myMutation)

if __name__ == "__main__":
    pop = toolbox.population(n=1000)

    fit = 0.0
    while (fit < len(restrings)):

        algorithms.eaMuPlusLambda (
                pop, toolbox,
                600, 200, #parents, children. 400/100increase those to decrease chance of getting stuck in local minima, but compilation time increases
                .2, .4, #probabilities
                1) #iterations

        top = sorted(pop, key=lambda x:x.fitness.values[0])[-1]
        fit = top.fitness.values[0]
        print(fit)

    print(top)

