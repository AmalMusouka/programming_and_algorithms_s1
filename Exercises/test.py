input_string = """Some glory in their birth, some in their skill,
Some in their wealth, some in their bodies' force,
Some in their garments, though new-fangled ill,
Some in their hawks and hounds, some in their horse;
And every humour hath his adjunct pleasure,
Wherein it finds a joy above the rest:
But these particulars are not my measure;
All these I better in one general best.
Thy love is better than high birth to me,
Richer than wealth, prouder than garments' cost,
Of more delight than hawks or horses be;
And having thee, of all men's pride I boast:
Wretched in this alone, that thou mayst take
All this away and me most wretched make."""


def words_from_string(input: str):
    words = input.lower().split()
    return words


def solve(input: str):
    words = words_from_string(input)
    tally = {}
    for word in words:
        key = len(word)

        if key not in tally:
            tally[key] = []

        tally[key].append(word)

    return tally



print(solve(input_string))