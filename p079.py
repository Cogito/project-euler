from collections import defaultdict

if __name__ == '__main__':
    successors = defaultdict(set)
    with open("p079_keylog.txt") as attempts:
        for attempt in attempts:
            for c in attempt[1:2]:
                successors[attempt[0]].add(c)
            successors[attempt[1]].add(attempt[2])
            successors[attempt[2]]
    # print(sorted(successors.items(), key=lambda x: len(x[1])), successors)
    output = []
    while len(successors) > 0:
        item, _ = sorted(successors.items(), key=lambda x: len(x[1]))[0]
        output.append(item)
        del successors[item]
        for _, others in successors.items():
            if others and item in others:
                others.remove(item)
    print("".join(reversed(output)))
