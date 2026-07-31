from itertools import permutations
def solve(puzzle):
    left, result = puzzle.split(" == ")
    addends = left.split(" + ")
    full_sentence = addends + [result]
    unique_letters = set("".join(full_sentence))

    for j in permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, j))
        if any(len(word) > 1 and letter_to_digit[word[0]] == 0 for word in full_sentence):
            continue
        left_sum = sum(int("".join(str(letter_to_digit[c]) for c in word)) for word in addends)
        right_sum = int("".join(str(letter_to_digit[c]) for c in result))
        if left_sum == right_sum:
            return letter_to_digit