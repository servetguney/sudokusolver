


from sfiles.sudoku import sudoku
from sfiles.Thread import sudokuthread
import copy
import multiprocessing
import math

def loadFile(filename:str,formatType:str):
    matrix_list = []
    if formatType == "dotted":
        with open(filename,"r") as f:
            data=f.readlines()
        for line in data:
            temp = list(line.rstrip())
            tmatrix = []
            rmatrix = []
            position = 1
            for i in range(len(temp)):
                if temp[i] != '.':
                    rmatrix.append(int(temp[i]))
                elif temp[i] == '.':
                    rmatrix.append(None)
                if position == 9:
                    tmatrix.append(copy.deepcopy(rmatrix))
                    rmatrix = []
                    position = 0
                position += 1
            matrix_list.append(copy.deepcopy(tmatrix))
        return matrix_list
    elif formatType  == "withZero":
        pass
    elif formatType == "withE":
        with open(filename,"r") as f:
            data=f.readlines()
        for line in data:
            temp = list(line.rstrip())
            tmatrix = []
            for i in range(len(temp)):
                if temp[i] != 'E':
                    tmatrix.append(int(temp[i]))
                elif temp[i] == 'E':
                    tmatrix.append(None)
            matrix_list.append(tmatrix)
        return [matrix_list]
    else:
        print("Can not find the fileformat, \"dotted\",\"withZero\",\"withE\"")


def multiprocessWork(thecompoundmatrix):
    counter = 0
    for i in thecompoundmatrix:
        t = sudokuthread(counter, i)
        t.start()
        counter += 1

if __name__=="__main__":
    target = loadFile("mysudoku15","dotted")
    packunitnumber = 1200
    total = len(target)
    packnumber = math.ceil(total / packunitnumber)
    print(packnumber)
    p = multiprocessing.Process(target=multiprocessWork,args=(target[0:1199],))
    a = multiprocessing.Process(target=multiprocessWork,args=(target[1200:total],))
    p.start()
    a.start()