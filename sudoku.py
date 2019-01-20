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

import copy
import time


class sudoku:

    default_list = [1,2,3,4,5,6,7,8,9]
    def __init__(self,matrix:list):
        self.object_list = []
        self.object_list.append(copy.deepcopy([matrix]))

    def checkMissing(self,toCheckList:list,TargetList:list):
        resultList = [x for x in toCheckList if x not in TargetList]
        return resultList

    def createColumnList(self,index:int,matrix:list):
        resultList = []
        for i in range(len(self.default_list)):
            resultList.append(matrix[i][index])
        return resultList

    def createRowList(self,index:int,matrix:list):
        return matrix[index]

    def createRegionList(self,index:int,matrix:list):
        resultList = []
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
        resultList.append(matrix[frindex][fgindex])
        resultList.append(matrix[frindex][fgindex+1])
        resultList.append(matrix[frindex][fgindex+2])
        resultList.append(matrix[frindex+1][fgindex])
        resultList.append(matrix[frindex+1][fgindex+1])
        resultList.append(matrix[frindex+1][fgindex+2])
        resultList.append(matrix[frindex+2][fgindex])
        resultList.append(matrix[frindex+2][fgindex+1])
        resultList.append(matrix[frindex+2][fgindex+2])
        return resultList

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

    def intersectionList(self,i,j,matrix):
        set1 = set(self.checkMissing(self.default_list,self.createColumnList(j,matrix)))
        set2 = set (self.checkMissing(self.default_list, matrix[i]))
        set3 = set (self.checkMissing(self.default_list, self.createRegionList(self.memberRegion(i, j), matrix)))
        return list((set1.intersection(set2)).intersection(set3))


    def iterateOver(self,matrix):

        resolvedTotalNumber = 81
        candidate_possibility = [9,[],[]]

        while True:
            changecount = 0
            resolvedNumber = 0

            for i in range(len(self.default_list)):
                for j in range(len(matrix[i])):

                    if matrix[i][j] is None:
                        set_intersection = self.intersectionList(i,j,matrix)

                        if not set_intersection:
                            return ["FAILED",[]]

                        if len(set_intersection) == 1:
                            matrix[i][j] = set_intersection[0]
                            changecount += 1

                        if len(set_intersection) < candidate_possibility[0]:
                            candidate_possibility[0] = len(set_intersection)
                            candidate_possibility[1] = [i, j]
                            candidate_possibility[2] = set_intersection

                    if matrix[i][j] is not None:
                        resolvedNumber += 1
                        if resolvedNumber == resolvedTotalNumber:
                            return ["SOLVED",[]]

            if changecount == 0:
                return ["NEED",candidate_possibility]

    def solve(self):
        start_time = time.time()
        max_object_dept = 0
        if not self.object_list:
            print("The Sudoku Can Not be Solved")
            return
        else:
            while self.object_list:
                if len(self.object_list) > max_object_dept:
                    max_object_dept = len(self.object_list)
                temporary = copy.deepcopy(self.object_list[-1][-1])
                result = self.iterateOver(temporary)
                if result[0] == "SOLVED":
                    end_time = time.time ()
                    print ( "Duration:{}:Maximum Object Dept:{}".format (
                        (str(end_time - start_time).replace(".",",")) , max_object_dept ) )
                    return
                if result[0] == "FAILED":
                    self.object_list.pop()
                if result[0] == "NEED":
                    last_object = copy.deepcopy ( self.object_list [ -1 ] )
                    self.object_list.pop ()
                    for i in result[1][2]:
                        temporary[result[1][1][0]][result[1][1][1]] = i
                        last_object.append(copy.deepcopy(temporary))
                        self.object_list.append(copy.deepcopy(last_object))
                        last_object.pop()