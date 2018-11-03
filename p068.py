import itertools


def is_magic(ring):
    groups = ring_groups(ring)
    return all(sum(group) == sum(groups[0]) for group in groups)


def ring_groups(ring):
    length = len(ring) // 2
    outer = ring[:length]
    inner = ring[length:]
    return [[outer[i], inner[i], inner[(i + 1) % length]] for i in range(length)]


def all_magic_ngon_rings(n):
    yield from (combination for combination in itertools.permutations(range(1, n + 1)) if combination[0] == min(combination[:len(combination) // 2]) and is_magic(combination))


def ring_group_concat(ring):
    return "".join(str(n) for group in ring_groups(ring) for n in group)


def test_p068():
    assert is_magic([4, 6, 5, 3, 2, 1])


def p066():
    return max(ring_group_concat(magic_ring) for magic_ring in all_magic_ngon_rings(10))


if __name__ == '__main__':
    print(p066())
