import os
from common.validate_path import validate_path


def write_file(working_directory, file_path, content):

    try:
        path = validate_path(working_directory, file_path)

        if not path["is_valid_target_dir"]:
            raise Exception(
                f'Cannot write to "{file_path}" as it is outside the permitted working directory'
            )

        if os.path.isdir(path["full_path"]):
            raise Exception(
                f'Cannot write to "{path["full_path"]}" as it is a directory'
            )

        os.makedirs(file_path, exist_ok=True)
        with open(path["full_path"], "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")
