pre_order_traverse(root)
new_stack.reverse()
for node in new_stack:
    if node.value == 'let':
        print('reacehd let')
        std_let(node)
    elif node.value == 'where':
        std_where(node)
    elif node.value == 'fcn_form':
        std_fcn_form(node)
    elif node.value == 'tau':
        std_tuple(node, root)
    elif node.value == 'lambda':
        std_multi_param(node)
    elif node.value == 'within':
        print('reached within')
        std_within(node)
    