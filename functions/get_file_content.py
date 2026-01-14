import os
from common.validate_path import validate_path
from google.genai import types
from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file in a specified file path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path path to read from file, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    path = validate_path(working_directory, file_path)

    try:
        if not path["is_valid_target_dir"]:
            return f'Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path["full_path"]):
            return f'File not found or is not a regular file: "{path["full_path"]}"'

        with open(path["full_path"], "r") as file:
            file_content_string = file.read(MAX_CHARS)

            # After reading the first MAX_CHARS...
            if file.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return file_content_string

    except Exception as e:
        print(f"Error: {e}")
