import ast

def parse_source_code(source_code):
    
    tree = ast.parse(source_code)
    functions = []

    
    for node in ast.walk(tree):
        
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)  

    return functions
