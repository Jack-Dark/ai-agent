import os
from common.validate_path import validate_path
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    path = validate_path(working_directory, file_path)

    try:
        if not path["is_valid_target_dir"]:
            raise Exception(
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )
        if not os.path.isfile(path["full_path"]):
            raise Exception(
                f'File not found or is not a regular file: "{path["full_path"]}"'
            )

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
