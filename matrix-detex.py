
from Tkinter import Tk

def texToMat():
    s = Tk().clipboard_get()
    print s

    if "\\begin{" in s:
        s = s[s.find('}', 0, len(s))+1:]
    if "\\end{" in s:
        s = s[:s.rfind('\\', 0, len(s))]
    s = s.replace(" ", "")
    s = s.replace("&", ",")
    s = s.replace("\\\\", "},{")
    s = "{{" + s + "}}"

    print s
    Tk().clipboard_clear()
    Tk().clipboard_append(s)
    Tk().destroy()
