import re
my_string = "I like to run in the morning."
my_string_1 = "Dabcaabc"
my_string_2 = "9"
def check_sentance(text):
    func1_regexp1 = re.findall("\A[A-Z][a-z]+\s", text)
    func1_regexp1_1 = re.findall("^[A-Z]", text)
    func1_regexp2 = re.findall("[.]{1}$", text)
    func1_regexp3 = re.findall("\w", text)
    func1_regexp4 = re.findall("\s", text)
    if func1_regexp1 or func1_regexp1_1 and func1_regexp2 and len(func1_regexp3)+len(func1_regexp4)+1==len(text) and len(func1_regexp4)>=2:
        print(True)
    else:
        print(False)
#        raise Exception("It is not right sentance.")

def check_upercase_and_lowercase(text):
    func2_regexp1 = re.findall("\A[A-Z]", text)
    func2_regexp2 = re.findall("[abc]", text)
    if func2_regexp1 and len(text)==(len(func2_regexp1)+len(func2_regexp2)):
        print(True)
    else:
         print(False)
#         raise Exception("This does not contain only abc or the first letter is not uppercase")
    
def natural_number(text):
    func3_regexp1 = re.findall("^[1-9]", text)
    if len(text)==1 and func3_regexp1:
        print(True)
    else:
        print(False)
 #       raise Exception("Enter only natural number.")
