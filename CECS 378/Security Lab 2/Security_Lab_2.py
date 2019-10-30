import string

alphaLower = list(string.ascii_lowercase)
alphaUpper = list(string.ascii_uppercase)

def ShiftCharacters(stringToEdit, amountToShift):
    finalString = ""
    for char in stringToEdit:
        if char.isalpha():
            if char.isupper():
                letterIndex = alphaUpper.index(char)
                finalString = finalString + alphaUpper[((letterIndex + amountToShift) % 26)]
            else:
                letterIndex = alphaLower.index(char)
                finalString = finalString + alphaLower[((letterIndex + amountToShift) % 26)]
        else:
            finalString = finalString + char
    return finalString

stringToTranslate = """
F elmb vlr afak'q qoxkpixqb fq yv exka, qexq'p texq zljmrqbop xob clo. Fc vlr afa fq yv
exka, vlr pelria obal fq ybzrxpb alfkd fq fk yv exka fp fkbccfzfbkq xka qexq'p tev qefp
qbuq fp pl ilkd. Xipl, qefp xppfdjbkq zxiip clo x pjxii mvqelk moldoxj. Lkb txv lc plisfkd
qefp fp rpfkd pqofkd.jxhbqoxkp() xka tefib fq fp obzljjbkaba; fq fp klq kbzbppxofiv qeb
lkiv lmqflk vlr exsb. Elmb vlr exa crk tlohfkd qefp lrq.
"""
## Would have easily worked with a little trial and error, but the clue was more than enough 
## as each letter was 3 ahead of the first in the picture
print(ShiftCharacters(stringToTranslate, 3))