from flask import Flask, request
from utils import check_syntax_errors, analyze_code_with_pylint, get_ai_debugging_suggestions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":  
        file = request.files["file"]  

        if file:
            code = file.read().decode("utf-8")

            syntax_error = check_syntax_errors(code)
            if syntax_error:
                return f"<h3>{syntax_error}</h3>" 

            with open("temp.py", "w") as temp_file:
                temp_file.write(code)

            pylint_errors = analyze_code_with_pylint("temp.py")

            if not pylint_errors:
                return "<h3>No errors found!!!</h3>" 

            ai_fix = get_ai_debugging_suggestions(code, pylint_errors)
            return f"<h3>AI DEBUGGING SUGGESTIONS:</h3><pre>{ai_fix}</pre>"

    return '''<form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>'''

if __name__ == "__main__":
    app.run(debug=True)
