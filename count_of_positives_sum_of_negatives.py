# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers.

# If the input array is empty or null, return an empty array.


def count_positives_sum_negatives(arr):
    result = [0, 0]
    for i in arr:
        if i > 0:
            result[0] = result[0] + 1
        elif i < 0:
            result[1] = result[1] + int(i)
    if len(arr) == 0:
        result = []

    return result


if __name__ == '__main__':
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
    assert count_positives_sum_negatives([1]) == [1, 0]
    assert count_positives_sum_negatives([- 1]) == [0, -1]
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
    assert count_positives_sum_negatives([]) == []

    print("Well job!")
