from config import MAZE_HEIGHT, MAZE_WIDTH
import random
import os

class MazeTiles:
    def __init__(self):
        self.air = " "
        self.wall = "#"
        self.start = "S"
        self.end = "E"

class Directions:
    def __init__(self):
        self.up = "up"
        self.down = "down"
        self.right = "right"
        self.left = "left"

maze_tiles = MazeTiles()
directions = Directions()

class MazeGenerator:
    def __init__(self, file_name):
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        self.output_file = file_name

        os.system("cls")
        print("==> MAZE GENERATOR <==\n")
        print(f"Output will be saved to: {self.output_file}")

        print("> Setting up...")
        self.setup()

    def setup(self):
        self.maze = [[maze_tiles.wall for i in range(MAZE_WIDTH)] for i in range(MAZE_HEIGHT)]
        print("> Generating...")
        self.generate()

        # when done save
        self.save()

    def generate(self):
        start_x = random.randint(0, len(self.maze[0]) - 1)
        start_y = 0
        self.generate_pos(start_x, start_y)

    def generate_pos(self, x: int, y: int):
        if y == 0:
            self.generate_pos(x, y + 1)
        


    def random_direction(self) -> str:
        return random.choice([directions.up, directions.down, directions.right, directions.left])

    def save(self):
        print("\n\n==> GENERATING DONE <==\n")
        print(f"> Saving to {self.output_file}...")
        f = open(self.output_file, "w")
        for y in self.maze:
            for x in y:
                f.write(x)
            f.write("\n")

        print("> Saved")

    def get_direction(self, x: int, y: int, direction: str, len=1) -> list:
        _x = 0
        _y = 0
        if direction == directions.up:
            _y = -1
        elif direction == directions.down:
            _y = 1
        elif direction == directions.right:
            _x = 1
        elif direction == directions.left:
            _x = -1

        tiles = []

        for i in range(len(len)):
            if y + _y * i > 0 and y + _y * i < len(self.maze) and x + _x * i > 0 and x + _x * i < len(self.maze[y]):
                tiles.append(
                    self.maze[y + _y * i][x + _x * i]
                )
            else:
                return tiles

        return None