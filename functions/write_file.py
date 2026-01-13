import os
from config import MAX_CHARS


def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_dir_abs, file_path)
    target_dir = os.path.normpath(full_path)
    # Will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    try:
        if not valid_target_dir:
            raise Exception(
                f'Cannot write to "{file_path}" as it is outside the permitted working directory'
            )
        if os.path.isdir(full_path):
            raise Exception(f'Cannot write to "{file_path}" as it is a directory')

        os.makedirs(file_path, exist_ok=True)
        with open(full_path, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")
