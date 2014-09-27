from matrix_detex import *

def test_toMat():
	s = "\\begin{bmatrix} a \cdot b & 0 \\\\ 0 & 1 \\end{bmatrix} \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}"
	assert toMat(s)  == "{{a*b,0},{0,1}}{{0,1},{1,0}}"

def test_toTex():
	s = "{{a*b,0},{0,1}}{{0,1},{1,0}}"
	assert toTex(s)  == "\\begin{bmatrix} \na \cdot b&0\\\\\n0&1\n\\end{bmatrix}\\begin{bmatrix} \n0&1\\\\\n1&0\n\\end{bmatrix}"