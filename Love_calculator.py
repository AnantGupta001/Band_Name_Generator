# DAY 3

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
T = lower_name1.count("t") + lower_name2.count("t")
R = lower_name1.count("r") + lower_name2.count("r")
U = lower_name1.count("u") + lower_name2.count("u")
Ee = lower_name1.count("e") + lower_name2.count("e")
L = lower_name1.count("l") + lower_name2.count("l")
O = lower_name1.count("o") + lower_name2.count("o")
V = lower_name1.count("v") + lower_name2.count("v")
E = lower_name1.count("e") + lower_name2.count("e")
Total1 = str(T + R + U + Ee)
Total2 = str(L + O + V + E)
Love_Score = int(Total1 + Total2)
if Love_Score < 10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score >= 40 and Love_Score <= 50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")
