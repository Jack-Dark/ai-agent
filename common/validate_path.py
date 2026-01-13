import os


def validate_path(working_directory, file_path):
    working_dir_abs: str = os.path.abspath(working_directory)
    full_path: str = os.path.join(working_dir_abs, file_path)
    target_dir: str = os.path.normpath(full_path)
    is_valid_target_dir: bool = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    return {
        "is_valid_target_dir": is_valid_target_dir,
        "working_dir_abs": working_dir_abs,
        "full_path": full_path,
        "target_dir": target_dir,
    }
