def countSmileys(input):
    input = list(input)
    count_valid = 0

    for i in range(len(input)):
        # print(input[i])
        for j in range(len(input[i])):
            # print(input[i][j])
            if j == 0:
                if input[i][j] == ":" or input[i][j] == ";":
                    continue 
                else:
                    break

            if j == 1 and (input[i][j] == "-" or input[i][j] == "~"):
                continue
            elif j == 1 and (input[i][j] == ")" or input[i][j] == "D"):
                count_valid += 1
            elif j == 2:
                if input[i][j] == ")" or input[i][j] == "D":
                    count_valid += 1
            else:
                break

    print(count_valid)
    return count_valid

countSmileys([':)', ';(', ';}', ':-D'])
countSmileys([';D', ':-(', ':-)', ';~)'])
countSmileys([';]', ':[', ';*', ':$', ';-D'])