from functions.get_file_content import get_file_content


def main():
    test("calculator", "lorem.txt")
    test("calculator", "main.py")
    test("calculator", "pkg/calculator.py")
    test("calculator", "/bin/cat")
    test("calculator", "pkg/does_not_exist.py")


def test(working_directory, file_path):
    if file_path == ".":
        print(f"Result for current file path:")
    else:
        print(f"Result for '{file_path}' file path:")
    result = get_file_content(working_directory, file_path)
    print(result)


if __name__ == "__main__":
    main()
