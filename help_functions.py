def read_maze(url):
    with open(url) as f:
        lines = [[char for char in line.strip('\n')] for line in f]

    for line in lines:
        print(line)


    print(f'Matrix height is: {len(lines)}')
    print(f'Matrix Width is: {len(lines[0])}')

    if len(lines) == len(lines[0]):
        print('The maze is rectangular')
    else:
        print('The maze is not rectangular')
