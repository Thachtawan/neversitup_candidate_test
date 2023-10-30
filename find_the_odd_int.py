def find_the_odd_int(input):
    input = list(input)
    new_dic = {}
    result = ""

    for i in range(len(input)):
        if input[i] not in new_dic:
            new_dic[input[i]] = 1
        else:
            new_dic[input[i]] += 1

    for prop in new_dic:
        if int(new_dic[prop]) % 2 != 0:
            result = prop

    print(result)
    return result

find_the_odd_int([7])
find_the_odd_int([0])
find_the_odd_int([1,1,2])
find_the_odd_int([0,1,0,1,0])
find_the_odd_int([1,2,2,3,3,3,4,3,3,3,2,2,1])