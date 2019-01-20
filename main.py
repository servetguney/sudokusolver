'''
A1 B1 C1 | D1 E1 F1 | G1 H1 I1
A2 B2 C2 | D2 E2 F2 | G2 H2 I2
A3 B3 C3 | D3 E3 F3 | G3 H3 I3

A4 B4 C4 | D4 E4 F4 | G4 H4 I4
A5 B5 C5 | D5 E5 F5 | G5 H5 I5
A6 B6 C6 | D6 E6 F6 | G6 H6 I6

A7 B7 C7 | D7 E7 F7 | G7 H7 I7
A8 B8 C8 | D8 E8 F8 | G8 H8 I8
A9 B9 C9 | D9 E9 F9 | G9 H9 I9
'''
'''
53EE7EEEE
6EE195EEE
E98EEEE6E
8EEE6EEE3
4EE8E3EE1
7EEE2EEE6
E6EEEE28E
EEE419EE5
EEEE8EE79
'''




class sudoku:

    default_list = [1,2,3,4,5,6,7,8,9]

    def __init__(self,filename:str):
        self.sudoku_matrix = []
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
            self.sudoku_matrix.append(tmatrix)


    def checkMissing(self,toCheckList:list,TargetList:list):
        print("The checkList {} TargetList {}".format(toCheckList,TargetList))
        resultList = [x for x in toCheckList if x not in TargetList]
        print("The returnList {}".format(resultList))
        return resultList

    def createColumnList(self,index:int,matrix:list):
        resultList = []
        for i in range(len(self.default_list)):
            resultList.append(matrix[i][index])
        return resultList

    def createRowList(self,index:int,matrix:list):
        return matrix[index]

    def createRegionList(self,index:int,matrix:list):
        regionList = []
        frindex = 0
        fgindex = 0

        if index < 3:
            frindex = 0
            fgindex = ( index % 3 ) * 3
        elif index >=3 and index < 6:
            frindex = 3
            fgindex = ( index % 3 ) * 3
        elif index >= 6:
            frindex = 6
            fgindex = ( index % 3 ) * 3

        regionList.append(matrix[frindex][fgindex])
        regionList.append(matrix[frindex][fgindex+1])
        regionList.append(matrix[frindex][fgindex+2])
        regionList.append(matrix[frindex+1][fgindex])
        regionList.append(matrix[frindex+1][fgindex+1])
        regionList.append(matrix[frindex+1][fgindex+2])
        regionList.append(matrix[frindex+2][fgindex])
        regionList.append(matrix[frindex+2][fgindex+1])
        regionList.append(matrix[frindex+2][fgindex+2])
        return regionList
    def memberRegion(self,rindex,gindex):
        if rindex < 3 and gindex < 3:
            return 0
        elif rindex < 3 and ( gindex >= 3 and gindex < 6):
            return 1
        elif rindex < 3 and gindex >=6:
            return 2
        elif (rindex >=3 and rindex < 6 ) and gindex < 3 :
            return 3
        elif (rindex >=3 and rindex < 6 ) and (gindex >= 3 and gindex < 6):
            return 4
        elif (rindex >= 3 and rindex < 6) and gindex >=6:
            return 5
        elif rindex >= 6 and gindex < 3:
            return 6
        elif rindex >= 6 and (gindex >= 3 and gindex < 6):
            return 7
        elif rindex >= 6 and gindex >=6:
            return 8

    def UpdateMatrix(self,matrix:list):
        candidate = matrix.copy()
        updateList = []
        resolvedTotalNumber = 81
        resolvedNumber = 0

        while True:
            resolvedNumber = 0
            updateList = []
            for i in range(len(self.default_list)):
                for j in range(len(candidate[i])):
                    if candidate[i][j] is None:
                        set1 = set(self.checkMissing(self.default_list,self.createColumnList(j,candidate)))
                        set2 = set(self.checkMissing(self.default_list,candidate[i]))
                        set3 = set(self.checkMissing(self.default_list,self.createRegionList(self.memberRegion(i,j),candidate)))
                        setinter = list((set1.intersection(set2)).intersection(set3))

                        print("The set 1 {} and set 2 {} and set 3 {}".format(set1,set2,set3))
                        print("The setInter {}".format(setinter))
                        if not setinter:
                            return ["FAILED",[]]
                        if len(setinter) == 1:
                            candidate[i][j]= setinter[0]
                            print("The candidate {}".format(candidate))
                        updateList.append(len(setinter))
                        print("The update List {} ".format(updateList))
                    elif candidate[i][j] is not None:
                       resolvedNumber +=1
                       if resolvedNumber == resolvedTotalNumber:
                           print("The quiz has been solved")
                           return ["SOLVED",matrix]
            if min(updateList) >= 1:

                return ["NEED",matrix]
            for i in candidate:
                print("The matrix {}".format(i))
        print("The matrix {}".format(matrix))
        print("The resolvedNumber {}".format(resolvedNumber))

    def test(self,matrix:list):
        print(id(matrix))
        print(id(self.sudoku_matrix))

        temp = matrix.copy()
        print(id(temp))
        print("The  class sudoku matrix is {}".format(self.sudoku_matrix))
        print("The function sudoku_matrix is {}".format(matrix))

        temp[0][0]=99
        print("The  class sudoku matrix is {}".format(self.sudoku_matrix))
        print("The function matrix is {}".format(matrix))
        print("The function temp is {}".format(temp))


if __name__=="__main__":
    s=sudoku("mysudoku2.txt")
    #s.test(s.sudoku_matrix)
    [a,b]=s.UpdateMatrix(s.sudoku_matrix)
    print("Tha status is  {} and matrix is {}".format(a,b))
    #s.arrange(s.sudoku_matrix)
