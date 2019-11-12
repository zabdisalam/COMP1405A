def main():
    fullinput = []
    wordinputs = []
    fullinputstr = ''
    myinput = input("input ur char \n")
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
    return fullinput, fullinputstr, wordinputs, myinput


def changewords():
    fullinput, fullinputstr, wordinputs, myinput = main()

    def run():

        changeivalues = input("\nWould you like to change the words?")
        if changeivalues == 'yes':
            changedivalues = input(f"What words would you like to change?"
                                   f" (write down the word you want to change): {fullinputstr}\n")
            changeinput = input(f"What would you want to change {changedivalues} to: ")
            changedivalues = wordinputs.index(changedivalues)
            wordinputs[changedivalues] = changeinput
            print(" ".join(wordinputs))
        elif changeivalues != 'yes' or 'no':
            print("Answer with either yes or no")
            run()
    run()


changewords()
