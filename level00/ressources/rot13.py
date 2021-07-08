text = 'cdiiddwpgswtgt'

rot1 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'BCDEFGHIJKLMNbcdefghijklmnOPQRSTUVWXYZAopqrstuvwxyza')

test = text.translate(rot1)

print (test)

rot2 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'CDEFGHIJKLMNOcdefghijklmnoPQRSTUVWXYZABpqrstuvwxyzab')



test = text.translate(rot2)

print (test)


rot3 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'DEFGHIJKLMNOPdefghijklmnopQRSTUVWXYZABCqrstuvwxyzabc')


test = text.translate(rot3)

print (test)


rot4 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'EFGHIJKLMNOPQefghijklmnopqRSTUVWXYZABCDrstuvwxyzabcd')


test = text.translate(rot4)

print (test)


rot5 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'FGHIJKLMNOPQRfghijklmnopqrSTUVWXYZABCDEstuvwxyzabcde')


test = text.translate(rot5)

print (test)


rot6 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'GHIJKLMNOPQRSghijklmnopqrsTUVWXYZABCDEFtuvwxyzabcdef')


test = text.translate(rot6)

print (test)


rot7 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'HIJKLMNOPQRSThijklmnopqrstUVWXYZABCDEFGuvwxyzabcdefg')


test = text.translate(rot7)

print (test)


rot8 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'IJKLMNOPQRSTUijklmnopqrstuVWXYZABCDEFGHvwxyzabcdefgh')


test = text.translate(rot8)

print (test)


rot9 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'JKLMNOPQRSTUVjklmnopqrstuvWXYZABCDEFGHIwxyzabcdefghi')


test = text.translate(rot9)

print (test)


rot10 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'KLMNOPQRSTUVWklmnopqrstuvwXYZABCDEFGHIJxyzabcdefghij')


test = text.translate(rot10)

print (test)


rot11 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'LMNOPQRSTUVWXlmnopqrstuvwxYZABCDEFGHIJKyzabcdefghijk')


test = text.translate(rot11)

print (test)


rot12 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'MNOPQRSTUVWXYmnopqrstuvwxyZABCDEFGHIJKLzabcdefghijkl')


test = text.translate(rot12)

print (test)


rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

test = text.translate(rot13)

print (test)