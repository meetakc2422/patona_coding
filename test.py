au = 'ttyyuuurrrrr'
expected_output = 't2y2u3r5'
c = ''
di = 1
print(len(au))
for i in range(len(au)):
    try:
        b = au[i]
        if b == au[i+1]:
            di += 1
        else:
            c += au[i]+str(di)
            di = 1
    except IndexError as e:
        c += au[i] + str(di)

print(c)
