import ast

def ast_print(node: ast.Module):
    print(ast.dump(node, indent=1))