from functions.get_files_info import *

def run_tests():
    print("Result for current directory:")
    print(run_python_file("calculator", "main.py"))
    print()

    print("Result for current directory:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))    
    print()

    print("Result for current directory:")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("Result for current directory:")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("Result for current directory:")
    print(run_python_file("calculator", "nonexistent.py"))
    print()

if __name__ == "__main__":
    run_tests()