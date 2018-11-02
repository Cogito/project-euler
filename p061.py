from euler_helpers import triangle_numbers, square_numbers, pentagonal_numbers, hexagonal_numbers, heptagonal_numbers, octagonal_numbers
import networkx
import numpy


def p061():
    triangles = list(triangle_numbers(1000, 9999))
    squares = list(square_numbers(1000, 9999))
    pentagonals = list(pentagonal_numbers(1000, 9999))
    hexagonals = list(hexagonal_numbers(1000, 9999))
    heptagonals = list(heptagonal_numbers(1000, 9999))
    octagonals = list(octagonal_numbers(1000, 9999))

    G = networkx.DiGraph()

    G.add_edges_from([(a, b) for a in triangles for b in squares if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in triangles for b in pentagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in triangles for b in hexagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in triangles for b in heptagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in triangles for b in octagonals if a % 100 == b // 100])

    G.add_edges_from([(a, b) for a in squares for b in pentagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in squares for b in hexagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in squares for b in heptagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in squares for b in octagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in squares for b in triangles if a % 100 == b // 100])

    G.add_edges_from([(a, b) for a in pentagonals for b in hexagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in pentagonals for b in heptagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in pentagonals for b in octagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in pentagonals for b in triangles if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in pentagonals for b in squares if a % 100 == b // 100])

    G.add_edges_from([(a, b) for a in hexagonals for b in heptagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in hexagonals for b in octagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in hexagonals for b in triangles if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in hexagonals for b in squares if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in hexagonals for b in pentagonals if a % 100 == b // 100])

    G.add_edges_from([(a, b) for a in heptagonals for b in octagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in heptagonals for b in triangles if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in heptagonals for b in squares if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in heptagonals for b in pentagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in heptagonals for b in hexagonals if a % 100 == b // 100])

    G.add_edges_from([(a, b) for a in octagonals for b in triangles if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in octagonals for b in squares if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in octagonals for b in pentagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in octagonals for b in hexagonals if a % 100 == b // 100])
    G.add_edges_from([(a, b) for a in octagonals for b in heptagonals if a % 100 == b // 100])

    types = [
        triangles,
        squares,
        pentagonals,
        hexagonals,
        heptagonals,
        octagonals
    ]
    for start in (node for node in triangles if node in G.nodes):
        for step1 in G.successors(start):
            for step2 in G.successors(step1):
                for step3 in G.successors(step2):
                    for step4 in G.successors(step3):
                        for step5 in G.successors(step4):
                            nodes = (start, step1, step2, step3, step4, step5)
                            # Create a matrix that encodes which numbers are each number type. If this matrix has rank 6 then there are different numbers for each type.
                            A = numpy.matrix([[1 if node in number_type else 0 for number_type in types] for node in nodes], dtype='int')
                            if start in G.successors(step5) and numpy.linalg.matrix_rank(A) == 6:
                                print(sum(nodes), nodes)


if __name__ == '__main__':
    p061()
