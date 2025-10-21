import numpy as np
import random
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

from visualize_packing import visualize_disk_usage

FILE_TOTAL = 300
FILE_LOW_SIZE = 1  # 1 gb
FILE_UP_SIZE = 100  # 100 gb

DISK_TOTAL = 25
DISK_CAPACITY = 2 * 1024  # 2 tb

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

files = [random.randint(FILE_LOW_SIZE, FILE_UP_SIZE + 1) for _ in range(FILE_TOTAL)]

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("randomDisk", random.randint, 0, DISK_TOTAL - 1)
toolbox.register(
    "individualCreator",
    tools.initRepeat,
    creator.Individual,
    toolbox.randomDisk,
    n=FILE_TOTAL,
)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


def fitness(individual):

    disk_usage = {}
    for file_idx, disk in enumerate(individual):
        disk_usage[disk] = disk_usage.get(disk, 0) + files[file_idx]

    max_usage = max(disk_usage.values()) if disk_usage else 0
    return (max_usage,)


toolbox.register("evaluate", fitness)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=DISK_TOTAL - 1, indpb=0.2)


def run_ga(generations=50, population_size=50, cx_prob=0.7, mut_prob=0.2):
    pop = toolbox.populationCreator(n=population_size)
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)

    pop, log = algorithms.eaSimple(
        pop,
        toolbox,
        cxpb=cx_prob,
        mutpb=mut_prob,
        ngen=generations,
        stats=stats,
        halloffame=hof,
        verbose=True,
    )
    return hof[0], hof[0].fitness.values[0], log


best_ind, best_fit, log = run_ga(generations=100, population_size=200)
print("Лучшее распределение:", best_ind)
print("Максимальная загрузка диска (ГБ):", round(best_fit, 3))

minFitnessValues, meanFitnessValues = log.select("min", "avg")

plt.figure(figsize=(10, 6))
plt.plot(
    minFitnessValues,
    color="red",
    linewidth=2,
    marker="o",
    markersize=5,
    label="Минимальная приспособленность",
)
plt.plot(
    meanFitnessValues,
    color="green",
    linewidth=2,
    marker="x",
    markersize=5,
    label="Средняя приспособленность",
)

plt.xlabel("Поколение", fontsize=12)
plt.ylabel("Значение функции приспособленности", fontsize=12)
plt.title("Эволюция приспособленности генетического алгоритма", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

visualize_disk_usage(best_ind, files, DISK_CAPACITY)
