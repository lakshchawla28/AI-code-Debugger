import streamlit as st
from utils import check_syntax_errors, analyze_code_with_pylint, get_ai_debugging_suggestions

st.title("AI-POWERED CODE DEBUGGER")
code = st.text_area("Paste Your Python Code Here")  

if st.button("Debug Code"):
    if not code.strip():
        st.error("PLEASE ENTER SOME PYTHON CODE.")
    else:
        syntax_error = check_syntax_errors(code)

        if syntax_error:
            st.error(syntax_error)
        else:
            # Save code to a temporary file
            with open("temp.py", "w") as temp_file:
                temp_file.write(code)

            pylint_errors = analyze_code_with_pylint(temp_file)

            if not pylint_errors:
                st.success("NO ERRORS FOUND IN THE CODE")
            else:
                ai_fix = get_ai_debugging_suggestions(code, pylint_errors)

                st.write("**AI-DEBUGGING SUGGESTIONS**")
                if ai_fix:
                    st.code(ai_fix)
                else:
                    st.info("No AI suggestions available.")
