from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content

def run_tests():
    print("Result for current directory:")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Result for current directory:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Result for current directory:")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Result for current directory:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()

if __name__ == "__main__":
    run_tests()