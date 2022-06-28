"""
Lesson 3: Reading a maze from text file

1. Understand the 2D list data structure
2. Representing a maze as a 2d list
3. Reading a maze from a text file
4. Check dimensions of the maze and apply logic to it
5. Display a maze from a text file
"""

with open('mazes/wide_maze.txt') as f:
    lines = [[char for char in line.strip('\n')] for line in f]

for line in lines:
    print(line)

if len(lines) == len(lines[0]):
    print('The maze is rectangular')
else:
    print('The maze is not rectangular')


print('=' * 30)


from help_functions import read_maze
url = 'mazes/challenge_maze.txt'
maze = read_maze(url)

print(maze)
