
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
    points = list()
    Stuart = 0
    Kevin = 0

    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            points.append(string[i:j])
    
    for j in points:

        if j[0] in "AEIOU":
            Kevin+=1
        else:
            Stuart+=1
    
    if Stuart>Kevin:
        return(f'Stuart {Stuart}')
    elif Kevin>Stuart:
        return(f'Kevin {Kevin}')
    else:
        print("Draw")
    

print(minion_game('BANANANA'))