import os
from common.validate_path import validate_path


def get_files_info(working_directory, directory="."):

    path = validate_path(working_directory, directory)
    try:

        if not path["is_valid_target_dir"]:
            raise Exception(
                f'Cannot list "{directory}" as it is outside the permitted working directory'
            )
        if not os.path.isdir(path["full_path"]):
            raise Exception(f'"{path["full_path"]}" is not a directory')
        target_dir_contents = os.listdir(path["full_path"])
        for item in target_dir_contents:
            item_path = f"{path["full_path"]}/{item}"
            print(
                f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            )
    except Exception as e:
        print(f"Error: {e}")
