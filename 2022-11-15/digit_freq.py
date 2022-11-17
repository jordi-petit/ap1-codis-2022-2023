import yogi
from typing import List


def print_mes_freq(counts: List[int]) -> None:
	pos_max = 0
	max_count = counts[0]
	for idx, count in enumerate(counts):
		if count > max_count:
			pos_max = idx
			max_count = count
	print(pos_max, max_count)


def main() -> None:
	base = yogi.read(int)
	counts: List[int] = [0 for i in range(base)]
	num = yogi.scan(int)
	while num is not None:
		if num == 0:
			counts[0] += 1
		while num > 0:
			counts[num % base] += 1
			num = num // base
		num = yogi.scan(int)

	print_mes_freq(counts)


if __name__ == "__main__":
	main()