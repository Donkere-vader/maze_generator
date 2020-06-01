from main import MazeGenerator
import sys

file_name = None
if len(sys.argv) > 1:
    file_name = sys.argv[1]

if not file_name:
    print("Please provide the program with a file name to save the script to.")
    exit()

if __name__ == "__main__":
    maze_generator = MazeGenerator(file_name)
    maze_generator.generate()