
itotalseconds = -1

while itotalseconds < 0:
    itotalseconds = int(input("Enter the number of seconds: "))

ihours = itotalseconds // 3600
iminutes = (itotalseconds % 3600) // 60
iseconds = (itotalseconds % 60)

shourspref = ''
sminutespref = ''
ssecondspref = ''

if ihours < 10:
    shourspref = '0'

if iminutes < 10:
    sminutespref = '0'

if iseconds < 10:
    ssecondspref = '0'

print(f'{shourspref}{ihours}:{sminutespref}{iminutes}:{ssecondspref}{iseconds}')

