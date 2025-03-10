import argparse
import os
from utils import check_syntax_errors,analyze_code_with_pylint,get_ai_debugging_suggestions

def debug_code(file_path):
    '''runs debugger for a given python file'''
    if not os.path.exists(file_path):
        print(f"ERROR:{file_path}not found")
        return
    
    with open(file_path,"r") as file:
        code=file.read()
        
    syntax_error=check_syntax_errors(code)
    if syntax_error:
        print(f"THE CODE HAS FOLLOWING ERROR:{syntax_error}")
        return
    
    pylint_errors=analyze_code_with_pylint(code)
    if not pylint_errors:
        print("NO ERRORS FOUND IN THE CODE")
        return
    
    ai_fix=get_ai_debugging_suggestions(code,pylint_errors)
    print("\n AI debugging suggestions:")
    print(ai_fix)
    
if __name__  == "__main__":
    parser=argparse.ArgumentParser(description="AI-powered python code debugger")
    parser.add_argument("file",help="path to python file to debug")
    args=parser.parse_args()
    debug_code(args.file)
