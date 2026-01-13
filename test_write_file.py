from functions.write_file import write_file


def main():
    test("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    test("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    test("calculator", "/tmp/temp.txt", "this should not be allowed")


def test(working_directory, directory, content):
    if directory == ".":
        print(f"Result for current directory:")
    else:
        print(f"Result for '{directory}' directory:")
    result = write_file(working_directory, directory, content)
    print(result)


if __name__ == "__main__":
    main()
