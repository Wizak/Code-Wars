def is_merge(s, part1, part2):
    s = set(s)
    s.difference_update(set(part1))

    return s.isdisjoint(set(part1))


if __name__ == '__main__':

	s, part1, part2 = 'codewars', 'cod', 'wars'

	print(is_merge(s, part1, part2))