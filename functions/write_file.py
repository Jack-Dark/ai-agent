import os
from common.validate_path import validate_path
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path path to read from file, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content read from the specified file",
            ),
        },
        required=["file_path", "content"],
    ),
)


def write_file(working_directory, file_path, content):
    try:
        path = validate_path(working_directory, file_path)

        if not path["is_valid_target_dir"]:
            return f'Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(path["full_path"]):
            return f'Cannot write to "{path["full_path"]}" as it is a directory'

        os.makedirs(os.path.dirname(path["full_path"]), exist_ok=True)

        with open(path["full_path"], "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")
