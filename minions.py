
#  input= list of elements that might have repeats
#  output= list without repeats
def unique(ls):
    unique = list()
    for i in ls:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique


def minion_game(string):
    Stuart = 0
    Kevin = 0
    length = len(string)

    for i in range(length):
        if string[i].upper() in "AEIOU":
            Kevin += length-i
        else:
            Stuart += length-i
    if Stuart > Kevin:
        print(f'Stuart {Stuart}')
    elif Kevin > Stuart:
        print(f'Kevin {Kevin}')
    else:
        print('Draw')


print(minion_game('BANANA'))