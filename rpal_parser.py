
class Stack:
        def __init__(self):
                self.stack = []
        
        def top(self):
                return self.stack[-1]
        
        def push(self, element):
                self.stack.append(element)
        
        def pop(self):
                popped_ele = self.stack.pop()
                

        

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
                print('X -> not T X')
        
        if next_token == ')' or next_token == '':
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


        if next_token in token_list:
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

        if next_token == 'i':
                stack.pop()
                stack.push('i')
                print('P->i')
        
        if next_token in token_list:
                stack.pop()
                stack.push(next_token)
                print(f'P->{next_token}')
        
non_terminals = ['E', 'T', 'X', 'F', 'Y', 'P']
non_terminals = ['or', 'nor', 'xor', 'and', 'nand', 'not', '(', ')', 'true', 'false']
stack = Stack()
stack.push('E')
while(True):
        



        









        






        
        


