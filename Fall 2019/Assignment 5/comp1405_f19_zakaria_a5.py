fullinput = []
wordinputs = []
fullinputstr = ''
myinput = input("input ur char \n")

def main():
    global fullinput
    global wordinputs
    global fullinputstr
    for i in myinput:
        asciimyinput = ''
        if 65 <= ord(i) <= 90:
            asciimyinput = ord(i)
        elif 97 <= ord(i) <= 122:
            asciimyinput = ord(i) - 32
        else:
            asciimyinput = ord(i)
        finalinput = chr(asciimyinput)
        fullinput.append(finalinput)
        print(f"{finalinput}", end='')
        fullinputstr = "".join(fullinput)
        wordinputs = fullinputstr.split()
main()
def changeinput():
    global myinput
    changeivalues = input('\nWhat do you want change a phrase, word or letter\n')
    changedivalues = input(f"What {changeivalues} would you like to change?"
                           f" (write down the {changeivalues} you want to change): {fullinputstr}\n")
    if changeivalues == 'words' or 'word' or 'a word':
        changeword = input(f"What would you want to change {changedivalues} to: ")
        changedivalues = wordinputs.index(changedivalues)
        wordinputs[changedivalues] = changeword
    myinput = " ".join(wordinputs)
    main()
changeinput()