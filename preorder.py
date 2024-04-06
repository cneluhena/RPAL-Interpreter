def post_to_pre(post_order):
    stack = []
    
    for token in reversed(post_order):
        if token[1] == 0:  # If token is an operand
            stack.append(token)
        else:  # If token is an operator
            if token[0] in ['gamma', 'tau', ',', 'eq', '-', '+', '->', 'rec', 'where', 'let']:
                operands = []
                for _ in range(token[1]):
                    operands.append(stack.pop())
                operands.reverse()
                stack.append(token)
                stack.extend(operands)
            else:
                stack.append(token)
    
    return stack

post_order = [('<ID:Sum>', 0), ('<ID:A>', 0), ('<ID:Psum>', 0), ('<ID:A>', 0), ('<ID:Order>', 0), ('<ID:A>', 0), 
              ('gamma', 2), ('tau', 2), ('gamma', 2), ('<ID:Psum>', 0), ('<ID:T>', 0), ('<ID:N>', 0), (',', 2), 
              ('<ID:N>', 0), ('<INT:0>', 0), ('eq', 2), ('<INT:0>', 0), ('<ID:Psum>', 0), ('<ID:T>', 0), 
              ('<ID:N>', 0), ('<INT:1>', 0), ('-', 2), ('tau', 2), ('gamma', 2), ('<ID:T>', 0), ('<ID:N>', 0), 
              ('gamma', 2), ('+', 2), ('->', 3), ('fcn_form', 3), ('rec', 1), ('where', 2), ('fcn_form', 3), 
              ('<ID:Print>', 0), ('<ID:Sum>', 0), ('<INT:1>', 0), ('<INT:2>', 0), ('<INT:3>', 0), ('<INT:4>', 0), 
              ('<INT:5>', 0), ('tau', 5), ('gamma', 2), ('gamma', 2), ('let', 2)]

pre_order = post_to_pre(post_order)
print(pre_order)