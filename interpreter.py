import sys

def interpreter(t):
    m = [0]
    p = 0
    out = ""
    i = 0

    while i < len(t):
        c = t[i]
        if c == ">":
            p += 1
            if p == len(m):
                m.append(0)
        elif c == "<":
            p -= 1
            if p < 0:
                raise IndexError("Pointer moved below zero!")
        elif c == "+":
            m[p] += 1
        elif c == "-":
            m[p] -= 1
        elif c == ".":
            out += chr(m[p])
        elif c == ",":
            m[p] = ord(t())
        elif c == "[":
            if m[p] == 0:
                count = 1
                while count > 0:
                    i += 1
                    if t[i] == "[":
                        count += 1
                    elif t[i] == "]":
                        count -= 1
        elif c == "]":
            if m[p] != 0:
                count = 1
                while count > 0:
                    i -= 1
                    if t[i] == "]":
                        count += 1
                    elif t[i] == "[":
                        count -= 1
        i += 1
    return out

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            print(interpreter(file.read()))