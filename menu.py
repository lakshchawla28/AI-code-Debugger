import subprocess
import sys

def main():
    while True:
        print("\n🔹 AI-Powered Python Debugger")
        print("")
        print("1️⃣ Run CLI Debugger")
        print("2️⃣ Start Flask Web App")
        print("3️⃣ Start Streamlit App")
        print("4️⃣ Exit")
        
        choice=int(input("\n ENTER YOUR CHOICE : "))
        
        if choice==1:
            file_path=input("ENTER PYTHON FILE PATH TO DEBUG : ")
            subprocess.run(["python","main.py",file_path])
            
        elif choice==2:
            print("STARTING FLASK WEB APP....")
            subprocess.run(["python","web_flask.py"])
            
        elif choice == 3:
            print("STARTING STREAMLIT WEB APP...")
            subprocess.run([sys.executable, "-m", "streamlit", "run", "web_streamlit.py"], check=True)



        
        elif choice==4:
            print("Exiting... 🚀")
            print("\nthank youu !!!")
            print("")
            print("MADE BY LAKSH")
            break
        
        else:
            print("INVALID CHOICE!,PLEASE ENTER VALID OPTION..")
            
if __name__ =="__main__":
    main()
