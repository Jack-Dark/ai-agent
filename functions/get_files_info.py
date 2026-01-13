import os


def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_dir_abs, directory)
    target_dir = os.path.normpath(full_path)
    # Will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    try:

        if not valid_target_dir:
            raise Exception(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
        if not os.path.isdir(full_path):
            raise Exception(f'Error: "{full_path}" is not a directory')
        target_dir_contents = os.listdir(full_path)
        for item in target_dir_contents:
            item_path = f"{full_path}/{item}"
            print(
                f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            )
    except Exception as e:
        print(e)
