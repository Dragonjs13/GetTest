import sys

original = [6, 16, 2, 7, 4]
input1 = ['01', '0111', '001', '001', '00001',]
"""
          '01111', '01', '000011', '0001', '01', '0111', '0011', '01', '000011', '01', '01111', '0111', '00001', '00001', '0111', '001', '001', '000111', '000011', '01', '01111', '0111', '0111', '00111', '0011', '001', '01', '011', '000011', '01111', '0001', '0111', '001', '011', '01111', '0000111', '0011', '00001', '011', '0011', '01', '01', '01', '01111', '001', '0111', '0001', '00011', '00111', '011', '00001', '01111', '00011', '01', '00111', '00001', '001', '00001', '00001', '011', '011', '01', '01', '01', '01', '0001', '0111', '0001', '0111', '000111', '00001', '011', '011', '0111', '000111', '01111', '0000111', '00001', '0011', '0000111', '00001', '01', '001', '0001']
          """
firstNum = {'01': 1, '001': 2, '0001': 3, '00001': 4}
secondNum = {'01': 6, '001': 7, '0001': 8, '00001': 9}
problemNumbers = {'01', '001', '0001', '00001'}


def convertFromEM(array):
    base = []
    for x in array:
        num = 0
        for i in x:
            if int(i) == 0:
                num = num + 1
            if int(i) == 1:
                num = num + 5
        if num == 21:
            num = 0
        base.append(num)
    return base


def P(input2):
    print("Input", input2)
    # let possibilities = array of all possibilities
    possibilities = []
    # get the first problem number index

    idx = [i for i, item in enumerate(input2) if item in problemNumbers]
    print(idx)

    if len(idx) == 0:
        print("NP")
        # no more problem numbers
        possibilities = [convertFromEM(input2)]
    else:
        print("P")
        idx = min(int(s) for s in idx)
        # let endPossibilities  = [P(input1[idx + 1 .. n])]
        endPossibilities = [P(input2[idx + 1:])]
        for possibilityArray in endPossibilities:
            for possibility in possibilityArray:
                possibilities.append(convertFromEM(input2[:idx]) + [firstNum[input2[idx]]] + possibility)
                possibilities.append(convertFromEM(input2[:idx]) + [secondNum[input2[idx]]] + possibility)

    return possibilities

sys.setrecursionlimit(10000)
p = P(input1)
correctPos = p.index(original)

print("END", p)

