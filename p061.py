from euler_helpers import triangle_numbers, square_numbers, pentagonal_numbers, hexagonal_numbers, heptagonal_numbers, octagonal_numbers
import networkx

triangles = list(triangle_numbers(1000, 9999))
squares = list(square_numbers(1000, 9999))
pentagonals = list(pentagonal_numbers(1000, 9999))
hexagonals = list(hexagonal_numbers(1000, 9999))
heptagonals = list(heptagonal_numbers(1000, 9999))
octagonals = list(octagonal_numbers(1000, 9999))

# print(list(octagonals))
G = networkx.DiGraph()

# triangles_from = [(l % 100) for l in triangles]
# triangles_to = [(l // 100) for l in triangles]
# squares_from = [(l % 100) for l in squares]
# squares_to = [(l // 100) for l in squares]
#
# print([l for l in triangles_from if l in squares_to])
#
# print([t for t in triangles if t in hexagonals])

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

print(list(networkx.simple_cycles(G)))
