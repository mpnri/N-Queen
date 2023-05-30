import math
import bisect
import random

n = 8


class Creature:
    def __init__(self, gens: list[int] | None = None):
        if gens is None:
            self.gens = [random.randint(1, n) for i in range(n)]
        else:
            self.gens = gens
        # print(self.gens)
        self._fitness = None

    @property
    def fitness(self) -> int:
        if self._fitness is not None:
            return self._fitness
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                cnt += self.gens[i] != self.gens[j] and abs(i - j) != abs(
                    self.gens[i] - self.gens[j]
                )
        self._fitness = cnt
        return self._fitness

    def show(self):
        for i in range(n):
            for j in range(n):
                if j == self.gens[i] - 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()


t = Creature()
print(t.fitness)
t.show()
society_number = 10
maximum_fitness = (n * (n - 1)) // 2
society = [Creature() for i in range(society_number)]

generation_number = 0

society.sort(key=lambda creature: creature.fitness, reverse=True)

for i in range(10):
    print(society[i].fitness)

society[0].show()
while society[0].fitness < maximum_fitness and generation_number < 100:
    # todo: parent selection with child making
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

        par1 = bisect.bisect_left(
            accumulated_society_fitness, ri1, 0, len(accumulated_society_fitness)
        )
        par2 = bisect.bisect_left(
            accumulated_society_fitness, ri1, 0, len(accumulated_society_fitness)
        )
        
        parent1 = society[par1]
        parent2 = society[par2]
        #todo: make child
        break

    society.sort(key=lambda creature: creature.fitness, reverse=True)
    generation_number += 1
