import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.wumpus_pos = self.generate_random_position()
        self.gold_pos = self.generate_random_position()
        self.pit_pos = [self.generate_random_position() for _ in range(size)]

    def generate_random_position(self):
        return (random.randint(0, self.size-1), random.randint(0, self.size-1))

    def print_grid(self):
        for row in self.grid:
            print('|'.join(row))

    def update_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_pos:
                    self.grid[i][j] = 'A'
                elif (i, j) == self.wumpus_pos:
                    self.grid[i][j] = 'W'
                elif (i, j) == self.gold_pos:
                    self.grid[i][j] = 'G'
                elif (i, j) in self.pit_pos:
                    self.grid[i][j] = 'P'
                else:
                    self.grid[i][j] = ' '

    def move_agent(self, direction):
        x, y = self.agent_pos
        if direction == 'up' and x > 0:
            self.agent_pos = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.agent_pos = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_pos = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.agent_pos = (x, y + 1)

game = WumpusWorld()
game.update_grid()
game.print_grid()
