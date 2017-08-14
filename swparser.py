#parser.py
#by: gv_029
import sys
import os

def main():
    print("This program parses the sweep rules file from Outlook.com")
    print("Would you like to parse your file?")
    print("Press any button to start, or press n to exit")
    answer = input()

    if answer == "N" or "n":
        print("Goodbye")
        exit()
    else:
        reader()

def reader():
    f = open('Sweeprules.txt' , 'r').read()
    f_list = list(f)
    doc_len = (len(f_list))

    for i in range(doc_len):
        if f_list[i] == ">":
            f_list[i] = "/> \n"


    f_revised = ''.join(f_list)
    print("Sweep rules have been parsed!")
    f = open('SweepRules-parsed.txt', 'w')
    f.write(f_revised)
    f.close()





main()
