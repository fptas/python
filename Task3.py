

d = -1
while not (d >= 0 and d <= 9):
    dstr = input("Enter one gidit between 0 and 9: ")
    if not (dstr >= '0' and dstr <= '9'):
        continue
    d = int(dstr)
n = str(d)
nn = n + n
nnn = nn + n

rez = int(n) + int(nn) + int(nnn)
print(f"n+nn+nnn = {rez}")