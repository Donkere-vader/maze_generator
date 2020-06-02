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
        start_x = random.randint(1, len(self.maze[0]) - 1)
        start_y = 0
        self.maze[start_y][start_x] == maze_tiles.start
        self.generate_pos(start_x, start_y)

    def generate_pos(self, x: int, y: int):
        if self.maze[y][x] == maze_tiles.wall:
            self.maze[y][x] = maze_tiles.air
        print(f"> Checking: ({x}, {y})")

        self.print_maze(highlight=(x, y))

        directions_list = [directions.up, directions.down, directions.right, directions.left]

        for random_direction in random.sample([directions.up, directions.down, directions.right, directions.left], len(directions_list)):
            cords_x, cords_y = self.generate_cords(random_direction, x, y)
            if self.check_pos(cords_x, cords_y, margin=1):
                if self.get_direction(x, y, random_direction, len=3).count(maze_tiles.wall) >= 2 and self.get_direction(x -1, y, random_direction, len=3).count(maze_tiles.wall) >= 2 and self.get_direction(x, y + 1, random_direction, len=3).count(maze_tiles.wall) >= 2:
                    self.generate_pos(cords_x, cords_y)
            
    def check_pos(self, x: int, y: int, margin=0) -> bool:
        if y >= 0 + margin and y < len(self.maze) - margin and x >= 0 + margin and x < len(self.maze[y]) - margin:
            return True
        return False

    def print_maze(self, highlight: tuple= ()):
        os.system('cls')
        print("<--- MAZE --->")
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if highlight == (j, i):
                    print(f"\u001b[31m_\u001b[0m", end="")
                else:
                    print(self.maze[i][j], end="")
            print()

    def generate_cords(self, direction, x, y) -> int:
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

        return x + _x, y + _y

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

        for i in range(len):
            if self.check_pos(x + _x * i, y + _y * i):
                tiles.append(
                    self.maze[y + _y * i][x + _x * i]
                )
            else:
                break

        return tiles