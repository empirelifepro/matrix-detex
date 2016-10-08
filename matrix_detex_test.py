from matrix_detex import *

def test_to_mat():
	s = '\\begin{bmatrix} a \cdot b & 0 \\\\ 0 & 1 \\end{bmatrix} \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}'
	assert to_mat(s)  == '{{a*b, 0}, {0, 1}}{{0, 1}, {1, 0}}'

def test_to_tex():
	s = '{{a*b, 0}, {0, 1}}{{0, 1}, {1, 0}}'
	assert to_tex(s)  == '\\begin{bmatrix} \na \\cdot b & 0 \\\\\n0 & 1\n\\end{bmatrix}\\begin{bmatrix} \n0 & 1 \\\\\n1 & 0\n\\end{bmatrix}'
