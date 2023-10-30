import itertools

def permutations(text):
    result = []
    text = str(text)

    list_permuted = list(itertools.permutations(text))
    for i in range(len(list_permuted)):
        new_text = "".join(list_permuted[i])

        if new_text in result:
            continue
        else:
            result.append(new_text)

    print(result)
    return result

permutations("a")
permutations("ab")
permutations("abc")
permutations("aabb")