# the main() function which executes everything
def main():
    # again value used to define if the user is going to run the run() function or ask the question for a new string
    again = False
    # a value to define if the while loop should continue or stop
    finished = False
    # a while loop which starts and continues as long as finished is False
    while not finished:
        # Takes in userinput and capitalizes it
        def upper():
            # puts each letter inputted by the user as a field in an array
            fullinput = []
            # puts each word inputted by the user as a field in an array
            wordinputs = []
            # saves the final capitalized string in a new string (fullinputstr)
            fullinputstr = ''
            # variable which takes in the user input
            myinput = input("Type the string to be translated: \n")
            # for loop which capitalizes the user input (loops through each letter in myinput)
            for i in myinput:
                # temporary variable which is used to store each letter's or ascii character's encoded number
                asciimyinput = ''
                # ensures the user input to be capitalized. If it's in between 97 and 122 then its lowercased;
                # hence, the condition capitalizes it
                if 97 <= ord(i) <= 122:
                    # subtracts it by 32 to save the capital encoding of the ascii character into asciimyinput
                    asciimyinput = ord(i) - 32
                elif 65 <= ord(i) <= 90:
                    asciimyinput = ord(i)
                else:
                    asciimyinput = 32
                # new variable which stores the decrypted version of the encoded ascii characters (in asciimyinput)
                finalinput = chr(asciimyinput)
                # saves the decrypted letter as a field in fullinput
                fullinput.append(finalinput)
                # joins the fields in fullinput into a string (saves it in fullinputstr)
                fullinputstr = "".join(fullinput)
                # splits each word from fullinputstr to be saved into wordinputs
                wordinputs = fullinputstr.split()
            # prints the final result of fullinputstr
            print(f'String for translation: {fullinputstr}')
            # returns all of them so that they could be used in further functions
            return fullinput, fullinputstr, wordinputs

        # a function which allows user to change phrases, words or letters
        def run():
            # takes the returned variables for further usage. It also runs the main function
            fullinput, fullinputstr, wordinputs = upper()

            # function which changes words
            def changewords():
                # variable which stores each letter inputted by the user which are part of their string
                finalvalue = []
                # variable which prompts the user if they want to change any words,
                # and it stores the lowercased value of their input
                changeivalues = input("Would you like to replace any of the words?:\n").lower()
                # if the user wants to change any words i.e. if the value of changeivalues is 'yes' then....
                if changeivalues == 'yes':
                    # a new variable which asks the user for what words in their string they want to change.
                    # (fullinputstr is taken from upper() function)
                    changedivalues = input(f"What word would you like to replace: {fullinputstr}\n")
                    # splits each word in changedivalues that is in changedivalues
                    splittedchangedivalues = changedivalues.split()
                    # loops through each field in splittedchangedivalues to see if it's is in their string
                    for i in range(0, len(splittedchangedivalues)):
                        # The field that it's looping through,
                        # check if that field's word is in the user's string (fullinputstr)
                        if splittedchangedivalues[i] not in fullinputstr.split():
                            # if its not in the user's string then print, that the field cannot be replaced
                            print(f"'{splittedchangedivalues[i]}' cannot be replaced. It is not part of your string."
                                  f" (Uppercase your characters)")
                        # or else, meaning if the field's word is in the user's string.
                        else:
                            # then add or append or push the field's word to finalvalue
                            finalvalue.append(splittedchangedivalues[i])
                    # now if the finalvalue (which only has changedivalues fields/words which are in user's string)
                    # is not the same as changedivalues then..
                    if "".join(finalvalue) != changedivalues:
                        # restart the function
                        changewords()
                    # or else, which includes finalvalue == changedivalues
                    # (all the values you want to change are in string), then...
                    else:
                        # new input variable which prompts then stores your new value replacement for changedivalues
                        changeinput = input(f"What would you want to replace '{changedivalues}' with: \n")
                        # finds the location of changedivalues field (which is a number) in wordinputs
                        # (from upper() function) and then stores it in the previous changedivalues
                        # (changes the previous values that were stored in changedivalues before)
                        changedivalues = wordinputs.index(changedivalues)
                        # takes the location in changedivalues and uses that so that
                        # it could change a specific value in wordinputs -- to changeinput (above)
                        wordinputs[changedivalues] = changeinput
                        # print the final results when words are changed.
                        # joins wordinputs into a string with a space between each word
                        print(f"After replacing words: {' '.join(wordinputs)}")
                # if the user doesn't want to change words, then..
                elif changeivalues == 'no':
                    # do nothing. which eventually makes it move on to the next function
                    print()
                # if its not yes or no then tell the user t type yes or no and restart the function
                else:
                    print("Answer with either 'yes' or 'no'")
                    changewords()

            # function which replaces phrases
            def changingphrase():
                # now since wordinputs been changed by the previous function,
                # we will bring in a new variable (txtstr1) which joins the words in wordinputs into a string
                txtstr1 = " ".join(wordinputs)
                # then here we split the string into a list which splits at each letter
                txt = list(txtstr1)
                # joins txt into a string
                txtstr = "".join(txt)
                # a new variable which prompts then stores user input, if they want to replace a phrase or not
                changeval = input("Would you like to replace a phrase?: \n").lower()
                # if the user wants to change a phrase
                if changeval == "yes":
                    # a new variable which prompts then stores the phrase that the user wants to replace
                    changedphrase = input(f"What phrase would you like to replace: {txtstr}\n")
                    # a list which takes in the field which are part of their string
                    changingval = []
                    # if changedphrase is not part of their string then..
                    if changedphrase not in " ".join(wordinputs):
                        # prints the phrase cannot be replaced
                        print(f"'{changedphrase}' cannot be replaced. It is not part of your string."
                              f" (Uppercase your characters)")
                    # or else, meaning changedphrase is part of their string
                    else:
                        # then you'll add changedphrase to changingval list
                        changingval.append(changedphrase)
                    # now if the final value of changingval when joined into a string is not the same as changedphrase..
                    if " ".join(changingval) != changedphrase:
                        # then restart the function
                        changingphrase()
                    # or else, meaning that the final value of changingval
                    # when joined into a string IS the same as changedphrase,
                    # or the phrase the user wants to change is part of their string
                    else:
                        # a new variable which finds the location of changedphrase in txtstr (in numbers)
                        inputindex = txtstr.index(changedphrase)
                        # a new variable which stores the length of changedphrase
                        inputlength = len(changedphrase)
                        # new input variable which prompts then stores the new phrase that the person wants to replace
                        myoutput = input(f"What would you like to replace '{changedphrase}' with?:\n")
                        # a new variable which stores the inputindex added with its length
                        inputrange = (inputindex + inputlength)
                        # a new variable which stores the inputindex
                        # and the length of the phrase the user would like to replace
                        outputrange = (inputindex + len(myoutput))
                        # a for loop which loops from the start of the location of changedphrase in the user's string,
                        # to the end of changedphrase
                        for i in range(inputindex, inputrange):
                            # then it makes all the fields in which the user wants to change, empty
                            txt[i] = ''
                        # once empty a for loop starts in which it loops two variables
                        # the first variable loops through the range between
                        # the start location of changedphrase in the user's input up to the end of the user's output.
                        # the second variable, x, loops through each letter in the user's output
                        for i, x in zip(range(inputindex, outputrange), myoutput):
                            # i represents the field location and x represents the value inserted in that location
                            txt.insert(i, x)
                        # prints the final ouput of when phrases been replaced
                        print(f"After replacing phrases: {''.join(txt)}")
                # if the user doesn't want to change phrases
                elif changeval == 'no':
                    # then do nothing. which eventually move on to the next function
                    print()
                # if the user doesnt write yes or no
                else:
                    # then print that these are the the only two options and restart the function
                    print("Answer with either 'yes' or 'no'")
                    changingphrase()
                # return txt so that it could be used for further usage.
                return txt

            # function which changes letters
            def changingletters():
                # imports txt variable from changingphrase() and runs changingphrase() as well
                txt = changingphrase()

                # nested function to only run the changing letters part.
                # Hence when this function is called then changingphrase() wont run again
                def changedletters():
                    # a new variable which prompts then stores if the user wants to change letters or not.
                    wanttochange = input("Do you want to replace any letters: \n").lower()
                    # if the user wants to change letters
                    if wanttochange == "yes":
                        # a new variable which prompts then stores the letters
                        # from their string that they want to replace
                        changevalue = input(f"What letters do you want to replace?: {''.join(txt)}\n")
                        # splits each letter in changevalue into a list and then stores it in splittedchangevalue
                        splittedchangevalue = list(changevalue)
                        # a new variable which stores all the letters,
                        # that the user wants to change, which are in user's string
                        changingvalue = []
                        # new variable which stores all the new letters that the user wants to replace changevalue with
                        changedvalue = []
                        # a loop which loops through each letter's location one by one
                        # and checks if each letter is in txt
                        for i in range(0, len(splittedchangevalue)):
                            # checks if the letter location, that its looping through, has a letter which is in txt
                            if splittedchangevalue[i] in txt:
                                # if the letter is in txt then it adds or appends that value to changingvalue
                                changingvalue.append(splittedchangevalue[i])
                                # then it asks what you'd like to replace that letter with
                                currentvalue = input(
                                    f"What would you like to replace '{splittedchangevalue[i]}' with?: \n")
                                # then it adds or appends the new value (currentvalue) to changedvalue
                                changedvalue.append(currentvalue)
                            # but if its not in txt
                            elif splittedchangevalue[i] not in txt:
                                # then print that the letter cannot be replaced. Because it is not part of their string.
                                print(f"'{splittedchangevalue[i]}' cannot be replaced. It is not part of your string."
                                      f" (Uppercase your characters)")
                                # and breaks the function
                                break
                        # finalvalue joins the changingvalue-list's letters into a string.
                        finalvalue = "".join(changingvalue)
                        # if the finalvalue is not the same as the user input
                        # i.e. if even some of the letters the user wants to change are not part of their string
                        if finalvalue != changevalue:
                            # then restart the function
                            changedletters()
                        # or else, meaning that all the letters the user wants to change are part of their string
                        else:
                            # then loop through two variables. The first variable loops through
                            # the finalvalue (each letter in the user's string that the user wants to change).
                            # The second variable loops through the new characters that the user wants
                            for m, x in zip(finalvalue, changedvalue):
                                # another, nested loop in which it loops through
                                # each field's location in txt (user's string)
                                for j in range(0, len(txt)):
                                    # if the field location contains a letter in which the user wants to replace
                                    if txt[j] == m:
                                        # then replace it with their letter (whch is defined in changedvalue)
                                        txt[j] = x
                            # then print that the letters are replaced
                            print(f'After replacing letters: {"".join(txt)}')
                    # but if the user doesn't want to change letters
                    elif wanttochange == "no":
                        # then do nothing, which will eventually make it move to the next function/step
                        print()
                    # if the user doesn't type yes or no
                    else:
                        # then print that those are the only two options
                        print("Answer with either 'yes' or 'no'")
                        # and restart the function, so that they can answer it again
                        changedletters()
                    # lastly, print their final result
                    print(f'Your translated string: {"".join(txt)}')

                # run the changedletters function. (This is nested under the changingletters() function)
                changedletters()

            # run changedwords() function. (this is nested under changewords() function)
            changewords()
            # run changewords() function.
            changingletters()

        # if again, (at the top of the page) is False, which is the default case
        if not again:
            # then run run() function
            run()
        # once it runs the run() function.
        # Then prompt and store the value of whether or not they'd like to translate a new string
        newstring = input("Do you want to translate a new string \n").lower()
        # if the user doesn't want a new string
        if newstring == "no":
            # then print goodbye.
            print("Goodbye.")
            # and turn finished's value to True, in order to stop the while loop
            finished = True
        # if the user wants to to translate a new string.
        elif newstring == "yes":
            # then keep again's value False so that it could run the run() function (line 261)
            again = False
        # but if the user doesn't type yes or no then
        else:
            # the print that those are their only two options
            print("Answer with either yes or no")
            # and turn again's value to True so that it could not meet line 261 condition and skip running the run()
            # function so that the user could answer the question again
            again = True


# runs the main() function at execution
if __name__ == '__main__':
    main()
