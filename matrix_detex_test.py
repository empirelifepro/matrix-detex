from matrix_detex import *

def test():
	root = Tk()
	s = "\\begin{bmatrix} a \cdot b & 0 \\\\ 0 & 1 \\end{bmatrix} \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}"
	#s = "\left( 13 \cdot 6 \right) \cdot \left( 12 \cdot 6 \right) \cdot \left( 11 \cdot 4 \right)"
	copy(s , root)
	toMat()
	return root.clipboard_get() == "{{a*b,0}{0,1}}{{0,1},{1,0}}"