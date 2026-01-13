from functions.get_files_info import get_files_info


def main():
    test("calculator", ".")
    test("calculator", "pkg")
    test("calculator", "/bin")
    test("calculator", "../")


def test(working_directory, directory):
    if directory == ".":
        print(f"Result for current directory:")
    else:
        print(f"Result for '{directory}' directory:")
    result = get_files_info(working_directory, directory)
    print(result)


if __name__ == "__main__":
    main()
