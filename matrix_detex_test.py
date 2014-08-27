from matrix_detex import *


def test():
    root = Tk()
    s = "\\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}"
    copy(s , root)
    toMat()
    
test()    
