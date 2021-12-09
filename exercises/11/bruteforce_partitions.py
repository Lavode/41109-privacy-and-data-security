import more_itertools as mit

# We'll use integers rather than floats to work around floating-point erorrs.
# As such, each probability is in [0, 100], and each distribution will sum to 100.
a = [10, 12, 15, 20, 43]
b = [15, 15, 15, 15, 15, 25]
c = [10, 10, 10, 14, 14, 14, 14, 14]


def get_best_partition(inp):
    '''Find partition of input into two disjoint subsets such that the absolute
    value of the sum of the subsets is minimized.

    This is a brute-force implementation of the partition problem, which will
    try all 2^n possible two-partitions of an n-length input.
    '''
    best_a, best_b = None, None
    best_diff = sum(inp)

    for a, b in mit.set_partitions(inp, 2):
        new_diff = abs(sum(a) - sum(b))
        if new_diff < best_diff:
            best_a, best_b = a, b
            best_diff = new_diff

    return best_a, best_b, best_diff

for x in [a, b, c]:
    print(f"Getting best partition for {a}")
    x_1, x_2, x_diff = get_best_partition(x)
    print(f"Partitioned into: {x_1} and {x_2} with difference {x_diff}")
