import math
import bisect
import random

n = 16
random.seed(42)


class Creature:
    def __init__(self, gens: list[int] | None = None):
        if gens is None:
            self.gens = [random.randint(1, n) for i in range(n)]
        else:
            self.gens = gens

        # self._fitness = None
        self.fitness = self.get_fitness()

    # @property
    # def fitness(self) -> int:
    def get_fitness(self) -> int:
        # if self._fitness is not None:
        #     return self._fitness
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                cnt += self.gens[i] != self.gens[j] and abs(i - j) != abs(
                    self.gens[i] - self.gens[j]
                )
        # self._fitness = cnt
        # return self._fitness
        return cnt

    def show(self):
        for i in range(n):
            for j in range(n):
                if j == self.gens[i] - 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

    def mutate(self):
        # r = random.randint(0, n - 1)
        # n_val = random.randint(1, n)
        # self.gens[r] = n_val
        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        self.gens[r1], self.gens[r2] = self.gens[r2], self.gens[r1]

        # * self._fitness = None
        self.fitness = self.get_fitness()

    @staticmethod
    def crossover(x: "Creature", y: "Creature"):
        if random.random() < 0.99:
            r = random.randint(0, n - 1)
            return Creature(x.gens[:r] + y.gens[r:]), Creature(y.gens[:r] + x.gens[r:])
        else:
            return x, y


society_number = 200
maximum_fitness = (n * (n - 1)) // 2
society = [Creature() for i in range(society_number)]

generation_number = 0
society.sort(key=lambda creature: creature.fitness, reverse=True)

while society[0].fitness < maximum_fitness and generation_number < 10_000:
    # * roulette wheel selection
    accumulated_society_fitness = []
    tmp = 0
    for creature in society:
        tmp += creature.fitness
        accumulated_society_fitness.append(tmp)
    total_fitness = tmp
    new_society = []
    while len(new_society) < society_number:
        ri1 = random.randint(0, total_fitness - 1)
        ri2 = random.randint(0, total_fitness - 1)

        par1 = bisect.bisect_left(accumulated_society_fitness, ri1, 0, society_number)
        par2 = bisect.bisect_left(accumulated_society_fitness, ri2, 0, society_number)

        parent1 = society[par1]
        parent2 = society[par2]

        # * make child with crossover
        child1, child2 = Creature.crossover(parent1, parent2)
        new_society.append(child1)
        new_society.append(child2)

    for creature in new_society[1:]:
        if random.random() < 0.1:
            creature.mutate()

    new_society.sort(key=lambda creature: creature.fitness, reverse=True)

    society[society_number // 2 :] = new_society[: society_number // 2]
    society.sort(key=lambda creature: creature.fitness, reverse=True)
    society = society[:society_number]
    generation_number += 1

print()
answer = society[0]
if answer.fitness == maximum_fitness:
    print("WIN")
print(answer.fitness)
print(answer.gens)
answer.show()
