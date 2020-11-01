import numpy as np
import random as rd
import pickle
np.random.seed(42)
rd.seed(42)


def dictLoad():
    with open('SCDict', 'r') as handle:
        data = handle.read()
    SandCO = pickle.loads(data)
    return SandCO

def randomWrong(index):
    first = rd.randrange(0, 49, 1)
    while(first == index):
        first = rd.randrange(0, 49, 1)
    second = rd.randrange(0, 49, 1)
    while((second == first) or (second == index)):
        second = rd.randrange[49]
    third = rd.randrange[49]
    while((third == second) or (third == index)):
        third = rd.randrange[49]
    return first, second, third

def Options():
    answer = dictLoad()
    first, second, third = 0, 0, 0
    Qlist = list()
    Klist = list()
    for i in range(0, 49, 1):
        first, second, third = randomWrong(i)
        Klist[i].append(answer[i]['state'])
        Qlist[i].append([answer[i]['capital'],
                         answer[first]['capital'],
                         answer[second]['capital'],
                         answer[third]['capital']])
    return Qlist, Klist

def masterLists(Qlist, Klist):
    keyList = list()
    testList = list()
    with open('mkey', 'at') as masterKey:
        masterKey.write('The Master Answer Key\n\n')
    with open('mtest', 'at') as masterTest:
        masterTest.write('The Master Test\n\n')
        for i in range(0, 49, 1):
            masterKey.write(f"{i}: State = {Klist[i]['state']}, Capital = {Qlist[i][0]['capital']}")
            keyList[i].append(Klist[i], Qlist[i][0])
            masterTest.write(f"{i}: The capital of {Klist[i]} is:\n\n")
            testList[i].append(Qlist[i][0]['capital'], Qlist[i][1]['capital'], Qlist[i][2]['capital'], Qlist[i][3]['capital'])
            masterTest.write(f"a: {Qlist[i][0]['capital']}\n")
            masterTest.write(f"b: {Qlist[i][1]['capital']}\n")
            masterTest.write(f"c: {Qlist[i][2]['capital']}\n")
            masterTest.write(f"d: {Qlist[i][3]['capital']}\n")
    return keyList, testList

def createQuizzes(keyList, testList):
    total = list(zip(keyList, testList))
    rd.shuffle(total)
    keyList, testList = zip(*total)
    for i in range(0, 34, 1):
        with open(f'quiz.{i}', 'wt') as totalQuiz:
            np.random.shuffle(testList[i])
            totalQuiz.write(f"{i}: The capital of {testList[i].pop([i][0])} is: \n\n")
            totalQuiz.write(f"a:{testList[i][0]['capital']}.\n")
            totalQuiz.write(f"b:{testList[i][1]['capital']}.\n")
            totalQuiz.write(f"c:{testList[i][2]['capital']}.\n")
            totalQuiz.write(f"d:{testList[i][3]['capital']}.\n")

# Let there be quizzes!
Options()