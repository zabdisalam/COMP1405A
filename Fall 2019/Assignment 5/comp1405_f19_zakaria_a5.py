fullinput = []
wordinputs = []
fullinputstr = ''
myinput = input("input ur char \n")

def start():
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
start()
def main():
    global myinput
    changeivalues = input('\nWhat do you want change a phrase, word or letter\n')
    changedivalues = input(f"What {changeivalues} would you like to change?"
                           f" (write down the {changeivalues} you want to change): {fullinputstr}\n")
    if changeivalues == 'words' or 'word' or 'a word':
        changeword = input(f"What would you want to change {changedivalues} to: ")
        changedivalues = wordinputs.index(changedivalues)
        wordinputs[changedivalues] = changeword
    myinput = " ".join(wordinputs)
    start()
main()

# def cashregister(x):
#     cents = [25, 10, 5, 1]
#     for i in cents:
#         if x-i >= 0:
#             x = x-i
#             print(i, end=' ')
#             cashregister(x)
#
# cashregister(38)
#
# def change(n, coins_available, coins_so_far):
#     if sum(coins_so_far) == n:
#         yield coins_so_far
#     elif sum(coins_so_far) > n:
#         pass
#     elif coins_available == []:
#         pass
#     else:
#         for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
#             yield c
#         for c in change(n, coins_available[1:], coins_so_far):
#             yield c
#
# if __name__ == '__main__':
#     n = 90
#     coins = [1, 5, 10, 25]
#
#     solutions = [s for s in change(n, coins, [])]
#     for s in solutions:
#         s
#
#     print('optimal solution:', min(solutions, key=len))