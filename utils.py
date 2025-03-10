import ast
import subprocess
import openai
import config

openai_api_key=config.OPENAI_API_KEY

def check_syntax_errors(code):
    '''checks python syntax errors using ast(abstract syntax tree)'''
    
    try:
        ast.parse(code)
        return None
    
    except SyntaxError as e:
        return f"syntax error:{e}"
    
def analyze_code_with_pylint(file_path):
    '''runs pylint on python file to detect logical errors'''
    
    result=subprocess.run(["pylint",file_path,"--errors only"],capture_output=True,text=True)
    
    return result.stdout.strip()

def get_ai_debugging_suggestions(code, errors):
    '''uses openai api to analyze and fix code errors'''
    
    prompt= f"This is the python code with errors :\n\n{code}Errors:\{errors}\n explain and suggests fixes accordingly"
    
    response=openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"system","content":prompt}]
    )
    
    return response["choices"][0]["messages"]["content"]
