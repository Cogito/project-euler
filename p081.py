def find_minimal_sum(matrix):
    size = len(matrix)
    visited = [(0, 0)]
    visited.extend((n, size) for n in range(size))
    visited.extend((size, n) for n in range(size))
    paths = {(0, 0): matrix[0][0]}

    while True:
        smallest_path = min(paths, key=paths.get)
        x, y = smallest_path
        candidates = []
        if (x + 1, y) not in visited:
            candidates.append((x + 1, y))
        if (x, y + 1) not in visited:
            candidates.append((x, y + 1))
        if len(candidates) == 0:
            del paths[smallest_path]
            continue
        new_path = min(candidates, key=lambda cell: paths[smallest_path] + matrix[cell[0]][cell[1]])
        paths[new_path] = paths[smallest_path] + matrix[new_path[0]][new_path[1]]
        visited.append(new_path)
        if new_path == (size - 1, size - 1):
            return paths[new_path]


def matrix_from_file(path):
    with open(path) as matrix_file:
        return [[int(col) for col in row.split(',')] for row in matrix_file]


def test_po81():
    assert find_minimal_sum(matrix_from_file('p081_test_matrix.txt'))


def p081():
    return find_minimal_sum(matrix_from_file('p081_matrix.txt'))


if __name__ == '__main__':
    print(p081())
