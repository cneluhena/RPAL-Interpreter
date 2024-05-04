pre_order_traverse(root)
new_stack.reverse()
for node in new_stack:
    if node.value == 'let':
        std_let(node)
    elif node.value == 'where':
        std_where(node)
    elif node.value == 'fcn_form':
        std_fcn_form(node)
    elif node.value == 'tau':
        std_tuple(node)