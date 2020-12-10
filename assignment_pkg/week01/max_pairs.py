import sys


class MaxPairs:
    def calc_max_pairs(self, numbers):
        if len(numbers) < 2:
            return -1
        if len(numbers) == 2:
            return numbers[0] * numbers[1]
        max_idx = 0
        max_num = 0
        for idx, i in enumerate(numbers):
            if i > max_num:
                max_num = i
                max_idx = idx
        max_idx2 = 0
        max_num2 = 0
        for idx, i in enumerate(numbers):
            if i > max_num2 and idx != max_idx:
                max_num2 = i
                max_idx2 = idx

        return numbers[max_idx] * numbers[max_idx2]


if __name__ == "__main__":
    # str_numbers=input('please enter input numbers:')
    sys.stdin.readline()
    str_numbers = sys.stdin.readline()
    max_pair = MaxPairs()
    print(max_pair.calc_max_pairs([int(num) for num in str_numbers.split()]))
