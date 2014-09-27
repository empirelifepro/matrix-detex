
from Tkinter import Tk
import re

def copy(s, root):
    root.clipboard_clear()
    root.clipboard_append(s)
    
def toMat():
    root = Tk()
    s = root.clipboard_get()
    print s

    s = re.sub(r'\\begin{.+?}', '{{', s)
    s = re.sub(r'\\end{.+?}', '}}', s)
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    s = s.replace('&', ',')
    s = s.replace('\\\\', '},{')
    s = s.replace('\cdot', '*')
    s = s.replace('\left', '')
    s = s.replace('\right', '')

    print s
    copy(s, root)
    root.destroy()

def toTex():
    root = Tk()
    s = root.clipboard_get()
    print s
    
    s = s.replace("{{", "\\begin{bmatrix} \n")
    s = s.replace("}}", "\n\\end{bmatrix}")
    s = s.replace("},{", "\\\\\n")
    s = s.replace(",", "&")
    s = s.replace("*", " \\cdot ")
    
    print s
    copy(s, root)
    root.destroy()
