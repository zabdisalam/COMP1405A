professions = ["Be a climatologist from Toronto",
               "Be a doctor from Los Angeles", "Be a police from Ottawa"]
team = ["", "", "", ""]
supplies = {
    "climatoligists": {
        "thermometer": 23.80,
        "hygrometer": 30.60,
        "barometer": 40.25
    },
    "doctors": {
        "syringe": 12.00,
        "anesthesia": 70.76,
        "scalpel": 25.81
    },
    "polices": {
        "tazer": 40.65,
        "gun": 90.56,
        "car": 265.50
    }
}

budget = 650
originalBudget = 0


def alterTeam():
    for i in range(len(team)):
        print(i + 1, end=" ")
        print(team[i])


for i in range(len(professions)):
    print(i + 1, end=" ")
    print(professions[i])
    if i == 2:
        # chosen profession value
        cpval = int(input("\n What's the profession of your choice?  _"))
        if 1 <= cpval <= 3:
            professions[0] = "climatoligists"
            professions[1] = "doctors"
            professions[2] = "polices"
            print(
                "\n", f"Who do you want to be amongst your team of {professions[cpval-1]}? List at least 4 of them.")

            def market():
                global budget
                global originalBudget
                if budget == 650:
                    print("\n", f"{supplies[professions[cpval-1]]}".replace("{", "").replace("}", "").replace(",", "\n").replace(": ", ": $"),
                          f"\n\n What do you want to buy? You have a total of ${float(budget)}")
                else:
                    print("\n", f"{supplies[professions[cpval-1]]}".replace("{", "").replace("}", "").replace(",", "\n").replace(": ", ": $"),
                          f"\n\n What do you want to buy? You have a total of ${float(budget)}", "\n\r In order to leave the store. Type the word 'exit' ")
                customerChoice = input()
                if customerChoice != 'exit':
                    print(
                        f"A {customerChoice} costs {supplies[professions[cpval-1]][customerChoice]} how many do you want to buy?")
                    quantity = int(input())
                    originalBudget = float(budget -
                                           (quantity *
                                            supplies[professions[cpval-1]][customerChoice]))
                    if originalBudget > 0:
                        budget = originalBudget
                        print(f"You have now a total of ${float(budget)}")
                elif originalBudget > 0 and customerChoice == 'exit':
                    budget = 0
                if budget != 0 and originalBudget != 0:
                    if originalBudget < 0:
                        print(
                            "You can't take that much amount it's going to result as a negative number. Please try again.")
                    market()
                elif originalBudget == 0 and budget != 0:
                    budget == originalBudget
                    print("\n At least buy something")
                    market()
                elif budget == 0 and originalBudget == 0:
                    print(
                        "All your money has been spent. You have successfully reached the end to Zakaria's Assignment")
                elif budget == 0 and originalBudget != 0:
                    print(
                        "You have successfully reached the end to Zakaria's Assignment")

            def teamNames():
                ctnval1 = input("\r 1 ")
                team[0] = ctnval1
                ctnval2 = input("\r 2 ")
                team[1] = ctnval2
                ctnval3 = input("\r 3 ")
                team[2] = ctnval3
                ctnval4 = input("\r 4 ")
                team[3] = ctnval4
            teamNames()
            confirmation = input("\n Are all the names correct? ").lower()
            if confirmation == "yes":
                print(
                    f"Before pursuing your career amongst your {professions[cpval-1]} team. You need to buy some supplies.")
                market()
            elif confirmation == "no":
                alteration = int(
                    input("What team names do you want to change? _"))
                if 1 <= alteration <= 4:
                    altval = input(
                        f"What would you like to change it to \n\r {alteration} ")
                    team[alteration - 1] = altval
                    print("\n Here's is your final output")
                    alterTeam()
                    print(
                        f"Before pursuing your career amongst your {professions[cpval-1]} team. You need to buy some supplies.")
                    market()
            elif confirmation != "yes" or "no":
                print("\n Answer with either yes or no")
                confirmation = str(input("\n Are all the names correct? "))
        else:
            print("Sorry, try running the program again. Your values were invalid")