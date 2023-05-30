import math
import random

n = 8


class Creature:
    def __init__(self, gens: list[int] | None = None):
        if gens is None:
            self.gens = [random.randint(1, n) for i in range(n)]
        else:
            self.gens = gens
        # print(self.gens)
        self._fitness = 0

    @property
    def fitness(self) -> float:
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                cnt += self.gens[i] != self.gens[j] and abs(i - j) != abs(
                    self.gens[i] - self.gens[j]
                )
        return cnt

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
society_first_number = 100
maximum_fitness = (n * (n - 1)) // 2
society = [Creature() for i in range(society_first_number)]

generation_number = 0

society.sort(key=lambda creature: creature.fitness, reverse=True)

for i in range(10):
    print(society[i].fitness)

society[0].show()
while society[0].fitness == maximum_fitness or generation_number < 100:
    # todo: parent selection with child making
    society.sort(key=lambda creature: creature.fitness, reverse=True)
    generation_number += 1
