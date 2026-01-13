from functions.run_python_file import run_python_file


def main():
    test("calculator", "main.py")  # (should print the calculator's usage instructions)
    test(
        "calculator", "main.py", ["3 + 5"]
    )  # (should run the calculator... which gives a kinda nasty rendered result)
    test("calculator", "tests.py")  # (should run the calculator's tests successfully)
    test("calculator", "../main.py")  # (this should return an error)
    test("calculator", "nonexistent.py")  # (this should return an error)
    test("calculator", "lorem.txt")  # (this should return an error)


def test(working_directory, directory, args=None):
    if directory == ".":
        print(f"Result for current directory:")
    else:
        print(f"Result for '{directory}' file:")
    result = run_python_file(working_directory, directory, args)
    print(result)


if __name__ == "__main__":
    main()
