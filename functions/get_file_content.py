import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
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
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )
        if not os.path.isfile(full_path):
            raise Exception(f'File not found or is not a regular file: "{file_path}"')

        with open(full_path, "r") as file:
            file_content_string = file.read(MAX_CHARS)

            # After reading the first MAX_CHARS...
            if file.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return file_content_string

    except Exception as e:
        print(f"Error: {e}")
