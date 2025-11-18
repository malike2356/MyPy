# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

my_name = "Malike"
my_age = 38
is_Male = True
is_Female = False
company_name = 'Velox'
longest_word = "supercalifragilisticexpialidocious"

print(my_name + " is ", my_age, "years old")
print("When " + my_name + " was not ", my_age,
      ", He was much younger and Fresh.\nSo Fresh that His friends used to call him", my_name, ", the Fresh")
print(company_name.upper() + " is a company founded by " + my_name)
print("So, Is it ", company_name.upper().isupper(), " that the name ", company_name.upper(),
      " is always rendered in Upper Case?")
print(company_name.isupper())
print("the Former name for", company_name, "is", company_name.replace("Velox", "Agilis Consult"))
print()
print("Do you know the longest word is: \""+longest_word+"\"")
print("The length of", longest_word.upper() + " is: " + str(len(longest_word)), "characters")
print("The first character in " + longest_word.lower() + " is: " + longest_word[0])
print("The Fifth character in " + longest_word.lower() + " is: " + longest_word[5 - 1])
print("the index of " + str(longest_word[8-1]) + " in " + longest_word.upper() + " is " + str(longest_word.index("l")))
print("Index is therefore the position of a character deduce by subtracting 1 from the length of the character")
print()
