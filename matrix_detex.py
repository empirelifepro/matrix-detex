
from Tkinter import Tk
import re

def copy(s, root):
    root.clipboard_clear()
    root.clipboard_append(s)
    
def toMat(s):
    s = re.sub(r'\\begin{.+?}', '{{', s)
    s = re.sub(r'\\end{.+?}', '}}', s)
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    s = s.replace('&', ',')
    s = s.replace('\\\\', '},{')
    s = s.replace('\cdot', '*')
    s = s.replace('\left', '')
    s = s.replace('\right', '')
    return s

def toTex(s):
    s = s.replace("{{", "\\begin{bmatrix} \n")
    s = s.replace("}}", "\n\\end{bmatrix}")
    s = s.replace("},{", "\\\\\n")
    s = s.replace(",", "&")
    s = s.replace("*", " \\cdot ")
    return s

def main():
    root = Tk()
    s = root.clipboard_get()
    print s
    if s[0] == '{':
        out = toTex(s)
    else:
        out = toMat(s)
    print out
    copy(out, root)
    root.destroy()  