class MaxPairs:
    def max_pairs_naive(self, numbers):
        assert len(numbers) >= 2
        assert all (0<= a <= 2 * 10**5 for a in numbers)
        product=0
        for i in range(len(numbers)):
            for j in range(i +1, len(numbers)):
                product=max(product,numbers[i] * numbers[j])
        return product

    def max_pairs(self, numbers):
        assert len(numbers) >= 2
        assert all (0<= a <= 2 * 10**5 for a in numbers)

        if len(numbers) == 2:
            return numbers[0] * numbers[1]
        max_idx1 = 0
        for idx, i in enumerate(numbers):
            if i > numbers[max_idx1]:
                max_idx1 = idx
        max_idx2 = 1
        for idx, i in enumerate(numbers):
            if i > numbers[max_idx2] and idx != max_idx1:
                max_idx2 = idx

        return numbers[max_idx1] * numbers[max_idx2]


if __name__ == "__main__":
    list_len=int(input())
    numbers=list(map(int,input().split()))
    assert list_len == len(numbers)
    max_pair = MaxPairs()
    print(max_pair.calc_max_pairs(numbers))
