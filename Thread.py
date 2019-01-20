
import threading
from sfiles.sudoku import sudoku
import time


class sudokuthread(threading.Thread):
    def __init__(self,threadID,matrix):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.sudokuVariable = sudoku(matrix)
        self.starttime = time.time()
        self.stoptime = -1
    def run(self):
        print("The ID of the Thread is  {} anc active thread count {}".format(self.ThreadID,threading.active_count()))
        self.sudokuVariable.solve()
        self.stoptime = time.time()
        print("The Thread Duration: {}".format(self.stoptime-self.starttime))







