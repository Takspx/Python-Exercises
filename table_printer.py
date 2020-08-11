table_data = [['apples', 'oranges', 'cherries', 'bananas'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):
    col_widths = [0] * len(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if len(data[i][j]) > col_widths[i]:
                col_widths[i] = len(data[i][j])

    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(col_widths[y]), end = ' ')
        print('')

print_table(table_data)
