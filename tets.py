import string

with open("a.txt", "r") as file:
    file_content = file.read()
    print(file_content)

letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punction = [')', '(', ';', ',']
operator_symbol = ['+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=',
                   '~', '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?']
list_of_tokens = []
lst = []
space = [' ', '\t', '\n']
a = 0
while (a < len(file_content)):
    str = ""
    token = ""
    if (file_content[a] == '"'):
        token = "<String>"
        t = 0
        while (a < len(file_content) and (file_content[a] in punction or file_content[a] in space or file_content[a] == '\\' or file_content[a] == '\"' or file_content[a] in letter or file_content[a] in digit or file_content[a] in operator_symbol)):
            str += file_content[a]
            a += 1
            if (file_content[a] == '"'):
                str += file_content[a]
                a += 1
                break
    elif (file_content[a] in letter):
        token = "<Identifier>"
        while (a < len(file_content) and (file_content[a] in letter or file_content[a] in digit or file_content[a] == '_')):
            str += file_content[a]
            a += 1
    elif (file_content[a] in space):
        token = "<DELETE>"
        while (a < len(file_content) and file_content[a] in space):
            str += file_content[a]
            a += 1
    elif (file_content[a] in punction):
        str = file_content[a]
        token = file_content[a]
        a += 1
    elif (file_content[a] in operator_symbol):
        token = "<OPERATOR>"
        while (a < len(file_content) and file_content[a] in operator_symbol):
            str += file_content[a]
            a += 1
    elif (file_content[a] in digit):
        token = "<DIGIT>"
        while (a < len(file_content) and file_content[a] in digit):
            str += file_content[a]
            a += 1
    
    if token != '<DELETE>':
        list_of_tokens.append(str)


    print(repr(str), "=>", token)
    print(list_of_tokens)

    
class Stack:
        def __init__(self):
                self.stack = []
        
        def top(self):
                if len(self.stack) == 0:
                      return '$'
                return self.stack[-1]
        
        def push(self, element):
                self.stack.append(element)
        
        def pop(self):
                popped_ele = self.stack.pop()
        
        def isEmpty(self):
            if len(self.stack) == 0:
                  return True
                

        

def procE(next_token, stack: Stack):
        token_list = ['not', '(', 'i', 'true', 'false']
        if next_token in token_list:
                stack.pop()
                stack.push('X')
                stack.push('T')
                print('E -> TX')

def procT(next_token, stack: Stack):
        token_list = ['not', '(', 'i', 'true', 'false']
        if next_token in token_list:
                stack.pop()
                stack.push('Y')
                stack.push('F')
                print('T -> FY')

def procX(next_token, stack: Stack):
        if next_token == 'or':
                stack.pop()
                stack.push('X')
                stack.push('T')
                stack.push('or')
                print('X -> or T X')
        
        if next_token == 'nor':
                stack.pop()
                stack.push('X')
                stack.push('T')
                stack.push('nor')
                print('X -> not T X')

        if next_token == 'xor':
                stack.pop()
                stack.push('X')
                stack.push('T')
                stack.push('xor')
                print('X -> xor T X')
        
        if next_token == ')' or next_token == "$":
                stack.pop()
                print('X -> ')
        

def procY(next_token, stack: Stack):
        token_list = ['or', 'nor', 'xor', ')']

        if next_token == 'and':
                stack.pop()
                stack.push('T')
                stack.push('and')
                print('Y -> and T')
                
        
        if next_token == 'nand':
                stack.pop()
                stack.push('T')
                stack.push('nand')
                print('Y -> nand T')


        if next_token in token_list or next_token == "$":
                stack.pop()
                print('Y ->')


def procF(next_token, stack: Stack):
        token_list = ['(', 'i', 'true', 'false']
        if next_token == 'not':
                stack.pop()
                stack.push('F')
                stack.push('not')
                print('F -> not F')
        
        if next_token in token_list:
                stack.pop()
                stack.push('P')
                print('F -> P')
        
def procP(next_token, stack: Stack):
        token_list = ['i', 'true', 'false']
        if next_token == '(':
                stack.pop()
                stack.push(')')
                stack.push('E')
                stack.push('(')
                print('P -> (E)')
        
        if next_token in token_list:
                stack.pop()
                stack.push(next_token)
                print(f'P->{next_token}')
        
non_terminals = ['E', 'T', 'X', 'F', 'Y', 'P']
terminals = ['or', 'nor', 'xor', 'and', 'nand', 'not', '(', ')', 'true', 'false', 'i']
stack = Stack()
stack.push('E')
print(list_of_tokens)
list_of_tokens.append('$')
for token in list_of_tokens:
    while(True):
        if stack.isEmpty():
            break
        if stack.top() == 'E':
            procE(token, stack)
        if stack.top() == 'T':
            procT(token, stack)
        if stack.top() == 'X':
            procX(token, stack)
        if stack.top() == 'F':
            procF(token, stack)
        if stack.top() == 'Y':
            procY(token, stack)
        if stack.top() == 'P':
            procP(token, stack) 
        if stack.top() in terminals:
            if stack.top() == token:
                stack.pop()
                print(" ")
                break
    if token == '$':
        break
            

